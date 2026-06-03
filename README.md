# MemoryMesh AI

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A production-ready Streamlit-powered AI memory system with intelligent retrieval, compression, and self-correction capabilities. MemoryMesh AI enables efficient storage and retrieval of contextual information with automatic summarization and feedback-driven learning.

## Features

- **Memory Storage**: Persist user memories with automatic metadata extraction
- **Compression**: Intelligent summarization of stored memories to reduce redundancy
- **Retrieval**: Semantic search and context-aware memory retrieval
- **Self-Correction**: Learn from user feedback to improve memory accuracy
- **REST API**: Comprehensive API endpoints for programmatic access
- **Web Interface**: User-friendly Streamlit dashboard

## Quick Start

### Prerequisites

- Python 3.8+
- pip or conda package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rujpuj/memorymesh-AI.git
   cd memorymesh-AI
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

The application will be available at `http://localhost:8501`

## Project Structure

```
memorymesh-AI/
├── app/                          # Core application logic
│   ├── api.py                   # REST API endpoints
│   ├── memory.py                # Memory management core
│   ├── retriever.py             # Semantic retrieval engine
│   ├── compressor.py            # Memory compression module
│   └── learner.py               # Self-correction learning
├── frontend/
│   └── streamlit_app.py         # Web interface
├── data/
│   ├── memories.db              # SQLite database
│   └── corrections.json         # Feedback corrections
├── tests/                       # Test suite
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## API Reference

### Health Check
```http
GET /health
```
Verify service status.

### Store Memory
```http
POST /memories
Content-Type: application/json

{
  "content": "string",
  "metadata": "object"
}
```
Store a new memory with automatic compression.

### List Memories
```http
GET /memories
```
Retrieve all stored memories with summaries.

### Retrieve Context
```http
POST /retrieve
Content-Type: application/json

{
  "query": "string"
}
```
Search and retrieve relevant memories for a given query.

### Store Correction
```http
POST /corrections
Content-Type: application/json

{
  "memory_id": "string",
  "feedback": "string"
}
```
Submit user feedback to improve memory accuracy.

## Development

### Running Tests

```bash
pytest -v
```

### Code Quality

This project uses `black` for code formatting and `pylint` for linting:

```bash
black app/ frontend/ tests/
pylint app/ frontend/ tests/
```

### Environment Variables

Create a `.env` file in the project root:

```env
STREAMLIT_SERVER_PORT=8501
STREAMLIT_LOGGER_LEVEL=info
```

## Deployment

### Streamlit Cloud

1. Push repository to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with app entry point: `frontend/streamlit_app.py`

### Docker

```bash
docker build -t memorymesh-ai .
docker run -p 8501:8501 memorymesh-ai
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows project style guidelines
- All tests pass
- Documentation is updated

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Authors

- **rujpuj** - Initial development

## Acknowledgments

- [Streamlit](https://streamlit.io) - Web app framework
- [SQLite](https://www.sqlite.org) - Embedded database
- Community feedback and contributions

## Support

For issues, questions, or suggestions, please [open an issue](https://github.com/rujpuj/memorymesh-AI/issues) on GitHub.

---

**Last Updated**: June 2026
