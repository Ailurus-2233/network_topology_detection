import scapy.all as sca
from scapy.layers.inet import IP, TCP, UDP, ICMP

def get_traceroute(target, timeout=30, ttl=30):
    ans = []
    a, s = sca.traceroute(target, timeout=timeout, maxttl=ttl)
    for i in range(len(a)):
        ans.append(a[i][1].src)
        if a[i][1].src == target:
            break
    return ans