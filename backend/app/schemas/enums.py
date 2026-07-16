from enum import Enum


class ScanStatus(str, Enum):
    """Possible states of a scan."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"