#!/bin/sh
sudo apt install python3-dev libpq-dev python3-pip -y
pip install -r requirements.txt
python3 manage.py migrate

