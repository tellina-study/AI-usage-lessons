"""Общие функции замера Семинара 12, Кейс 1 — через тот же вебхук s10-raw-openrouter
(харнесс стенда Семинара 10, переиспользован без изменений), ключ OpenRouter остаётся
на стороне n8n. Адаптировано из library/seminars/sem-10/stend/measure/harness2.py —
cosine() скопирована дословно, embed_batch()/llm_answer() адаптированы под нужды этого
замера (vision-вызов с image_url, а не текстовый контекст)."""
import base64
import io
import json
import re

from PIL import Image

from harness_call import call_raw

CHAT_MODEL = "openai/gpt-4o-mini"
EMBED_MODEL = "openai/text-embedding-3-small"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def embed_batch(texts, model=EMBED_MODEL, timeout=120):
    body = {"model": model, "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    if "data" not in resp:
        raise RuntimeError(f"embed_batch failed: {json.dumps(resp, ensure_ascii=False)[:500]}")
    vecs = [d["embedding"] for d in resp["data"]]
    usage = resp.get("usage", {})
    return vecs, {"wall_s": r["wall_s"], "cost": usage.get("cost"), "prompt_tokens": usage.get("prompt_tokens")}


def vision_call(system_prompt, user_text, image_b64_dataurl, model=CHAT_MODEL, timeout=90):
    """Один вызов gpt-4o-mini с изображением на входе (content-блок image_url, data-URL).
    Температура не задаётся явно — используется дефолт провайдера (не 0), см. README
    «Модель и настройки» — честно, не скрыто."""
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": user_text},
                {"type": "image_url", "image_url": {"url": image_b64_dataurl}},
            ]},
        ],
        "usage": {"include": True},
    }
    r = call_raw("https://openrouter.ai/api/v1/chat/completions", body, timeout=timeout)
    resp = r["response"] or {}
    try:
        content = resp["choices"][0]["message"]["content"]
    except Exception:
        content = None
    usage = resp.get("usage", {})
    return {
        "exec_id": r["exec_id"], "wall_s": r["wall_s"], "node_ms": r["node_ms"],
        "content": content, "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"), "cost": usage.get("cost"),
        "raw_error": resp.get("error"),
    }


def extract_json(text):
    """Модель иногда оборачивает JSON в ```json ... ``` несмотря на просьбу — снимаем
    ограждение прежде json.loads, не иначе."""
    if text is None:
        return None
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\n?", "", t)
        t = re.sub(r"```\s*$", "", t)
        t = t.strip()
    try:
        return json.loads(t)
    except Exception:
        m = re.search(r"\{.*\}", t, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                return None
        return None


def parse_amount(s):
    """Снимает разделители тысяч (запятая ИЛИ точка — в этом корпусе (CORD, Indonesian
    Rupiah) обе используются как разделитель тысяч, не десятичной дроби — проверено
    вручную по 30 эталонным записям meta.json, см. README). Возвращает int или None."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return int(s)
    s = str(s)
    neg = "-" in s or s.strip().startswith("(") and s.strip().endswith(")")
    digits = re.sub(r"[^0-9]", "", s)
    if not digits:
        return None
    val = int(digits)
    return -val if neg else val


def word_count(s):
    """Токенизация одной формой для ВСЕХ трёх вариантов описания (С6: одна размерность
    на сравнение) — считает алфавитно-цифровые куски, включая внутри компактного JSON
    без пробелов (вариант «поля»), а не только split() по пробелу."""
    if not s:
        return 0
    return len(re.findall(r"[A-Za-zА-Яа-яЁё0-9]+", s))


def to_data_url(path, w=None, h=None, q=85):
    im = Image.open(path).convert("RGB")
    if w and h:
        im = im.resize((max(1, int(w)), max(1, int(h))), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


def hard_layout_data_url(path, target_w, target_h, q=85):
    """«Трудная раскладка»: поворот 12° + обрезка 4% с каждого края — ровно те же
    параметры аугментации, что measure/case4_full_retrieval_30.py::hard_dup в Семинаре 10
    (не переизобретено), затем ресайз до того же разрешения (target_w, target_h), что и
    «лёгкая» раскладка этого же шага шкалы — так меняется ТОЛЬКО раскладка, не заодно
    и резкость за счёт разных итоговых размеров."""
    im = Image.open(path).convert("RGB")
    hard = im.rotate(12, expand=True, fillcolor=(255, 255, 255))
    ww, hh = hard.size
    hard = hard.crop((int(ww * 0.04), int(hh * 0.04), int(ww * 0.96), int(hh * 0.96)))
    hard = hard.resize((max(1, int(target_w)), max(1, int(target_h))), Image.LANCZOS)
    buf = io.BytesIO()
    hard.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"


SCALE_STEPS = {
    "full": 1.0,
    "half": 0.5,
    "quarter": 0.25,
    "eighth": 0.125,
    "sixteenth": 1 / 16,
    "thirtysecond": 1 / 32,
}
