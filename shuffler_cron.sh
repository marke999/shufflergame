#!/bin/bash

#Activate virtual environment
cd ~/Tasks/Python3/shufflergame
source myenv/bin/activate

#Activate Django server
python3 ~/Tasks/Python3/shufflergame/manage.py runserver 0.0.0.0:8200 > ~/Tasks/Python3/shufflergame/shuffler_log.txt
