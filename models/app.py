from typing import Optional
from pydantic import BaseModel

class testFile(BaseModel):
    id: Optional[list]
    name: str