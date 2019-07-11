#get changes and reload server
pkill flask
nohup flask run --reload --with-threads --port 80 -h 0.0.0.0 2>&1 &
exit o
