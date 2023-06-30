#!/bin/bash

#Activate virtual environment
cd myenv/bin/activate

#Activate Django server
python3 ~/Tasks/Python3/shuffler/manage.py runserver 0.0.0.0:8200 > ~/Tasks/Python3/shuffler/shuffler_log.txt
