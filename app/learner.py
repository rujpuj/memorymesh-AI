from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_CORRECTIONS_PATH = Path(__file__).resolve().parents[1] / "data" / "corrections.json"


class CorrectionLearner:
    def __init__(self, path: Path | str = DEFAULT_CORRECTIONS_PATH) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

    def add_correction(self, prompt: str, answer: str, correction: str) -> dict:
        entry = {
            "prompt": prompt,
            "answer": answer,
            "correction": correction,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        corrections = self.list_corrections()
        corrections.append(entry)
        self.path.write_text(json.dumps(corrections, indent=2), encoding="utf-8")
        return entry

    def list_corrections(self) -> list[dict]:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

