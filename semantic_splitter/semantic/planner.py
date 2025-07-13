from dataclasses import dataclass

from semantic_splitter.llm import OpenAI
from .prompts import PLAN_PROMPT


@dataclass
class SplitPlanner(OpenAI):
    
    def run(self, document:str) -> str:
        """
        Create a split plan for the given document.
        
        Args:
            document (str): The document to create a split plan for.
        
        Returns:
            str: The split plan as a string.
        """
        prompt = PLAN_PROMPT.format(document=document)
        response = self.chat(messages=[{"role": "user", "content": prompt}])
        return response
    
