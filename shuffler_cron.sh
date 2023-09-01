#!/bin/bash

#Activate virtual environment
cd ~/Tasks/Python3/shufflergame
source myenv/bin/activate

#Activate the local_ip script
sh local_ip.sh

#Activate Django server
python3 ~/Tasks/Python3/shufflergame/manage.py runserver 0.0.0.0:8200 > ~/Tasks/Python3/shufflergame/shuffler_log.txt
