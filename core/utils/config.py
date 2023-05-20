import json


class Config:
    def __init__(self, path):
        with open(path, "r") as f:
            config = json.load(f)
        self.host = config["db_host"]
        self.port = config["db_port"]
        self.user = config["db_user"]
        self.password = config["db_password"]
        self.db = config["db_database"]
        self.type = config["type"]
        self.net_iface = config["net_iface"]
