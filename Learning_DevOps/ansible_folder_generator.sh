#! /bin/bash

# Run in a new folder for an ansible project
# version .1

echo -e "
#########################################################
Creates recommended folder structure for ansible configs
#########################################################
"

rc="roles/common"

# make hosts file
touch hosts

 # here we assign variables to particular groups
mkdir group_vars

# # if systems need specific variables, put them here
mkdir host_vars

# master playbook
touch site.yml

#playbook for webserver tier
touch webservers.yml

#playbook for dbserver tier
touch dbservers.yml

mkdir roles
mkdir $rc #this hierachy represents a "role"

mkdir $rc/tasks
touch $rc/tasks/main.yml #tasks file can include smaller files if warranted

mkdir $rc/handlers
touch $rc/handlers/main.yml

mkdir $rc/templates
touch $rc/templates/ntp.conf.j2 #tempaltes end in .j2

mkdir $rc/vars #vars associated with this role
touch $rc/vars/main.yml

mkdir roles/webtier #same kidn of structure as "common" was above, but for specific web role
mkdir roles/monitoring
mkdir roles/food

echo "[done]"
