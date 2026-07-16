from app.core.scanner import BaseScanner
from app.schemas.scan_result import ScanResult


class ScanManager:
    """Responsible for executing scanners."""

    async def run(self, scanner: BaseScanner) -> ScanResult:
        """
        Execute a scanner and return its result.
        """
        return await scanner.scan()