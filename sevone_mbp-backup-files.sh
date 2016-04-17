#! /bin/bash

ua='/Users/adamschoonover'
NOW=$(date +"%m-%d-%Y")

# bash profile
cp $ua/.bash_profile $ua/bash_profile/bash_profile

# copy ssh
cp $ua/.ssh/* $ua/ssh/

cd $ua/Git/Post-install-scripts/

git add -A .
git commit -m "update $NOW"
git push origin master
