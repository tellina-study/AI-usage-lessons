"""Общие функции замера Кейса A (распознавание документов) — тот же вебхук
s10-raw-openrouter, ключ OpenRouter остаётся на стороне n8n. vision_call/extract_json/
to_data_url скопированы дословно из library/seminars/sem-12/stend/zamery-k1/harness2_lite.py
(С5: модель и вызов те же — openai/gpt-4o-mini, image_url data-URL, usage.include=true);
text_call добавлен для гибрида (OCR-текст вместо картинки, тот же JSON-промт)."""
import base64
import io
import json
import re

from PIL import Image

from harness_call import call_raw

CHAT_MODEL = "openai/gpt-4o-mini"


def vision_call(system_prompt, user_text, image_b64_dataurl, model=CHAT_MODEL, timeout=90):
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
    return _unpack(r)


def text_call(system_prompt, user_text, model=CHAT_MODEL, timeout=90):
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text},
        ],
        "usage": {"include": True},
    }
    r = call_raw("https://openrouter.ai/api/v1/chat/completions", body, timeout=timeout)
    return _unpack(r)


def _unpack(r):
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


SYS_EXTRACT = (
    "Ты — система автоматического извлечения значений из отсканированной формы-заявки. "
    "Верни СТРОГО валидный JSON-объект (без markdown-ограждения ```, без пояснений до "
    "или после — только сам JSON), в котором каждому ключу из списка полей соответствует "
    "значение этого поля ТАК, КАК ОНО НАПИСАНО В ДОКУМЕНТЕ (не пересказывай, не переводи, "
    "не форматируй заново). Если поле на документе отсутствует, нечитаемо или прочерк — "
    "верни null для этого ключа."
)


def build_user_prompt(targets):
    lines = ["Извлеки значения следующих полей документа (каждое — подпись поля на самом бланке):"]
    for i, t in enumerate(targets, 1):
        lines.append(f'field_{i}: "{t["q_text"]}"')
    keys = ", ".join(f"field_{i}" for i in range(1, len(targets) + 1))
    lines.append(f"Верни JSON с РОВНО этими ключами: {keys}.")
    return "\n".join(lines)


def to_data_url(path, q=90):
    im = Image.open(path).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=q)
    return f"data:image/jpeg;base64,{base64.b64encode(buf.getvalue()).decode()}"
