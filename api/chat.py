from fastapi import HTTPException
from core.utils import inject_omega_personality, generate_id, timestamp
from api.omega_core import get_omega_prompt
from api.providers import Providers

async def process_chat(messages, model, temperature, max_tokens):
    messages = get_omega_prompt(messages)
    
    providers = []
    if model in ["auto", "openai"]: providers.append(("openai", Providers.openai))
    if model in ["auto", "groq"]: providers.append(("groq", Providers.groq))
    if model in ["auto", "anthropic"]: providers.append(("anthropic", Providers.anthropic))
    
    for name, func in providers:
        try:
            result = await func(messages, temperature, max_tokens)
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            if content:
                return {
                    "id": generate_id(),
                    "created": timestamp(),
                    "provider": name,
                    "response": inject_omega_personality(content),
                    "model": model
                }
        except:
            continue
    
    raise HTTPException(500, "All providers failed")