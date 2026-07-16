from abc import ABC, abstractmethod

from app.schemas.scan_result import ScanResult


class BaseScanner(ABC):
    """Base class for all scanners."""

    def __init__(self, target: str):
        self.target = target

    @abstractmethod
    async def scan(self) -> ScanResult:
        """Execute the scan."""
        raise NotImplementedError