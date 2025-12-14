import bcrypt
from models.database import Database

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    def guardar(self):
        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO usuarios (username, password)
            VALUES (:1, :2)
        """, (self.username, self.password))

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT password FROM usuarios WHERE username = :1
        """, (username,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:
            hashed = row[0].encode("utf-8")
            return bcrypt.checkpw(password.encode("utf-8"), hashed)

        return False
