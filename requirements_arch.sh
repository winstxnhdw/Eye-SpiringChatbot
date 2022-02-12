#!/bin/bash

sudo pacman -Syu nodejs npm yarn
sudo pacman -Syu docker
systemctl start docker.service
systemctl nable docker.service
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
exit