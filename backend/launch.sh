#!/bin/bash

# Clear the port before beginning
sh ./clearport.sh

# Delete previous Docker image if any
docker stop chatbot-server
docker rm chatbot-server

# Build Docker image
docker build -t chatbot-server .

# Run Docker image
docker run --name chatbot-server chatbot-server