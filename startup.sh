#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo mkdir /opt/music_playlist_db
sudo chown -R jenkins /opt/music_playlist_db
sudo systemctl daemon-reload
sudo systemctl stop music-playlist.service
sudo systemctl start music-playlist.service