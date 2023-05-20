from utils import capture, snmp, traceroute
import json
from model import topo

def main():
    # 读取配置文件
    config_path = "config.json"
    config = json.load(open(config_path, "r"))
    
    # 启动捕获流量
    nodes_ip = capture.catch_packet(
        iface=config["iface"],
        count=config["count"],
        timeout=config["timeout"],
        filter=config["filter"],
    )

    # 使用traceroute获取路径
    paths = []
    for ip in nodes_ip:
        paths.append(traceroute.get_traceroute(ip))
    
    # 使用snmp获取路由节点的其他ip
    snmp_ip_group = []
    for path in paths:
        for i in range(1, len(path) - 1):
            snmp_ip_group.append(snmp.get_router_interfaces_ip(path[i], "public"))
    
    # 构建拓扑
    ans = topo.Topo()
    ans.init_topo(nodes_ip, paths, snmp_ip_group)

    # 输出拓扑
    with open("topo.json", "w") as f:
        f.write(ans.to_json_str())