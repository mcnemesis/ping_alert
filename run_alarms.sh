#!/usr/bin/sh

#This should ideally be run within a cron context so that we periodically check the state of our machines...

ALARM_SCRIPT='/usr/local/ping_alert/ping_alert.py'
PAUSE=5 #seconds
ALARM_DURATION=5000 #miliseconds

#Note: am deliberately using the local network hostnames of the machines, so that even dns resolution
#failures can be reported (since the hostnames can't resolve outside of the local network)

$ALARM_SCRIPT  entandikwa -v "DS Main Server" -d $ALARM_DURATION -x "Please Check that the Server is ON" -z "Please Check/Report status of Internet Connectivity"

sleep $PAUSE

$ALARM_SCRIPT  victor -v "Server Victor" -d $ALARM_DURATION -x "Please Check that the Server is ON" -z "Please Check/Report status of Internet Connectivity"


sleep $PAUSE

$ALARM_SCRIPT  scar -v "Server Scar" -d $ALARM_DURATION -x "Please Check that the Server is ON" -z "Please Check/Report status of Internet Connectivity"
