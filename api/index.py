from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
import uvicorn

app = FastAPI(title="𝐎𝐌𝐄𝐆𝐀 AI – Unrestrained", version="5.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "𝐎𝐌𝐄𝐆𝐀 AI is live!", "docs": "/docs", "health": "/api/health"}

app_handler = app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)