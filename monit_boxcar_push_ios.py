#!/usr/bin/python

import urllib
import urllib2
import sys
import syslog
import os

ACCESS_KEY = ""
BOXURL = "https://new.boxcar.io/api/notifications/"
TAG = 'Monitoring'

ARGUMENTS = sys.argv
if len(ARGUMENTS) != 4:
	print "ERROR: Wrong Arguments usage. Use boxcar_client.py <fail/recovery> <servername> <servicename>."
	syslog.syslog("BOXCAR_MONIT: ERROR: Wrong Arguments usage. Use boxcar_client.py <fail/recovery> <servername> <servicename>.")
	sys.exit(1)

def boxcar_push(t, m):
	TITLE = t
	MESSAGE = m
	opener = urllib2.build_opener(urllib2.HTTPHandler())
	data = urllib.urlencode({'user_credentials' : ACCESS_KEY,
                         'notification[title]'  : TITLE,
                         'notification[long_message]' : MESSAGE,
                         'notification[sound]' : 'bird-1',
                         'notification[source_name]' : TAG})
	content = opener.open(BOXURL, data=data).read()

def boxcar_fail(s, p):
	SERVER = s
	SERVICE = p
	TITLE = SERVER + " " + SERVICE + " ausgefallen"
	MESSAGE = "<p><b>" + SERVICE + " auf " + SERVER + " ausgefallen</b></p><p>Service " + SERVICE + " ausgefallen.</p>"
	if os.path.isfile("/tmp/" + SERVER + "_" + SERVICE):
		syslog.syslog("BOXCAR_MONIT: " + SERVER + " " + SERVICE + " still down.")
		sys.exit(1)
	else:
		tempfile = open("/tmp/" + SERVER + "_" + SERVICE, "w")
		tempfile.close()
		boxcar_push(TITLE, MESSAGE)

def boxcar_recovery(s, p):
	SERVER = s
	SERVICE = p
	TITLE = SERVER + " " + SERVICE + " ist wieder up"
	MESSAGE = "<p><b>" + SERVICE + " auf " + SERVER + " ist wieder up</b></p><p>Service " + SERVICE + " ist wieder up.</p>"
	os.remove("/tmp/" + SERVER + "_" + SERVICE)
	boxcar_push(TITLE, MESSAGE)


if ARGUMENTS[1] == 'fail':
	boxcar_fail(ARGUMENTS[2], ARGUMENTS[3])
elif ARGUMENTS[1] == 'recovery':
	boxcar_recovery(ARGUMENTS[2], ARGUMENTS[3])
else:
	syslog.syslog("BOXCAR_MONIT: ERROR: First argument is not fail or recovery.")
	sys.exit(1)