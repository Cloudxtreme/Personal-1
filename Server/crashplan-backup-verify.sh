#awk 'END {print Date: Time: ,}' crashplan_backup.txt
awk 'END {print "Date: ",$2," ","Time: ",$3}' ~/Dropbox/Logs/crashplan_backup.txt
