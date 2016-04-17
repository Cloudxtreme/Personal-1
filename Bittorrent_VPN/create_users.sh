#! /bin/bash

USER="adamschoonover"
PWD="adamschoonover"

sudo useradd $USER -m -s /bin/bash

sudo adduser $USER root

# add password
echo -e "$PWD\n$PWD\n" | passwd

# add to sudoers
echo "$USER ALL=(ALL:ALL) ALL" >> /etc/sudeoers
