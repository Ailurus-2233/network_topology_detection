from pydantic import BaseModel
from typing import Optional

class Capture(BaseModel):
    iface: str
    count: int
    timeout: int
    filter: Optional[str] = None