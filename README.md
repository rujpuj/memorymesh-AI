# MemoryMesh AI

MemoryMesh AI is a small starter project for storing, compressing, retrieving, and correcting user memories.

## Project Structure

```text
app/
  api.py
  compressor.py
  retriever.py
  memory.py
  learner.py
frontend/
  streamlit_app.py
data/
  memories.db
  corrections.json
tests/
```

## Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.api:app --reload
```

In another terminal:

```bash
streamlit run frontend/streamlit_app.py
```

## API

- `GET /health` checks the service.
- `POST /memories` stores a memory and compressed summary.
- `GET /memories` lists stored memories.
- `POST /retrieve` searches memories and returns a context block.
- `POST /corrections` stores feedback corrections.

## Tests

```bash
pytest
```
