#!/bin/bash 

sudo apt update
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-venv

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

pytest --cov=application tests/test_unit.py --cov-report term-missing --disable-warnings