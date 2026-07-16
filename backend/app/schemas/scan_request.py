from pydantic import BaseModel, Field


class PortScanRequest(BaseModel):
    """Request model for a port scan."""

    target: str
    ports: list[int] = Field(
        default=[80, 443],
        description="Ports to scan"
    )