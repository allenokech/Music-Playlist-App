#!/bin/bash
cd /opt/Music-Playlist-App
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py