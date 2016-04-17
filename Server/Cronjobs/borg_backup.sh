#!/bin/sh
REPOSITORY="/mnt/Backups"

# Backup all of /home and /var/www except a few
# excluded directories
borg create -v --stats                          \
    $REPOSITORY::`hostname`-`date +%Y-%m-%d`    \
    /mnt/NAS                                                                         \


# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. --prefix `hostname`- is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.
borg prune -v $REPOSITORY --prefix `hostname`- \
    --keep-daily=7 --keep-weekly=4 --keep-monthly=6
