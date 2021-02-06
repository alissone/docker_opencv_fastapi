"""
Sample app using cv2 and FastAPI
"""

# import uuid
import io
import cv2
from fastapi import File, FastAPI, UploadFile
import numpy as np
from PIL import Image
from starlette.responses import StreamingResponse


app = FastAPI()


@app.get("/")
def read_root():
    """Main page, still empty"""
    return {"info": "Send a POST request with an image to /grayscale"}


@app.post("/grayscale")
def get_image(file: UploadFile = File(...)):
    """Returns a grayscale version of the image uploaded"""

    image = np.array(Image.open(file.file))
    # name = f"/storage/{str(uuid.uuid4())}.jpg"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, im_png = cv2.imencode(".png", gray)
    return StreamingResponse(
        io.BytesIO(im_png.tobytes()),
        media_type="image/png",
        )
