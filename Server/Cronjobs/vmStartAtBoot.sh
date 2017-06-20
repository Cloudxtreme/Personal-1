#!/bin/bash

logFile='/home/aelchert/Dropbox/Logs/cronLog.txt'

# get list of VMs on the box and put into an array
declare -a getVMsList

getVMsList=( \
e2fe39a5-7bce-49ca-8891-3d61c35bef87 \
021d36a2-e8b8-4594-9b6a-a55033339600 \
2de22143-2b37-48db-b4dd-6237561083d3 \
1d483b74-b0ee-436c-92d0-9a8ff2ff707a \
)

# Loop through VM name array and try to start them. If they are already running
# it will return a 1. If it successfully starts them, it will return 0.

for vm in ${getVMsList[@]}; do
  VBoxManage startvm $vm --type headless 2>&1
  if [[ $? -eq  0 ]]; then
      echo "++ [vmStartScript] - $vm - has started" >> $logFile
  elif [[ $? -eq 1 ]]; then
      echo "-- [vmStartScript] - $vm - is already running" >> $logFile
  else
      echo "-- [vmStartScript] - $vm - Error Occured" >> $logFile
  fi
done
