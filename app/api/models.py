from pydantic import BaseModel
from typing import List, Optional, Dict

class HexagramBase(BaseModel):
    number: int
    name: str
    chinese_name: str
    unicode: str
    judgment: str
    image: str

class HexagramResponse(HexagramBase):
    lines: Optional[Dict[str, str]] = None

class ConsultationRequest(BaseModel):
    question: Optional[str] = None

class LineResult(BaseModel):
    lines: List[int]
    primary_hexagram: HexagramResponse
    changing_hexagram: Optional[HexagramResponse] = None
    changing_lines: Optional[List[int]] = None

class ConsultationResponse(BaseModel):
    question: Optional[str] = None
    result: LineResult

class ErrorResponse(BaseModel):
    detail: str