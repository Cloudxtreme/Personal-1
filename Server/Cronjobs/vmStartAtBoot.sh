#!/bin/bash

logFile='/home/aelchert/Dropbox/Logs/cronLog.txt'

# get list of VMs on the box and put into an array
declare -a getVMsList
getVMsList=($(VBoxManage list vms | cut -d ' ' -f1 | tr -d '"'))

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
