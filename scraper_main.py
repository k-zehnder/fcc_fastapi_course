from ray_scraper_class import Ray_Scraper
from scraper_class import Scraper


if __name__ == "__main__":
    chrome_driver_path = "/home/batman/Desktop/py/fcc_fastapi_course/chromedriver"
    so = Scraper(chrome_driver_path, headless=True)
    ro = Ray_Scraper.remote(chrome_driver_path, headless=True)