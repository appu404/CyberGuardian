from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["System"])
async def root():
    """Root endpoint."""
    return {
        "project": "CyberGuardian",
        "version": "0.1.0",
        "status": "running",
    }


@router.get("/health", tags=["System"])
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
    }