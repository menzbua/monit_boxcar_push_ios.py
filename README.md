# monit_boxcar_push_ios.py
Small Python Script that pushes Monit monitoring alarms to iOS via Boxcar.

Just put your Boxcar API Key to the APIKEY Variable.
In Monit configuration exec the Script with Arguments <fail/recovery> <servername> <service>. Use fail for failed Services and recovery for recovering a Service.

Example:
/usr/sbin/monit_boxcar_push_ios.py fail webserver ssl
/usr/sbin/monit_boxcar_push_ios.py recovery webserver ssl

Example Monit config:
check host webserver with address www.mywebserver.com
	if failed ping
		then exec "/usr/sbin/boxcar_client.py fail google ping" 
	else if succeeded
		then exec "/usr/sbin/boxcar_client.py recovery google ping"
