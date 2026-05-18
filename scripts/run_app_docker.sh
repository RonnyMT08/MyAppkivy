#!/bin/bash 

xhost +local:docker

#construct the docker image
docker build -t kivy-app .

# run the docker container
docker run -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --name myapp_container \
  kivy-app

# access the container and run the app
docker exec -it myapp_container bash

# inside the container, run the app
python main.py

#
