#!/usr/bin/env bash
# tools/presentation-build/render-env.sh
#
# SOURCE this file (do not execute it) to put the project's no-root render toolchain on PATH:
#   soffice (LibreOffice headless, PPTX -> PDF), pdftoppm (PDF -> PNG), and, if built,
#   rsvg-convert (SVG -> PNG) + ImageMagick's `convert` (raster post-processing).
#
#   source tools/presentation-build/render-env.sh
#   soffice --headless --version && pdftoppm -v
#
# None of these tools are installed system-wide in this environment and there is no root/sudo
# (see notes/mcp-limitations.md #render-bootstrap-1). This file only EXPORTS variables pointing
# at an already-built no-root install; it never downloads or builds anything itself -- run
# render-bootstrap.sh first (once per host) if the toolchain isn't there yet. This file is safe
# to source repeatedly and safe to source even when the toolchain hasn't been built (it warns to
# stderr and leaves PATH alone rather than failing the whole shell).
#
# For the common "convert a .pptx to PNGs" case, prefer pptx_to_png.sh, which sources this file
# internally -- you do not need to source it yourself for that case.
#
# --- The $HOME-override trap (notes/mcp-limitations.md #sem03-render-1) and how this avoids it ---
# LibreOffice needs an isolated profile dir so its first-run bootstrap doesn't write into (or
# collide with) a real home directory across parallel runs. Earlier sessions in this project
# fixed that by overriding $HOME before calling soffice -- but Python's user-site-packages path
# (~/.local/lib/pythonX.Y/site-packages, where python-pptx/pymupdf actually live on this host,
# NOT a venv) is ALSO derived from $HOME, so overriding it silently made python-pptx/pymupdf
# unimportable in the same shell (ModuleNotFoundError, no error explaining why).
#
# This toolchain does not need that trade-off: soffice takes its own isolated-profile flag
# (`-env:UserInstallation=file://<dir>`) that does not touch $HOME at all -- see pptx_to_png.sh,
# which passes a fresh temp dir on every invocation. $HOME is never overridden anywhere in this
# file or in pptx_to_png.sh. The PYTHONPATH export below is kept anyway, purely as a defensive
# belt-and-braces measure in case a CALLER's own script overrides $HOME later in the same shell
# for some unrelated reason -- it costs nothing and closes the failure mode at its root instead
# of just working around it.

# Capture the real user-site path before anything below could ever change $HOME.
_render_env_real_user_site="$(python3 -c 'import site; print(site.getusersitepackages())' 2>/dev/null || true)"
if [ -n "$_render_env_real_user_site" ] && [ -d "$_render_env_real_user_site" ]; then
  case ":${PYTHONPATH:-}:" in
    *":$_render_env_real_user_site:"*) ;; # already present, don't duplicate
    *) export PYTHONPATH="${_render_env_real_user_site}${PYTHONPATH:+:$PYTHONPATH}" ;;
  esac
fi
unset _render_env_real_user_site

# --- Prefix defaults ---
# /home/harness/.local is the real (unix-user-level) home on this host, shared across every
# per-account worktree/session -- NOT the same directory as $HOME inside a Claude Code session,
# which harness-control points at a per-account dir under harness-control-data/accounts/.
# The platform LibreOffice installer (see render-bootstrap.sh) defaults its own PREFIX to
# `$HOME/.local` too, but only produces something useful there when actually run with the real
# $HOME -- on THIS host it already has, so /home/harness/.local is where the working install
# lives and where render-bootstrap.sh installs to by default. Falls back to the per-account
# $HOME/.local if /home/harness doesn't exist (a different host/environment).
if [ -z "${RENDER_PREFIX:-}" ]; then
  if [ -d /home/harness ]; then
    RENDER_PREFIX="/home/harness/.local"
  else
    RENDER_PREFIX="$HOME/.local"
  fi
fi
export RENDER_PREFIX
RENDER_EXTRAS_PREFIX="${RENDER_EXTRAS_PREFIX:-$RENDER_PREFIX/render-extras}"
export RENDER_EXTRAS_PREFIX

# --- Core: LibreOffice + poppler-utils ---
if [ -f "$RENDER_PREFIX/lo-portable-env.sh" ]; then
  # shellcheck disable=SC1090
  . "$RENDER_PREFIX/lo-portable-env.sh"
else
  echo "[render-env] WARNING: $RENDER_PREFIX/lo-portable-env.sh not found -- soffice/pdftoppm will not be on PATH. Run tools/presentation-build/render-bootstrap.sh first." >&2
fi

# --- Extras: rsvg-convert + ImageMagick (best-effort, non-fatal if never built) ---
if [ -d "$RENDER_EXTRAS_PREFIX/sysroot/usr/bin" ]; then
  export LD_LIBRARY_PATH="$RENDER_EXTRAS_PREFIX/sysroot/usr/lib/x86_64-linux-gnu${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
  export PATH="$RENDER_EXTRAS_PREFIX/sysroot/usr/bin:$PATH"
  export MAGICK_CONFIGURE_PATH="$RENDER_EXTRAS_PREFIX/sysroot/etc/ImageMagick-6"
  _render_env_im_moddir="$(find "$RENDER_EXTRAS_PREFIX/sysroot/usr/lib/x86_64-linux-gnu" -maxdepth 1 -type d -name 'ImageMagick-*' 2>/dev/null | head -1)"
  if [ -n "$_render_env_im_moddir" ]; then
    export MAGICK_CODER_MODULE_PATH="$_render_env_im_moddir/modules-Q16/coders"
  fi
  unset _render_env_im_moddir
  # apt's imagemagick-6.q16 ships the binary as `convert-im6.q16`; the plain `convert` name is
  # normally created by update-alternatives at real package-install time, which a no-root
  # `dpkg-deb -x` extraction never runs. Alias it so callers can just use `convert`.
  if ! command -v convert >/dev/null 2>&1 && command -v convert-im6.q16 >/dev/null 2>&1; then
    convert() { convert-im6.q16 "$@"; }
    export -f convert
  fi
fi
