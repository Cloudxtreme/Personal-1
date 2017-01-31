# compare files
cd $nginxTempDIR
for x in $(find . "*.conf" -type f); do
	if [[$(cmp --silent $nginxTempDIR/x $nginxBackupDIR/x]) != 0]]; then
		mv $nginxTempDIR/x $nginxBackupDIR
	else:
		exit 0
	fi
done

if [[ $nginxCFG != $nginxBACKUP ]]; then
	cp /etc/nginx/conf.d/*.conf $DIR/Nginx
	cp /etc/nginx/nginx.conf $DIR/Nginx
    	printf "\n Updated Nginx conf - $NOW" >> $logFile
    	counter+=1
fi
