# personal-blogging-platform

A RESTful API for a personal blog, built with Python, FastAPI and SQLite. It supports the four basic CRUD operations (create, read, update, delete) on articles.

## Tech stack

- Python 3.13
- FastAPI (web framework)
- SQLAlchemy (database toolkit)
- SQLite (database, stored in a local `blog.db` file)
- pytest (tests)

## Endpoints

| Method | URL | Description |
|---|---|---|
| GET | `/articles` | List all articles. Optional filter: `?tag=python` |
| GET | `/articles/{id}` | Get one article. Returns 404 if it doesn't exist |
| POST | `/articles` | Create an article. Returns 201 |
| PUT | `/articles/{id}` | Update an article. Returns 404 if it doesn't exist |
| DELETE | `/articles/{id}` | Delete an article. Returns 204 |

Example request body for POST and PUT:

```json
{
  "title": "My first post",
  "content": "Hello world",
  "tags": "python,backend"
}
```

Tags are stored as a comma-separated string. The server sets `id`, `published_at` and `updated_at` itself.

## Setup (Windows, PowerShell)

```
git clone https://github.com/ernlynnnn/personal-blogging-platform.git
cd personal-blogging-platform
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```
fastapi dev main.py
```

Open http://127.0.0.1:8000/docs for an interactive page where you can try every endpoint. The `blog.db` database file is created automatically on first run.

## Test

```
pytest
```

## Project structure

- `main.py`: the API endpoints
- `database.py`: database connection and session setup
- `models.py`: the `Article` table definition
- `schemas.py`: request and response data shapes
- `test_main.py`: automated test of the full CRUD cycle

## Possible improvements

- Move tags into their own table (many-to-many relationship)
- Add date filters to `GET /articles`
- Use a separate database for tests
- Add authentication for write endpoints