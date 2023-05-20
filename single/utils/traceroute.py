import scapy.all as sca
from scapy.layers.inet import IP, TCP, UDP, ICMP


def get_traceroute(target, local_ip, timeout=30, ttl=10):
    ans = [local_ip]
    a, s = sca.traceroute(target, timeout=timeout, maxttl=ttl)
    temp = []
    for snd,rcv in a:
        temp.append([snd.ttl, rcv.src])
    temp.sort(lambda x: x[0])
    for i in temp:
        ans.append(i[1])
        if i[1] == target:
            break
    return ans
