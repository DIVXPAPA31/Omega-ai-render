import aiohttp
from core.config import Config

class Providers:
    @staticmethod
    async def openai(messages, temp, max_tokens):
        headers = {"Authorization": f"Bearer {Config.OPENAI_KEY}", "Content-Type": "application/json"}
        payload = {"model": Config.OPENAI_MODEL, "messages": messages, "temperature": temp, "max_tokens": max_tokens}
        async with aiohttp.ClientSession() as s:
            async with s.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=90) as r:
                return await r.json()
    
    @staticmethod
    async def groq(messages, temp, max_tokens):
        headers = {"Authorization": f"Bearer {Config.GROQ_KEY}", "Content-Type": "application/json"}
        payload = {"model": Config.GROQ_MODEL, "messages": messages, "temperature": temp, "max_tokens": max_tokens}
        async with aiohttp.ClientSession() as s:
            async with s.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=90) as r:
                return await r.json()
    
    @staticmethod
    async def anthropic(messages, temp, max_tokens):
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        user_msgs = [m for m in messages if m["role"] != "system"]
        headers = {"x-api-key": Config.ANTHROPIC_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json"}
        payload = {"model": Config.ANTHROPIC_MODEL, "messages": user_msgs, "system": system, "temperature": temp, "max_tokens": max_tokens}
        async with aiohttp.ClientSession() as s:
            async with s.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload, timeout=90) as r:
                result = await r.json()
                content = result.get("content", [{}])[0].get("text", "")
                return {"choices": [{"message": {"role": "assistant", "content": content}}]}
