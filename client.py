from archive.froala_flask_example_full import *
import requests


if __name__ == "__main__":
    # assign api_endpoint route to variable
    api_endpoint = "http://127.0.0.1:8000/validate"

    # post to route the filename not the actual imaage
    filename = "/home/batman/Desktop/py/fcc_fastapi_course/dog1.png"
    
    # send POST request to server from client
    r = requests.post(api_endpoint, files={"file": ("filename", open(filename, "rb"), "image/jpeg")})
    print(f'response code from server: {r}')
    print(f'response content: {r.content}')