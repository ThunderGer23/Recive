from typing import Optional
from pydantic import BaseModel

class testFile(BaseModel):
    name: str
    id: Optional[str]