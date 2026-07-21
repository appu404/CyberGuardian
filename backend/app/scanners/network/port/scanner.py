from .services import PORT_SERVICES
import socket
from datetime import datetime

from app.core.scanner import BaseScanner
from app.schemas.enums import ScanStatus
from app.schemas.scan_result import ScanResult

from .constants import DEFAULT_TIMEOUT


class PortScanner(BaseScanner):
    """TCP Port Scanner."""

    def __init__(self, target: str, ports: list[int]):
        super().__init__(target)
        self.ports = ports

    def _scan_port(self, port: int) -> bool:
        """Check whether a TCP port is open."""

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(DEFAULT_TIMEOUT)

        try:
            return sock.connect_ex((self.target, port)) == 0
        finally:
            sock.close()

    async def scan(self) -> ScanResult:
        """Scan the configured ports."""

        result = ScanResult(
            scanner="Port Scanner",
            target=self.target,
            status=ScanStatus.RUNNING,
        )

        open_ports = []

        for port in self.ports:
            if self._scan_port(port):
                open_ports.append(
                    {
                        "port": port,
                        "service": PORT_SERVICES.get(port, "Unknown"),
                    }
                )

        result.status = ScanStatus.COMPLETED
        result.finished_at = datetime.utcnow()
        result.results = {
            "ports_scanned": len(self.ports),
            "open_port_count": len(open_ports),
            "open_ports": open_ports,
        }

        return result