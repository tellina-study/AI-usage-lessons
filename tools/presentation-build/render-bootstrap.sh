#!/usr/bin/env bash
# tools/presentation-build/render-bootstrap.sh
#
# Builds (once per host, no root) the no-root render toolchain this project's slide pipeline
# needs: soffice (LibreOffice headless, PPTX->PDF) + pdftoppm (PDF->PNG) as the required core,
# plus rsvg-convert + ImageMagick's `convert` as a best-effort extra. Idempotent: if a working
# install is already found (functionally verified, not just "a path exists"), it is reused and
# nothing is re-downloaded. Safe to re-run any time; set FORCE=1 to rebuild the core toolchain
# even if one already verifies.
#
# Usage:
#   tools/presentation-build/render-bootstrap.sh
#   RENDER_PREFIX=/custom/path tools/presentation-build/render-bootstrap.sh
#   FORCE=1 tools/presentation-build/render-bootstrap.sh
#
# After this succeeds, use tools/presentation-build/pptx_to_png.sh for conversions, or
# `source tools/presentation-build/render-env.sh` to get soffice/pdftoppm/rsvg-convert/convert
# on PATH directly.
#
# Why this exists at all (see notes/mcp-limitations.md #render-bootstrap-1 for the full
# writeup): none of these tools are installed system-wide here, there is no root/sudo
# (`no new privileges`), but `apt-get download` (fetch a .deb without installing it) DOES work
# -- so the whole toolchain is built by downloading .debs and extracting them with
# `dpkg-deb -x` (plain file extraction, needs no root) into a local prefix.
#
# Two install paths for the CORE toolchain, tried in order:
#   1. The platform-owned installer at /opt/harness-control/scripts/install-libreoffice-portable.sh,
#      if present. It downloads the official upstream LibreOffice .deb bundle plus an
#      iteratively-resolved (ldd-based) closure of missing system libs, and already existed on
#      this host with a working install at /home/harness/.local before this script was ever
#      written -- verified live in this session on library/seminars/_archive/sem-04-.../sem-04.pptx
#      (real PPTX -> real PDF -> real PNGs, Cyrillic text intact, ~23s for a 40-slide deck).
#      Preferred because it is the platform's own maintained recipe (iterative ldd-based
#      dependency resolution, handles release-specific package-name drift) -- reuse it rather
#      than re-solving the same problem worse.
#   2. A self-contained fallback recipe (this script), used only if #1 is unavailable: resolve
#      the FULL recursive dependency closure of the distro's own `libreoffice-impress` +
#      `poppler-utils` packages via `apt-cache depends --recurse`, download every package with
#      `apt-get download`, and flat-extract them all into one sysroot with `dpkg-deb -x`. This
#      path has NOT been exercised end-to-end in this session (path #1 succeeded first, and a
#      full libreoffice-impress closure is a large, slow download not worth re-doing just to
#      test a path that wasn't needed) -- if you hit it for real, verify it the same way this
#      script verifies path #1 below, and update the mcp-limitations.md entry with what you
#      found.
#
# EXTRAS (rsvg-convert, ImageMagick `convert`) always use the same apt-cache-depends-recurse
# recipe as fallback path #2 above (there is no platform installer for these) -- built and
# verified live in this session (98 packages, ~86 MB download, both binaries functionally
# tested: SVG->PNG and PNG resize).

set -euo pipefail

PLATFORM_INSTALLER="/opt/harness-control/scripts/install-libreoffice-portable.sh"

log() { echo "[render-bootstrap] $*" >&2; }

if [ -z "${RENDER_PREFIX:-}" ]; then
  if [ -d /home/harness ]; then
    RENDER_PREFIX="/home/harness/.local"
  else
    RENDER_PREFIX="$HOME/.local"
  fi
fi
RENDER_EXTRAS_PREFIX="${RENDER_EXTRAS_PREFIX:-$RENDER_PREFIX/render-extras}"
log "RENDER_PREFIX=$RENDER_PREFIX"
log "RENDER_EXTRAS_PREFIX=$RENDER_EXTRAS_PREFIX"

