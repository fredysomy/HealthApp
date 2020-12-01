#!/bin/bash
sudo pip install -r requirements.txt 
sudo pip install pyqt5-tools
cd setup; sudo python setup.py
cd ..
python healthapp.py
