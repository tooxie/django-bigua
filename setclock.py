#!/usr/bin/python
from socket import *
import struct,os,time,sys

# Script to set Linux hardware clock (/usr/sbin/hwclock) from an NTP
# time server.   Run as "setclock.py" to simply print the time from
# the NTP server.  Run as "setclock.py --set" to set the Linux
# hardware clock (as the super user, of course).

# Based on Simon Foster's simple SNTP client from ASPN Python cookbook.
# Adapted by Paul Rubin; this script lives at:
#    http://www.nightsong.com/phr/python/setclock.py

time_server = ('0.us.pool.ntp.org', 123)
# time.apple.com is a stratum 2 time server.  (123 is the SNTP port number).
# More servers info can be found at
#
#   http://www.eecis.udel.edu/~mills/ntp/servers.htm
#
# Note it's considered antisocial to use a stratum 1 server (like NIST)
# for purposes like this which don't need extreme accuracy (i.e. syncing
# your own big NTP network).  See www.ntp.org for more info.
#
# You could also use time.windows.com (Microsoft server) which syncs
# all Windows XP machines everywhere, so it can presumably handle lots
# of clients.

# number of seconds between NTP epoch (1900) and Unix epoch (1970).
TIME1970 = 2208988800L      # Thanks to F.Lundh

client = socket( AF_INET, SOCK_DGRAM )
data = '\x1b' + 47 * '\0'
client.sendto(data, time_server)
data, address = client.recvfrom( 1024 )
if data:
    print 'Response received from', address,'\n'
    t = struct.unpack( '!12I', data )[10]
    if t == 0:
        raise 'invalid response'
    ct = time.ctime(t - TIME1970)
    print 'Current time = %s\n' % ct
    if len(sys.argv) > 1 and sys.argv[1] == "--set":
        os.system("/usr/sbin/hwclock --set '--date=%s'"% ct)
else:
    raise 'no data returned'
