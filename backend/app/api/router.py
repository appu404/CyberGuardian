from fastapi import APIRouter

from app.core.manager import ScanManager
from app.schemas.scan_request import PortScanRequest
from app.scanners.network.port.scanner import PortScanner

router = APIRouter()

manager = ScanManager()


@router.get("/", tags=["System"])
async def root():
    return {
        "project": "CyberGuardian",
        "version": "0.1.0",
        "status": "running",
    }


@router.get("/health", tags=["System"])
async def health():
    return {
        "status": "healthy",
    }


@router.post("/scan/ports", tags=["Network"])
async def scan_ports(request: PortScanRequest):
    scanner = PortScanner(
        target=request.target,
        ports=request.ports,
    )

    return await manager.run(scanner)