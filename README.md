# monit_boxcar_push_ios.py
Small Python Script that pushes Monit monitoring alarms to iOS via Boxcar.

Just put your Boxcar API Key to the ACCESS_KEY Variable.<br>
In Monit configuration exec the Script with Arguments <fail/recovery> <servername> <service>. Use fail for failed Services and recovery for recovering a Service.<br>
Optional can you modify the TAG variable to put the Boxcar Tag you want in.<br>

Example:<br>
/usr/sbin/monit_boxcar_push_ios.py fail webserver ssl<br>
/usr/sbin/monit_boxcar_push_ios.py recovery webserver ssl<br>

Example Monit config:<br>
<code>
check host webserver with address www.mywebserver.com
	if failed ping
		then exec "/usr/sbin/boxcar_client.py fail google ping" 
	else if succeeded
		then exec "/usr/sbin/boxcar_client.py recovery google ping"
</code>
