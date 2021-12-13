# from ray_classes import *
# from non_ray_classes import *
from ray_scraper_class import Ray_Scraper
from scraper_class import Scraper
import time
import pandas as pd
import ray

if __name__ == "__main__":
    # collect image data *without* ray
    start = time.perf_counter()
    scraper = Scraper("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    for i in range(10):
        scraper.load_images_from_folder("/home/batman/Desktop/py/fcc_fastapi_course/test_download")
    default_duration = time.perf_counter() - start
    print(f'NO RAY: {default_duration * 1000:.1f}ms')
    
    # collect image data *with* ray
    ray.init()
    start = time.perf_counter()
    scraper = Ray_Scraper.remote("/home/batman/Desktop/explore_ray/chromedriver", headless=True)
    for i in range(10):
        scraper.load_images_from_folder.remote("/home/batman/Desktop/py/fcc_fastapi_course/test_download")
    ray_duration = time.perf_counter() - start
    print(f'WITH RAY: {ray_duration * 1000:.1f}ms')
    ray.shutdown()
    
    
    times = pd.Series([default_duration, ray_duration])
    pct_change = abs(times.pct_change().to_list()[1])
    print(f'RAY is {pct_change}% faster.')

    # setup "analyzers"
    sim_analyzer = SimilarityAnalyzer()
    bw_analyzer= BlackWhiteThresholdAnalyzer()

    # results = ray.get(scraper.get_images.remote())
    # print(len(results))

    # img_urls = scraper.fetch_image_urls("cat", 5, 1)
    # TODO: scraper.persist_images(image_urls)
    
    # validate images
    """
    results = {}
    for analyzer in [sim, bw]:
        for path in image_paths:
            image = cv2.imread(path)
            bool_result = analyzer.isValidImage(image)
            results[(analyzer, path)] = boolResult
    return results
    """