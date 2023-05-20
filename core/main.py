from utils import config
from utils import database

config_path = "./config.json"

def main():
    c = config.Config(config_path)
    database.init_database(c)
    database.insert_ip("10.10.2.10")

if __name__ == "__main__":
    main()