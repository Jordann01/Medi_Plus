import oracledb

class Database:
    @staticmethod
    def get_connection():
        try:
            connection = oracledb.connect(
                user="mediplus",
                password="admin123",
                dsn="127.0.0.1:1522/orclpdb"
            )
            return connection

        except Exception as e:
            print("Error al conectar:", e)
            return None
