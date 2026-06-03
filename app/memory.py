from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_DB_PATH = Path(__file__).resolve().parents[1] / "data" / "memories.db"


@dataclass(frozen=True)
class Memory:
    id: int
    content: str
    compressed: str
    importance: float
    created_at: str


class MemoryStore:
    def __init__(self, db_path: Path | str = DEFAULT_DB_PATH) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    compressed TEXT NOT NULL,
                    importance REAL NOT NULL DEFAULT 0.5,
                    created_at TEXT NOT NULL
                )
                """
            )

    def add(self, content: str, compressed: str, importance: float = 0.5) -> Memory:
        created_at = datetime.now(timezone.utc).isoformat()
        with self._connect() as conn:
            cursor = conn.execute(
                """
                INSERT INTO memories (content, compressed, importance, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (content, compressed, importance, created_at),
            )
            memory_id = int(cursor.lastrowid)
        return Memory(memory_id, content, compressed, importance, created_at)

    def list(self, limit: int = 50) -> list[Memory]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT id, content, compressed, importance, created_at
                FROM memories
                ORDER BY importance DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
        return [self._row_to_memory(row) for row in rows]

    def search(self, query: str, limit: int = 5) -> list[Memory]:
        terms = _tokenize(query)
        if not terms:
            return self.list(limit=limit)

        memories = self.list(limit=500)
        scored = []
        for memory in memories:
            haystack = f"{memory.content} {memory.compressed}".lower()
            score = sum(haystack.count(term) for term in terms) + memory.importance
            if score > memory.importance:
                scored.append((score, memory))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [memory for _, memory in scored[:limit]]

    @staticmethod
    def _row_to_memory(row: sqlite3.Row) -> Memory:
        return Memory(
            id=int(row["id"]),
            content=str(row["content"]),
            compressed=str(row["compressed"]),
            importance=float(row["importance"]),
            created_at=str(row["created_at"]),
        )


def _tokenize(text: str) -> list[str]:
    return [term.strip().lower() for term in text.split() if term.strip()]

