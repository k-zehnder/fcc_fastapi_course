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
    pass
