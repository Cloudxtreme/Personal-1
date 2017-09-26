#!/bin/bash

# Run BTRFS system check, returns something like
#[/dev/sdc].write_io_errs   0
#
# grep's for the 0.

sudo /bin/btrfs deviec stats /mnt/NAS/ | grep -vE ' 0$'

# If something is returned, send email

if [$? == 0]; then
  echo "There was a response"
else
  echo "No response"
