import ray
import os
import cv2
from abc import ABC, abstractmethod

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
import requests


@ray.remote 
class Ray_Scraper:
    def __init__(self, chrome_driver_path, headless=True):
        self.chrome_driver_path = chrome_driver_path
        self.ser = Service(self.chrome_driver_path)
        self.op = webdriver.ChromeOptions()
        self.op.add_argument("--headless") if headless == True else None
        self.wd = webdriver.Chrome(service=self.ser, options=self.op)
        self.images_folder = "/home/batman/Desktop/explore_ray/images"
        self.images_arrays = []
        
    
    def load_images_from_folder(self):
        images = []
        for filename in os.listdir(self.images_folder):
            img = cv2.imread(os.path.join(self.images_folder,filename))
            if img is not None:
                images.append(img)
                self.images_arrays.append(img)
        return images
    
    def get_images(self):
        return self.images_arrays
    
    def fetch_image_urls(self, query:str, max_links_to_fetch:int,sleep_between_interactions:int=1):
        # build the google query
        search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

        # load the page
        self.wd.get(search_url.format(q=query))

        image_urls = set()
        image_count = 0
        results_start = 0
        while image_count < max_links_to_fetch:
            thumbnail_results = self.wd.find_elements_by_css_selector("img.Q4LuWd")
            number_results = len(thumbnail_results)


            for img in thumbnail_results[results_start:number_results]:
                # try to click every thumbnail such that we can get the real image behind it
                try:
                    img.click()
                    time.sleep(sleep_between_interactions)
                except Exception:
                    continue

            #     # extract image urls    
                actual_images = self.wd.find_elements_by_css_selector('img.n3VNCb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))

                image_count = len(image_urls)
                print(f'image count: {image_count}')
                if len(image_urls) >= max_links_to_fetch:
                    print(f"Found: {len(image_urls)} image links, done!")
                    break
                else:
                    print("Found:", len(image_urls), "image links, looking for more ...")
                # time.sleep(30)
            #     #return
                load_more_button = self.wd.find_element_by_css_selector(".mye4qd")
                if load_more_button:
                    self.wd.execute_script("document.querySelector('.mye4qd').click();")

                # move the result startpoint further down
                results_start = len(thumbnail_results)

        return image_urls