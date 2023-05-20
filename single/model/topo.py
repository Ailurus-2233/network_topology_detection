class Node:
    def __init__(self, id, device_type, ip):
        self.id = id
        self.device_type = device_type  # 0: host, 1: router
        self.ip = ip
        self.other_ip = []

    def is_router(self):
        return self.device_type == 1

    def is_contain_ip(self, ip):
        return ip in self.other_ip

    def add_ip(self, ip):
        self.other_ip.append(ip)

    def to_json_str(self):
        return '{"id": %d, "type": %d, "ip": "%s"}' % (
            self.id,
            self.device_type,
            self.ip,
        )


class Topo:
    def __init__(self):
        self.nodes = []
        self.links = []

    def init_topo(self, capture_ip, traceroute_path, snmp_ip_group):
        ip_map = {}
        for ip in capture_ip:
            id = len(self.nodes) + 1
            self.nodes.append(Node(id, 0, ip))
            ip_map[ip] = id

        snmp_ip_map = {}
        for ip_group in snmp_ip_group:
            id = len(self.nodes) + 1
            temp = Node(id, 1, ip_group[0])
            ip_map[ip_group[0]] = id
            for ip in ip_group:
                snmp_ip_map[ip] = ip_group[0]
                temp.add_ip(ip)
            self.nodes.append(temp)

        for path in traceroute_path:
            for i in range(1, len(path) - 1):
                path[i] = snmp_ip_map[path[i]]

        for path in traceroute_path:
            for i in range(len(path) - 1):
                from_id = ip_map[path[i]]
                to_id = ip_map[path[i + 1]]
                self.links.append(set([from_id, to_id]))
        self.links = list(set(self.links))

    def to_json_str(self):
        ans = ""
        ans += '{"nodes": ['
        for i in range(len(self.nodes)):
            ans += self.nodes[i].to_json_str()
            if i != len(self.nodes) - 1:
                ans += ","
        ans += '], "edges": ['
        for i in range(len(self.links)):
            ans += '{"from": %d, "to": %d}' % (
                list(self.links[i])[0],
                list(self.links[i])[1],
            )
            if i != len(self.links) - 1:
                ans += ","
        ans += "]}"
