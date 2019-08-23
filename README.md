# Broccoli-MDM
Broccoli-MDM is an open source master data management tool(MDM).
MDM tools are used to store and define and control common data of an organisation in the one point.

![screenshot](http://storage.googleapis.com/broccoli-mdm-site/images/3.png)

## Supported browsers
1. Chrome
2. Firefox

## Installation for developement

1. Create and activate a virtual environment

virtualenv -p python3.7 .venv
source .venv/bin/activate

2. Install all dependent packages from requirements.txt

pip install -r requirements.txt

3. Set environment variables if you need (OPTIONAL):

	BROCCOLI_SECRET_KEY = random long value (necessary for sessions encoding). MANDATORY FOR PRODUCTION USAGE.
	
	USE_SENTRY = 1 (enable sentry support https://sentry.io - the error tracker)
	
	SENTRY_KEY = your_sentry_key (if you set USE_SENTRY = 1 )

4. Run application

linux: python runserver.py

windows: run_dev_windows.bat

For production execution you have to use "Gunicorn".


## Screenshots
Screenshots are availible on our site
http://brocco.me


## Demo
Demostration is availible here: http://demo.brocco.me.
The demo is located on "Heroku" cloud provider and every 30 minutes of inactivity it idles and a cold run can take over 30 seconds.
Every commit to the master brach redeploys this demo.

Admin access:
admin:123

Regular user with restricted permissions:
test:123

## License
Now Broccoli MDM is under "Doom Source Licence" (https://tldrlegal.com/license/doom-source-licence). It means that you can't earn or get any profit from this software but you can freely use it personaly or for needs of your company.
