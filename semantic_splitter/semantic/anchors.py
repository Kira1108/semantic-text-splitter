# pydantic_models.py
from typing import List

from pydantic import BaseModel, Field

from semantic_splitter.llm import InstructOpenAI

from .planner import SplitPlanner
from .prompts import ANCHOR_FINDER_PROMPT


class SemanticSplitAnchors(BaseModel):
    """
    Identifies a full sentence within a text that serves as the optimal semantic split point.
    MOST IMPORTANT: the anchoor sentence shoule be shortest possible, but long enough to be unique.(LESS THAN 15 CHINESE CHARACTERS)
    """
    anchor_sentences: List[str] = Field(..., 
        description="A list of short strings, each quoted EXACTLY from the original text, where the split should occur. These sentence will be the begining of a new chunk."
    )
    
    
class AnchorFinder:
    def __init__(self):
        self.planner = SplitPlanner()
        self.llm = InstructOpenAI(response_model=SemanticSplitAnchors) 

    def run(self, text: str) -> SemanticSplitAnchors:
        
        print("Planning the split...")
        plan = self.planner.run(document = text)
        print(f"Split plan: {plan}\n")
        print("Finding anchors based on the plan...")
        response = self.llm.chat(
            messages=[{"role": "user", "content": ANCHOR_FINDER_PROMPT.format(plan=plan, text=text)}],
        )
        print(f"Anchor sentences found: {response.anchor_sentences}\n")
        return response
    
    

