#!/bin/bash

# Variables
REPO_DIR="/path/to/your/repository"
IMAGE_NAME="cv-analyser"
CONTAINER_NAME="cv-analyser-container"
HOST_PORT=8080
CONTAINER_PORT=80
LOG_FILE="/path/to/your/logfile.log"

# Pull the latest changes from the GitHub repository
cd $REPO_DIR
git pull &>> $LOG_FILE

# Build the Docker image
docker build -t $IMAGE_NAME . &>> $LOG_FILE

# Stop the existing container (if running)
docker stop $CONTAINER_NAME &>> $LOG_FILE || true
docker rm $CONTAINER_NAME &>> $LOG_FILE || true

# Run a new container with the updated image
docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME &>> $LOG_FILE
