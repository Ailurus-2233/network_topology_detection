import pymysql

db = None

class Database:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.user = user
        self.port = port
        self.password = password
        self.db = db

        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        self.connection.commit()

def init_database(config):
    global db
    db = Database(
        config.host,
        config.port,
        config.user,
        config.password,
        config.db
    )


def insert_ip(ip):
    global db
    db.execute(f"INSERT INTO `ip_table` (`ip`) VALUES ('{ip}')")
    db.connection.commit()