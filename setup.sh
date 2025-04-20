#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip -y
pip3 install virtualenv

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

python3 run.py
