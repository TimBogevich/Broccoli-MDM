# Broccoli-MDM
Broccoli-MDM is an open source master data management tool(MDM).
MDM tools are used to store and define and control common data of organisation in one point.

#Installation for developement

1. Create and activate a virtual environment
virtualenv -p python3.7 .venv
source .venv/bin/activate

2. Install all dependent packages from requirements.txt
pip install -r requirements.txt

3. Run application
linux: python runserver.py
windows: run_dev_windows.bat

For production execution you have to use gunicorn.
