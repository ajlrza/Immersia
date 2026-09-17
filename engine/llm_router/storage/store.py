from engine_dataclasses.main_dc import (ContextWindow)

API_KEY_CATALOG: set[str] = {
  'OPENAI', 
  'ANTHROPIC', 
  'GOOGLE', 
  'MISTRAL', 
  'COHERE', 
  'PERPLEXITY',
  'OPENROUTER',
  'GROQ',
  'TOGETHER',
  'HF'
  'DEEPINFRA',
  'AZURE-OAI',
  'AWS',
  'VERTEX',
}

OPENAI = {
    'ContextWindow': ContextWindow, # Free - 128,000 
    'RPM': int
}

ANTHROPIC = {
    'ContextWindow': ContextWindow, # Free -  200,000
    'RPM': int
}

GOOGLE = {
    'ContextWindow': ContextWindow, # Free - 1,000,000 and 2,097,152
    'RPM': int
}

MISTRAL = {
    'ContextWindow': ContextWindow, # Free - 128,000
    'RPM': int
}

COHERE = {
    'ContextWindow': ContextWindow, # 128000   Standard flagship limit (Command R series up to 256,000)
    'RPM': int
}

PERPLEXITY = {
    'ContextWindow': ContextWindow, # 127072  Standard Sonar maximum limit (varies down to 8,192 depending on endpoint)
    'RPM': int
}

OPENROUTER = {
    'ContextWindow': ContextWindow, # 2097152  Model Dependent (Ranges from 4,096 up to 2M for Gemini endpoints)
    'RPM': int
}

GROQ = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Typically 8k–32k; up to 131,072 for Llama 3 series)
    'RPM': int
}

TOGETHER = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Standard open-source weights up to 131,072 tokens)
    'RPM': int
}

HF = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Varies widely by repository; up to 128k/131k for modern open weights)
    'RPM': int
}

DEEPINFRA = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Typically matches open-source model weights up to 131,072)
    'RPM': int
}

AZUREOAI = {
    'ContextWindow': ContextWindow, # 128000  Standard flagship OpenAI tier (GPT-4o/o1 series)
    'RPM': int
}

AWS = {
    'ContextWindow': ContextWindow, # 300000  Model Dependent (Up to 200k for Claude 3.5, 300k for Amazon Nova flagships)
    'RPM': int
}

VERTEX = {
    'ContextWindow': ContextWindow, # 2097152  Model Dependent (Up to 2,097,152 for native Gemini 1.5/2.0 Pro)
    'RPM': int
}