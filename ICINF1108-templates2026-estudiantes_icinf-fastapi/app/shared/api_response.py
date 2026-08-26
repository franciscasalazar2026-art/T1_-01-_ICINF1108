from typing import Generic, TypeVar, Optional
from pydantic import BaseModel, Field
from datetime import datetime, timezone


T = TypeVar('T')

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())