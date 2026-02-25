from playwright.async_api import async_playwright
from app.core.config import settings
from app.core.logger import logger
from app.schemas.estate import EstateListing

class ScraperService:
    @staticmethod
    async def scrape_edevlet():
        results = []
        async with async_playwright() as p:
            # headless=True olduğu için tarayıcı arka planda görünmez çalışır
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            for sf in range(0, settings.EDEVLET_MAX_SF + 1, settings.EDEVLET_PAGE_STEP):
                url = f"{settings.EDEVLET_BASE_URL}?sf={sf}"
                logger.info(f"Starting...: {url}")

                try:
                    await page.goto(url, wait_until="networkidle")
                
                    rows = await page.query_selector_all("table.resultTable tbody tr")

                    for row in rows:
                        cols = await row.query_selector_all("td")
                  
                        if len(cols) >= 9:
                            link_element = await cols[8].query_selector("a")
                            detail_path = await link_element.get_attribute("href") if link_element else ""
                            
                            item = EstateListing(
                                category=await cols[0].inner_text(),
                                status=await cols[2].inner_text(),
                                city=await cols[3].inner_text(),
                                district=await cols[4].inner_text(),
                                neighborhood=await cols[5].inner_text(),
                                area=await cols[6].inner_text(),
                                price=await cols[7].inner_text(),
                                detail_url=f"https://www.turkiye.gov.tr{detail_path}"
                            )
                            results.append(item)
                    
                    logger.success(f"Page sf={sf} is completed. Total data: {len(results)}")
                    
                except Exception as e:
                    logger.error(f"Page sf={sf} error while checking: {str(e)}")
                    continue

            await browser.close()
            return results