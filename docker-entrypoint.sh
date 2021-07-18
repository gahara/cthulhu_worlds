#!/bin/sh
#sleep 25

#flask db migrate -m "entries table"
#flask db upgrade
exec gunicorn -b :5000 server:app