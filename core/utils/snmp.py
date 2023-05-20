import os

def snmpwalk(router_ip, community, oid):
    return os.popen('snmpwalk -v 2c -c %s %s %s' % (community, router_ip, oid)).read()

def get_router_interfaces_ip(router_ip, community):
    ans = snmpwalk(router_ip, community, "1.3.6.1.2.1.4.20.1.1")
    ans = ans.split('\n')
    ans = [x.split(' ')[-1] for x in ans if x]
    return ans
