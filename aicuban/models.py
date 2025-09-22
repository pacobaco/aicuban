from typing import Dict, List, Optional
from pydantic import BaseModel

class Procedure(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    suggested_codes: List[str] = []

class Decision(BaseModel):
    id: str
    question: str
    outcomes: Dict[str, str]

class Node(BaseModel):
    id: str
    type: str
    decision: Optional[Decision] = None
    procedure: Optional[Procedure] = None