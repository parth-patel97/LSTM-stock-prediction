# AGENTS.md

Guidelines for AI coding agents working on this project.

## Project Overview

LSTM Stock Price Prediction API built with FastAPI.

## Tech Stack

- Python 3.8
- FastAPI 0.76.0
- Uvicorn 0.17.6
- Pydantic 1.9.0

## Project Structure

```
/
├── api.py           # FastAPI application entry point
├── models.py        # Data models (placeholder)
├── schema.py        # Pydantic schemas (placeholder)
├── test.py          # Tests (placeholder)
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker build configuration
└── runtime.txt      # Runtime specification
```

## Build & Run

### Local Development

```bash
pip install -r requirements.txt
uvicorn api:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t lstm-prediction .
docker run -p 8000:8000 lstm-prediction
```

## API Endpoints

- `POST /get_closing_price_app` - Returns closing price prediction

## Dependencies

All dependencies are pinned in `requirements.txt`. Install with:
```bash
pip install --no-cache-dir --upgrade -r requirements.txt
```

## Notes for Agents

- Entry point is `api:app` in `api.py`
- Container runs on port 8000
- Working directory in Docker is `/LSTM-Prediction`
