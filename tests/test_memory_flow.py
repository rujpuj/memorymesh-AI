from app.compressor import compress_memory
from app.memory import MemoryStore
from app.retriever import MemoryRetriever


def test_compress_memory_keeps_first_sentences_short() -> None:
    text = "Riya likes concise status updates. She prefers examples. This can be ignored."

    assert compress_memory(text, max_sentences=2) == (
        "Riya likes concise status updates. She prefers examples."
    )


def test_store_and_retrieve_memory(tmp_path) -> None:
    store = MemoryStore(tmp_path / "memories.db")
    store.add(
        content="Alex is building a retrieval memory system.",
        compressed="Alex is building retrieval memory.",
        importance=0.8,
    )

    retriever = MemoryRetriever(store)
    results = retriever.retrieve("retrieval", limit=1)

    assert len(results) == 1
    assert results[0].compressed == "Alex is building retrieval memory."

