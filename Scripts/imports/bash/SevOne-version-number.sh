#! /bin/bash

# Use this to pull the version numbers

base=$(cat /SevOne.info | awk '/base/{print $3}');
major=$(cat /SevOne.info | awk '/major/{print $3}');
minor=$(cat /SevOne.info | awk '/minor/{print $3}');
patch=$(cat /SevOne.info | awk '/patch/{print $3}');
