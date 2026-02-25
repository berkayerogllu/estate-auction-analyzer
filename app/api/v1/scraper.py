from fastapi import APIRouter
from app.services.scraper_service import ScraperService

router = APIRouter()

@router.get("/run-edevlet")
async def run_scraper():
    data = await ScraperService.scrape_edevlet()
    return {"count": len(data), "items": data}