#!/usr/bin/env bash
set -euo pipefail

APP_NAME="myapp_container"
IMAGE_NAME="kivy-app"
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Clean up any previous container with the same name
docker rm -f "$APP_NAME" >/dev/null 2>&1 || true

# Authorize local Docker containers to connect to the X server
xhost +local:docker >/dev/null 2>&1 || true

# Build the Docker image
docker build -t "$IMAGE_NAME" "$PROJECT_DIR"

# Run the container mounting the current project
docker run -it \
  --name "$APP_NAME" \
  -e DISPLAY=${DISPLAY:-:0} \
  -v "$PROJECT_DIR":/app \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  "$IMAGE_NAME" \
  bash

# Para detener 'crl+c'
# Para correr container 'docker start myapp_container' 
# Para entrar en exec 'docker exec -it myapp_conteiner bash'
# Levantar app 'python main.py'