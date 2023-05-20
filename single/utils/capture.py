import scapy.all as sca
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """
    数据包回调函数
    :param packet: 数据包
    :return: IP地址列表
    """
    ans = []
    if packet.haslayer(IP):
        if is_inner_IP(packet[IP].src):
            ans.append(packet[IP].src)
        if is_inner_IP(packet[IP].dst):
            ans.append(packet[IP].dst)
    return ans



def is_inner_IP(ip):
    """
    判断是否为内网IP
    :param ip: IP地址
    :return: True or False
    """
    ip = ip.split(".")
    if ip[0] == "10":
        return True
    elif ip[0] == "172" and 16 <= int(ip[1]) <= 31:
        return True
    elif ip[0] == "192" and ip[1] == "168":
        return True
    else:
        return False


def catch_packet(iface=None, count=0, timeout=None, filter=None):
    """
    捕获数据包
    :param iface: 网卡名称
    :param count: 捕获数据包数量
    :param timeout: 超时时间
    :return: IP地址列表
    """
    ans = []
    def packet_callback(packet):
        if packet.haslayer(IP):
            if is_inner_IP(packet[IP].src):
                ans.append(packet[IP].src)
            if is_inner_IP(packet[IP].dst):
                ans.append(packet[IP].dst)
    sca.sniff(prn=packet_callback, iface=iface, count=count, timeout=timeout, filter=filter)
    ans_dict = {}
    for ip in ans:
        ans_dict[ip] = ans_dict.get(ip, 0) + 1
    return ans_dict