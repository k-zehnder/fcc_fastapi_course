print("CONDA ACTIVATE fcc")

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn

from PIL import Image
import io
import sys
import logging

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello world"}

@app.post("/predict/")
async def predict(file: bytes = File(...)):
    if file.content_type.startswith('image/') is False:
        raise HTTPException(status_code=400, detail=f'File \'{file.filename}\' is not an image.')    

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')

        # predicted_class = image_classifier.predict(image)
        
        # logging.info(f"Predicted Class: {predicted_class}")
        return {
            "filename": file.filename, 
            "contentype": file.content_type
        }
    except Exception as error:
        logging.exception(error)
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/analyze")
async def analyse(file: bytes = File(...)):
    image = Image.open(io.BytesIO(file)).convert("RGB")
    # # stats = process_image(image)
    return {"type" : type(image)}
