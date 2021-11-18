#!/bin/bash

while true
do
  python3 /root/coins/updateprices.py
  now=$(date +"%T")
  echo "Updating Prices ====> : $now"
 sleep 5
done