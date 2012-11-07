#!/bin/sh
INSTALL_DIR=/usr/local/ping_alert
mkdir -p $INSTALL_DIR
cp ping.py $INSTALL_DIR
cp ping_alert.py $INSTALL_DIR
cp run_alarms.sh $INSTALL_DIR
chmod +x $INSTALL_DIR/ping_alert.py
chmod +x $INSTALL_DIR/run_alarms.sh
echo
echo--------------
echo "Please ensure that the command notify-send is installed on your machine"
echo--------------
echo
echo "You might now wish to run 'crontab -e' as a non-root user to setup cron to routinely run your alarm script" 
echo "Here's a sample:"
echo
cat sample_crontab_e
