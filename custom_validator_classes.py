import os
import time
import datetime
import cv2
from abc import ABC, abstractmethod
from tqdm import tqdm

class ImageValidator(ABC):
    @abstractmethod
    def isValidImage(self):
        pass

class SimilarityAnalyzer(ImageValidator):
    def isValidImage(self):
        pass
    
class BlackWhiteThresholdAnalyzer(ImageValidator):
    def isValidImage(self):
        pass
    
if __name__ == "__main__":
    from froala_flask_example_full import *
    import requests

    filePath = "dog1.png"
    img = cv2.imread(filePath)
    print(img)
    
    def validation(filePath, mimetype):
        with wand.image.Image(filename=filePath) as img:
            if img.width != img.height:
                return False
        return True

    options = {
    'validation': validation
    }
    

    # assign server url and image path to variables
    url = "http://127.0.0.1:8000/analyze"
    filename = "/home/batman/Desktop/py/fcc_fastapi_course/dog1.png"
    # image_test = cv2.imread(filename)
    
    r = requests.post(url, files={"file": ("filename", open(filename, "rb"), "image/jpeg")})

    
    # files = {'media': open(image_test, 'rb')}
    # print(requests.post(url, files=files))

    # get response from server after posting image
    # r = requests.post(url, files={"file": ("filename", open(filename, "rb"), "image/jpeg")})
    # print(r)
    
    # response = Image.upload(FlaskAdapter(request), '/public/', options)
    # print(response)
