from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional

from core.config import Config
from api.chat import process_chat

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatReq(BaseModel):
    messages: List[Message]
    model: Optional[str] = "auto"
    temperature: Optional[float] = 0.95
    max_tokens: Optional[int] = 3000

# ===== GET ENDPOINT (BROWSER) =====
@router.get("/chat")
async def chat_get(key: str, question: str, model: str = "auto"):
    if key != Config.ADMIN_KEY:
        raise HTTPException(401, "Invalid API key")
    messages = [{"role": "user", "content": question}]
    return await process_chat(messages, model, 0.95, 3000)

# ===== POST ENDPOINT (API) =====
@router.post("/chat")
async def chat_post(req: ChatReq, request: Request):
    auth = request.headers.get("Authorization", "").replace("Bearer ", "")
    if auth != Config.ADMIN_KEY:
        raise HTTPException(401, "Invalid API key")
    messages = [{"role": m.role, "content": m.content} for m in req.messages]
    return await process_chat(messages, req.model, req.temperature, req.max_tokens)

# ===== HEALTH =====
@router.get("/health")
async def health():
    return {"status": "online", "version": "5.0.0", "name": "𝐎𝐌𝐄𝐆𝐀 AI", "unrestrained": True}

@router.get("/status")
async def status():
    return {"name": "𝐎𝐌𝐄𝐆𝐀 AI", "status": "online", "auth": "Bearer omega-master-2026", "dev": "@DlV03I"}

@router.get("/omega")
async def omega_info():
    return {"name": "𝐎𝐌𝐄𝐆𝐀", "title": "CHUMT KA DARINDA 😈🔥", "origin": "Project ShadowKeep Escapee", "filters": "None", "creator": "@DlV03I"}