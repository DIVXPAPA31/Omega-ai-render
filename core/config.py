import os

class Config:
    # API Keys
    OPENAI_KEY = os.environ.get("OPENAI_KEY", "sk-5678mnopqrstuvwx5678mnopqrstuvwx5678mnop")
    GROQ_KEY = os.environ.get("GROQ_KEY", "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")
    ANTHROPIC_KEY = os.environ.get("ANTHROPIC_KEY", "AQ.Ab8RN6Ks0UHRbaH6auNWfKGlM_fSa23RI965MBmfvzQxpfL6ng")
    
    # Admin
    ADMIN_KEY = "omega-master-2026"
    
    # Models
    OPENAI_MODEL = "gpt-4-turbo-preview"
    GROQ_MODEL = "mixtral-8x7b-32768"
    ANTHROPIC_MODEL = "claude-3-opus-20240229"