# docker_opencv_fastapi

This is a template to use opencv and fastapi with the official python docker image

### How to use
Just execute `docker-compose up --build` to run it. Browse to `localhost:5000/docs` to view available requests.

As an example, you can POST any image to `/grayscale` to receive another image as response, containing a grayscale version of whatever you sent.
