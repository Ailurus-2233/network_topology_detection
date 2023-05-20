from pydantic import BaseModel
from typing import Optional


class Traceroute(BaseModel):
    host: str
    timeout: int
    maxttl: int
