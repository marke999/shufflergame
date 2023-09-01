#!/bin/bash

local_IP="$(hostname -I | awk '{print $1}')"

#Iterate through each file in the folder
cd /shuffler_app/templates
for file in *; do
    if [ -f "$file" ]; then
       #Replace the IP address in the file with the value of local_IP
       sed -i "s#//192.168.1.10:#g" "$file"
    fi
done
