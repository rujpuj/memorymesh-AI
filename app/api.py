from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.compressor import compress_memory
from app.learner import CorrectionLearner
from app.memory import MemoryStore
from app.retriever import MemoryRetriever


app = FastAPI(title="MemoryMesh AI", version="0.1.0")
store = MemoryStore()
retriever = MemoryRetriever(store)
learner = CorrectionLearner()


class MemoryIn(BaseModel):
    content: str = Field(..., min_length=1)
    importance: float = Field(0.5, ge=0, le=1)


class SearchIn(BaseModel):
    query: str = ""
    limit: int = Field(5, ge=1, le=25)


class CorrectionIn(BaseModel):
    prompt: str
    answer: str
    correction: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/memories")
def create_memory(payload: MemoryIn) -> dict:
    compressed = compress_memory(payload.content)
    return store.add(
        content=payload.content,
        compressed=compressed,
        importance=payload.importance,
    ).__dict__


@app.get("/memories")
def list_memories(limit: int = 50) -> list[dict]:
    return [memory.__dict__ for memory in store.list(limit=limit)]


@app.post("/retrieve")
def retrieve(payload: SearchIn) -> dict:
    memories = retriever.retrieve(query=payload.query, limit=payload.limit)
    return {
        "context": retriever.context_block(query=payload.query, limit=payload.limit),
        "memories": [memory.__dict__ for memory in memories],
    }


@app.post("/corrections")
def add_correction(payload: CorrectionIn) -> dict:
    return learner.add_correction(
        prompt=payload.prompt,
        answer=payload.answer,
        correction=payload.correction,
    )


@app.get("/corrections")
def list_corrections() -> list[dict]:
    return learner.list_corrections()
