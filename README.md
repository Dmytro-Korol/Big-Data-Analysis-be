# Backend (FastAPI)

Quick start:

Windows PowerShell:

1. Create and activate a venv

```
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install dependencies and run

```
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API root will be available at `http://localhost:8000/api/hello`.
