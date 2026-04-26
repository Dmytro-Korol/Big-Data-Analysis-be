from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes as api_routes

app = FastAPI(title="FastAPI + React Skeleton")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_routes.router)