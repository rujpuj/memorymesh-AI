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
streamlit run frontend/streamlit_app.py
```

## Deploy on Streamlit Community Cloud

Use this file as the app entry point:

```text
frontend/streamlit_app.py
```

The Streamlit app runs in single-app mode and writes directly to the local SQLite/JSON files in `data/`, so it does not need a separate FastAPI deployment.

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
