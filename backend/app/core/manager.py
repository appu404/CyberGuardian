from app.core.scanner import BaseScanner
from app.schemas.scan_result import ScanResult


class ScanManager:
    """Responsible for executing scanners."""

    async def run(self, scanner: BaseScanner) -> ScanResult:
        return await scanner.scan()