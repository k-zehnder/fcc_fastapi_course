from ray_scraper_class import Ray_Scraper
from scraper_class import Scraper
import time
import ray

if __name__ == "__main__":
    
    ###############################################
    chrome_driver_path = "/home/batman/Desktop/py/fcc_fastapi_course/chromedriver"
    so = Scraper(chrome_driver_path, headless=True)
    ro = Ray_Scraper.remote(chrome_driver_path, headless=True)
    
    # *************** WITHOUT RAY ***************
    start = time.perf_counter()
    scraper = Scraper("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    output_folder = "/home/batman/Desktop/py/fcc_fastapi_course/test_download"
    
    # scrape urls into a list and return them
    scraped_urls = scraper.fetch_image_urls("cat", 5, 1)
    # for scraped_url in scraped_urls:
    #     scraper.download(scraped_url, output_folder)
    default_duration = time.perf_counter() - start
    print(f'NO RAY: {default_duration * 1000:.1f}ms')
    print(f'scraped urls: {scraped_urls}')
    
            
    # *************** WITH RAY ***************
    start = time.perf_counter()
    scraper = Ray_Scraper.remote("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    output_folder = "/home/batman/Desktop/py/fcc_fastapi_course/test_download"
    
    # scrape urls into a list and return them
    palettes = []
    scraped_urls = palettes.append(scraper.fetch_image_urls.remote("cat", 5, 1))
    scraped_urls = ray.get(palettes)
    print(f'scraped urls: {scraped_urls}')

    # for scraped_url in ray.get(scraped_urls):
    #     ray.get(scraper.download.remote(scraped_url, output_folder, verbose=False))
    
    ray_duration = time.perf_counter() - start
    print(f'RAY: {ray_duration * 1000:.1f}ms')
    print(f'scraped urls: {scraped_urls}')
        