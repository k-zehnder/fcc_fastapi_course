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
    
    """    
    files = {'media': open('/home/batman/Desktop/py/automate_boring_stuff/froala/public/32cb3ffbf0e4a9a8c24e2472b9bf46440b20dc0f.png', 'rb')}
    print(requests.post(test_url, files=files))
    """
    
    response = Image.upload(FlaskAdapter(request), '/public/', options)
    print(response)