core_ready() {
  [ -f "$RENDER_PREFIX/lo-portable-env.sh" ] || return 1
  ( set +u; . "$RENDER_PREFIX/lo-portable-env.sh"; command -v soffice >/dev/null 2>&1 && command -v pdftoppm >/dev/null 2>&1 )
}

extras_ready() {
  local bin="$RENDER_EXTRAS_PREFIX/sysroot/usr/bin"
  [ -x "$bin/rsvg-convert" ] || return 1
  [ -x "$bin/convert" ] || [ -x "$bin/convert-im6.q16" ] || return 1
}

install_core_fallback() {
  log "Building core toolchain via fallback recipe (apt-cache depends --recurse on libreoffice-impress + poppler-utils)..."
  local work; work="$(mktemp -d)"
  mkdir -p "$work/debs" "$RENDER_PREFIX/lo-sysroot"
  ( cd "$work/debs"
    local pkgs
    pkgs="$(apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances \
        libreoffice-impress libreoffice-core poppler-utils fonts-dejavu-core fonts-liberation 2>/dev/null \
      | grep -E '^\w' | sort -u)"
    log "  resolved $(echo "$pkgs" | wc -l) packages, downloading..."
    # shellcheck disable=SC2086
    apt-get download $pkgs 2>&1 | tail -5 || true
    log "  extracting (dpkg-deb -x, no root) into $RENDER_PREFIX/lo-sysroot ..."
    for deb in *.deb; do
      [ -e "$deb" ] || continue
      dpkg-deb -x "$deb" "$RENDER_PREFIX/lo-sysroot/" 2>/dev/null || true
    done
  )
  rm -rf "$work"
  cat > "$RENDER_PREFIX/lo-portable-env.sh" <<EOF
# Generated by tools/presentation-build/render-bootstrap.sh (fallback apt-package recipe --
# the platform installer at $PLATFORM_INSTALLER was not available when this was built).
# soffice here comes from the distro libreoffice-impress package, so it lives under
# lo-sysroot/usr/lib/libreoffice/program, unlike the platform installer's separate
# libreoffice-portable/ tree.
export LO_SYSROOT="$RENDER_PREFIX/lo-sysroot"
export LD_LIBRARY_PATH="\$LO_SYSROOT/usr/lib/x86_64-linux-gnu\${LD_LIBRARY_PATH:+:\$LD_LIBRARY_PATH}"
export FONTCONFIG_FILE="\$LO_SYSROOT/etc/fonts/fonts.conf"
export PATH="\$LO_SYSROOT/usr/lib/libreoffice/program:\$LO_SYSROOT/usr/bin:\$PATH"
EOF
}

install_extras() {
  log "Building extras (rsvg-convert + ImageMagick) via apt-cache depends --recurse on librsvg2-bin + imagemagick..."
  local work; work="$(mktemp -d)"
  mkdir -p "$work/debs" "$RENDER_EXTRAS_PREFIX/sysroot"
  ( cd "$work/debs"
    local pkgs
    pkgs="$(apt-cache depends --recurse --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances \
        librsvg2-bin imagemagick 2>/dev/null | grep -E '^\w' | sort -u)"
    log "  resolved $(echo "$pkgs" | wc -l) packages, downloading..."
    # shellcheck disable=SC2086
    apt-get download $pkgs 2>&1 | tail -5 || true
    log "  extracting (dpkg-deb -x, no root) into $RENDER_EXTRAS_PREFIX/sysroot ..."
    for deb in *.deb; do
      [ -e "$deb" ] || continue
      dpkg-deb -x "$deb" "$RENDER_EXTRAS_PREFIX/sysroot/" 2>/dev/null || true
    done
  )
  rm -rf "$work"
}

# --- Core ---
if [ "${FORCE:-0}" = "1" ]; then
  log "FORCE=1 -- rebuilding core toolchain regardless of existing install."
