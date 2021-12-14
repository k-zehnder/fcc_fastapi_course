print("CONDA ACTIVATE fcc")

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import cv2

from PIL import Image
import io
import sys
import logging

app = FastAPI()

"""

import wand.image

def validation(filePath, mimetype):
  with wand.image.Image(filename=filePath) as img:
    if img.width != img.height:
      return False
    return True

options = {
  'validation': validation
}
response = Image.upload(CustomAdapter(request), '/public/', options)

"""

def isValidImage(img):
  if img.width > 200:
    return True
  else:
    return False

@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.post("/validate/")
async def validate(file: UploadFile = File(...)): 
  """
  Path operation that takes as input a file and returns its name & type
  """   
  if file.content_type.startswith('image/') is False:
      raise HTTPException(status_code=400, detail=f'File \'{file.filename}\' is not an image.')    

  try:
      contents = await file.read()
      image = Image.open(io.BytesIO(contents)).convert('RGB')
      print(f'image type: {dir(image)}')
      print(f'image width: {image.width}')
      
      # predicted_class = image_classifier.predict(image)
      print(isValidImage(image))
      
      # logging.info(f"Predicted Class: {predicted_class}")
      return {
          "filename": file.filename, 
          "contentype": file.content_type,
          "valid" : isValidImage(image)
      }
  except Exception as error:
      logging.exception(error)
      e = sys.exc_info()[1]
      raise HTTPException(status_code=500, detail=str(e))


