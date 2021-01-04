#!/bin/bash 

sudo apt update
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

tests/test_unit.py --cov=application --cov-report term-missing --disable warnings

sudo mkdir /opt/Music-Playlist-App/application
sudo chown -R jenkins /opt/Music-Playlist-App/application

sudo systemctl daemon-reload
sudo systemctl stop music-playlist.service
sudo systemctl start music-playlist.service