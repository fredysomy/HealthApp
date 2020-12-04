#!/bin/bash
sudo pip install pandas
sudo pip install -r requirements.txt
cd setup; sudo python setup.py
cd ..
python healthapp.py
