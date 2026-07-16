from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from app.schemas.enums import ScanStatus


class ScanResult(BaseModel):
    """Standard response returned by all scanners."""

    scanner: str
    target: str
    status: ScanStatus = ScanStatus.PENDING

    started_at: datetime = Field(default_factory=datetime.utcnow)
    finished_at: datetime | None = None

    results: dict[str, Any] = Field(default_factory=dict)

    error: str | None = None