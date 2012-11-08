#!/usr/bin/env python
#-----------------------
#Script to Help Monitor specified Host, raise dbus notifications when down or unreachable
#-----------------------
#Author : Nemesis Fixx (joewillrich [at] gmail [dot] com)
#History:
#--------
#7th Nov, 2012 : Nemesis Fixx, Version 1.0
#-----------------------

from ping import Ping
import sys
from subprocess import call
from optparse import OptionParser

class PingAlarm(Ping):
    """
    Ping and Raise alarm if host is down or unresolvable
    """
    verbose_hostname = "HOST"
    duration = 1000
    action_down = None
    action_dns = None
    def __init__(self, *args, **kwargs):
        self.verbose_hostname = kwargs.pop('name',self.verbose_hostname)
        self.action_down = kwargs.pop('action_down',None)
        self.action_dns = kwargs.pop('action_dns',None)
        self.duration = int(kwargs.pop('duration',self.duration))

        super(PingAlarm, self).__init__(*args, **kwargs)

    def print_start(self):
        pass

    def print_unknown_host(self, e):
        self.raise_alarm("DNS FAILURE","%s(%s) is UNRESOLVABLE!" % (self.verbose_hostname,self.destination),self.action_dns)

    def print_success(self, delay, ip, packet_size, ip_header, icmp_header):
        self.success_call_count += 1

    def print_failed(self):
        self.raise_alarm("HOST is DOWN!","%s(%s) is DOWN!" % (self.verbose_hostname,self.destination),self.action_down)

    def print_exit(self):
        pass

    def raise_alarm(self,header,msg,action):
        call(["notify-send", "-i","error", "-t","%d" % self.duration, "-u","critical", header, msg + ("\n****** ACTION ******\n%s" % action if action else "") ])



usage = "usage: %prog TARGET [options] "
parser = OptionParser(usage)
parser.add_option("-d", "--alarm-duration", dest="duration", help="How long (millisecs) should alarm run", metavar="DURATION", default=1000)
parser.add_option("-v", "--verbose-name", dest="verbose_name", help="Verbose name of Host", metavar="VERBOSE_NAME", default="Target")
parser.add_option("-x", "--alarm-host-down", dest="alarm_down", help="Message to Display when Host is Down", metavar="DOWN_ALARM", default=None)
parser.add_option("-z", "--alarm-dns-error", dest="alarm_dns", help="Message to Display when Host can't be resolved", metavar="DNS_ALARM", default=None)

(options, args) = parser.parse_args()

if __name__ == '__main__':
    if len(args) == 1:
        PingAlarm(args[0],
                duration=options.duration,
                name=options.verbose_name,
                action_down=options.alarm_down,
                action_dns=options.alarm_dns
                )
    else:
        parser.print_help()
