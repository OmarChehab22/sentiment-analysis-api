# Sentiment Analysis API

A FastAPI-based sentiment analysis service using Hugging Face Transformers.

## Version
Current version: 1.0.0 (See [CHANGELOG.md](CHANGELOG.md) for details)

## Features

- Sentiment analysis of text input
- RESTful API endpoints
- Built with FastAPI and Hugging Face Transformers
- Uses the DistilBERT model fine-tuned on SST-2
- Swagger UI documentation
- Docker support (coming soon)

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add some feature"
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a Pull Request

### Branch Naming Convention

- Feature branches: `feature/your-feature-name`
- Bug fixes: `fix/your-fix-name`
- Documentation: `docs/your-docs-update`

### Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `test:` for adding tests
- `chore:` for maintenance tasks

## License

MIT License - see LICENSE file for details

## API Endpoints

### GET /
- Returns a welcome message

### POST /analyze
- Analyzes the sentiment of the provided text
- Request body:
```json
{
    "text": "Your text here"
}
```
- Response:
```json
{
    "sentiment": "POSITIVE" or "NEGATIVE",
    "confidence": 0.95
}
``` "# another test for commit from kamel" 
"# another test for commit from kamel" 
