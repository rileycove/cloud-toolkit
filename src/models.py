from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DataRecord(BaseModel):
    id: int
    source: str
    payload: dict
    created_at: datetime = datetime.now()