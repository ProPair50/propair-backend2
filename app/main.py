from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List  # 👈 new import

app = FastAPI(title="ProPair API (Baby Starter)", version="0.0.1")

# CORS: wide open while learning
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

# 👇 NEW ROUTE
@app.get("/providers")
def list_providers() -> List[dict]:
    # Mock data for now
    return [
        {"id": 1, "name": "Jhonny the Painter", "rating": 4.7},
        {"id": 2, "name": "Joshua Roofing", "rating": 4.9},
        {"id": 3, "name": "Ami Renovations", "rating": 4.5},
    ]
