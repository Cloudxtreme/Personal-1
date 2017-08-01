#!/bin/bash

filePath='/home/aelchert/Git/Personal/Scripts/twitterText/'

python $filePath/tweetToText.py
python $filePath/smtp.py
