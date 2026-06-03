from __future__ import annotations

import re


def compress_memory(text: str, max_sentences: int = 2, max_chars: int = 280) -> str:
    cleaned = " ".join(text.strip().split())
    if not cleaned:
        raise ValueError("Memory text cannot be empty.")

    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    summary = " ".join(sentences[:max_sentences]).strip()
    if len(summary) <= max_chars:
        return summary
    return summary[: max_chars - 3].rstrip() + "..."

