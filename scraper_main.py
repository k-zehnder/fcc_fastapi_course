from scraper_classes.ray_scraper_class import Ray_Scraper
from scraper_classes.scraper_class import Scraper
import time
import ray
import pandas as pd

if __name__ == "__main__":
    # collect image data *without* ray
    start = time.perf_counter()
    scraper = Scraper("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    # for i in range(10):
    img_urls = scraper.load_images_from_folder("/home/batman/Desktop/py/fcc_fastapi_course/test_download")
    # print(scraper.fetch_image_urls("dog", 5, 1))
    default_duration = time.perf_counter() - start
    print(f'NO RAY: {default_duration * 1000:.1f}ms')
    
    # collect image data *with* ray
    ray.init()
    start = time.perf_counter()
    scraper = Ray_Scraper.remote("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    # for i in range(10):
    img_urls = scraper.load_images_from_folder.remote("/home/batman/Desktop/py/fcc_fastapi_course/test_download")
    # print(ray.get(scraper.fetch_image_urls.remote("dog", 5, 1)))
    ray_duration = time.perf_counter() - start
    print(f'WITH RAY: {ray_duration * 1000:.1f}ms')
    ray.shutdown()
    
    
    times = pd.Series([default_duration, ray_duration])
    pct_change = abs(times.pct_change().to_list()[1])
    print(f'RAY is {pct_change}% faster.')