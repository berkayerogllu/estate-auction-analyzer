from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logging
from app.api.v1.scraper import router as scraper_router

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Estate Auction Analyze App",
    version="0.1.0"
)

app.include_router(scraper_router, prefix="/api/v1/scraper", tags=["Scraper"])

@app.get("/")
async def root():
    return {
        "project": settings.PROJECT_NAME,
        "status": "Online and running!"
    }