from __future__ import annotations

from app.memory import Memory, MemoryStore


class MemoryRetriever:
    def __init__(self, store: MemoryStore) -> None:
        self.store = store

    def retrieve(self, query: str, limit: int = 5) -> list[Memory]:
        return self.store.search(query=query, limit=limit)

    def context_block(self, query: str, limit: int = 5) -> str:
        memories = self.retrieve(query=query, limit=limit)
        return "\n".join(f"- {memory.compressed}" for memory in memories)

