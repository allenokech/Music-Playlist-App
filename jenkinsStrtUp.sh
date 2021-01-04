#!/bin/bash

sudo apt-get update
sudo apt-get install python3 -y
sudo apt-get install python3-venv -y
sudo apt-get install python3-pip -y

python3 -m venv venv

source venv/bin/activate
pip install -r requirements.txt
python3 app.py