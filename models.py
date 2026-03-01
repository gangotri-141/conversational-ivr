from pydantic import BaseModel
from typing import Optional

class IVRRequest(BaseModel):
    session_id: str
    user_input: str
    current_menu: str

class AIRequest(BaseModel):
    text: str
    session_id: str

class AIResponse(BaseModel):
    intent: str
    response_text: str