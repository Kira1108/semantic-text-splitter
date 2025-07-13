from dataclasses import dataclass
from openai import AzureOpenAI
from pydantic import BaseModel
from typing import Type, Optional
import instructor
from semantic_splitter.config import config

@dataclass  
class OpenAI:
    """A dataclass to hold OpenAI client configuration."""
    azure_endpoint: str = None
    api_key: str = None
    api_version: str = "2024-08-01-preview"
    timeout:int = 60
    model:str = "gpt-4o"
    
    def __post_init__(self):
        if not self.azure_endpoint:
            self.azure_endpoint = config.azure_endpoint
            
        if not self.api_key:
            self.api_key = config.api_key
            
        if (not self.api_key) or (not self.azure_endpoint):
            raise ValueError("Azure endpoint and API key must be provided.")
        
        self._client = AzureOpenAI(
            azure_endpoint=self.azure_endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
            timeout=self.timeout
        )
    
    def chat(self, messages:list):
        return self._client.chat.completions.create(
            model = "gpt-4o",
            messages = messages
        ).choices[0].message.content.strip()

@dataclass
class InstructOpenAI:
    azure_endpoint: str = None
    api_key: str = None
    api_version: str = "2024-08-01-preview"
    timeout:int = 60
    model:str = "gpt-4o"
    response_model: Optional[Type[BaseModel]] = None
    
    def __post_init__(self):
        if not self.azure_endpoint:
            self.azure_endpoint = config.azure_endpoint
            
        if not self.api_key:
            self.api_key = config.api_key
            
        if (not self.api_key) or (not self.azure_endpoint):
            raise ValueError("Azure endpoint and API key must be provided.")
        
        self._client = instructor.from_openai(
            AzureOpenAI(
                azure_endpoint=self.azure_endpoint,
                api_key=self.api_key,
                api_version=self.api_version,
                timeout=self.timeout
            )
        )
        
    def chat(self, messages:list):
        response = self._client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_model=self.response_model
        )
        return response
    
    
    

