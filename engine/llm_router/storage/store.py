from typing import Any
from engine_dataclasses.main_dc import (ContextWindow, OperationStatus)

OPENAI = {
    'ContextWindow': ContextWindow, # Free - 128,000 
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

ANTHROPIC = {
    'ContextWindow': ContextWindow, # Free -  200,000
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

GOOGLE = {
    'ContextWindow': ContextWindow, # Free - 1,000,000 and 2,097,152
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

MISTRAL = {
    'ContextWindow': ContextWindow, # Free - 128,000
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

COHERE = {
    'ContextWindow': ContextWindow, # 128000   Standard flagship limit (Command R series up to 256,000)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

PERPLEXITY = {
    'ContextWindow': ContextWindow, # 127072  Standard Sonar maximum limit (varies down to 8,192 depending on endpoint)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

OPENROUTER = {
    'ContextWindow': ContextWindow, # 2097152  Model Dependent (Ranges from 4,096 up to 2M for Gemini endpoints)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

GROQ = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Typically 8k–32k; up to 131,072 for Llama 3 series)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

TOGETHER = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Standard open-source weights up to 131,072 tokens)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

HF = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Varies widely by repository; up to 128k/131k for modern open weights)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

DEEPINFRA = {
    'ContextWindow': ContextWindow, # 131072  Model Dependent (Typically matches open-source model weights up to 131,072)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

AZUREOAI = {
    'ContextWindow': ContextWindow, # 128000  Standard flagship OpenAI tier (GPT-4o/o1 series)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

AWS = {
    'ContextWindow': ContextWindow, # 300000  Model Dependent (Up to 200k for Claude 3.5, 300k for Amazon Nova flagships)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

VERTEX = {
    'ContextWindow': ContextWindow, # 2097152  Model Dependent (Up to 2,097,152 for native Gemini 1.5/2.0 Pro)
    'Status': OperationStatus,
    'RPM': int,
    'PREFIX': ""
}

MODEL_CATALOG: set[str] = {
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

CONFIG_CATALOG: dict[object[str, Any]] = {
  'OPENAI': OPENAI,
  'ANTHROPIC': ANTHROPIC, 
  'GOOGLE': GOOGLE,
  'MISTRAL': MISTRAL,
  'COHERE': COHERE,
  'PERPLEXITY': PERPLEXITY,
  'OPENROUTER': OPENROUTER,
  'GROQ': GROQ,
  'TOGETHER': TOGETHER,
  'HF': HF,
  'DEEPINFRA': DEEPINFRA,
  'AZUREOAI': AZUREOAI,
  'AWS': AWS,
  'VERTEX': VERTEX
}