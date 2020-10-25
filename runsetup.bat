@echo on
set name=%1
set pass=%2
echo user: '%name%'>db.yaml
echo password: '%pass%'>>db.yaml
pip install -r requirements.txt 
pip install pyqt5-tools
setup\setup.py
healthapp.py
