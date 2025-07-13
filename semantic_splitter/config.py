from dataclasses import dataclass, field
import os

@dataclass
class Config:
    azure_endpoint: str = None
    api_key: str = None
    
    def __post_init__(self):
        if not self.azure_endpoint:
            self.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", None)
            
        if not self.api_key:
            self.api_key = os.getenv("AZURE_OPENAI_API_KEY", None)
            
config = Config()