elif core_ready; then
  log "Core toolchain already present and verified at $RENDER_PREFIX (soffice + pdftoppm) -- skipping install."
fi

if [ "${FORCE:-0}" = "1" ] || ! core_ready; then
  if [ -x "$PLATFORM_INSTALLER" ]; then
    log "Installing core via platform installer: $PLATFORM_INSTALLER"
    if ! PREFIX="$RENDER_PREFIX" "$PLATFORM_INSTALLER"; then
      log "Platform installer failed/exited non-zero -- will try the fallback recipe."
    fi
  else
    log "Platform installer not found at $PLATFORM_INSTALLER."
  fi
  core_ready || install_core_fallback
fi

core_ready || { log "ERROR: core toolchain (soffice + pdftoppm) still not usable after install attempts. See notes/mcp-limitations.md #render-bootstrap-1."; exit 1; }
log "Core toolchain verified: soffice + pdftoppm importable via $RENDER_PREFIX/lo-portable-env.sh"

# --- Extras (non-fatal) ---
if extras_ready; then
  log "Extras already present and verified at $RENDER_EXTRAS_PREFIX (rsvg-convert + convert) -- skipping install."
else
  install_extras || log "WARNING: extras install failed -- continuing without rsvg-convert/ImageMagick (non-fatal, core pipeline still works)."
  if extras_ready; then
    log "Extras verified: rsvg-convert + convert available via $RENDER_EXTRAS_PREFIX"
  else
    log "WARNING: extras still not usable after install attempt -- rsvg-convert/ImageMagick will not be on PATH. Core pipeline (soffice+pdftoppm) is unaffected."
  fi
fi

# --- Functional verification (not just "a path exists") ---
log "Running functional verification..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$SCRIPT_DIR/render-env.sh"

VERIFY_HOME_LOG="$(mktemp -t render-bootstrap-verify-XXXXXX.log)"
VERIFY_PROFILE="$(mktemp -d -t render-bootstrap-verify-profile-XXXXXX)"
if ! soffice --headless --norestore -env:UserInstallation="file://$VERIFY_PROFILE/lo_profile" --version > "$VERIFY_HOME_LOG" 2>&1; then
  log "ERROR: 'soffice --headless --version' did not run cleanly:"
  cat "$VERIFY_HOME_LOG" >&2
  rm -rf "$VERIFY_PROFILE"; rm -f "$VERIFY_HOME_LOG"
  exit 1
fi
if grep -qi "fontconfig error" "$VERIFY_HOME_LOG"; then
  log "ERROR: fontconfig misconfigured (missing fonts.conf/fonts):"
  cat "$VERIFY_HOME_LOG" >&2
  rm -rf "$VERIFY_PROFILE"; rm -f "$VERIFY_HOME_LOG"
  exit 1
fi
log "  soffice OK: $(cat "$VERIFY_HOME_LOG" | tr -d '\n')"
rm -rf "$VERIFY_PROFILE"; rm -f "$VERIFY_HOME_LOG"

pdftoppm -v > /dev/null 2>&1 || { log "ERROR: 'pdftoppm -v' did not run cleanly."; exit 1; }
log "  pdftoppm OK: $(pdftoppm -v 2>&1 | head -1)"

if command -v rsvg-convert >/dev/null 2>&1; then
  log "  rsvg-convert OK: $(rsvg-convert --version 2>&1)"
else
  log "  rsvg-convert not available (extras not built) -- non-fatal."
fi
if command -v convert >/dev/null 2>&1; then
  log "  convert OK: $(convert --version 2>&1 | head -1)"
else
  log "  convert not available (extras not built) -- non-fatal."
fi

log "Done. Core prefix: $RENDER_PREFIX  |  extras prefix: $RENDER_EXTRAS_PREFIX"
log "Use it: source $SCRIPT_DIR/render-env.sh   -- or --   $SCRIPT_DIR/pptx_to_png.sh <in.pptx> <out-dir>"
