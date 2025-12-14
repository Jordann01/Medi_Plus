from models.database import Database

conn = Database.get_connection()

if conn:
    print("Conexión exitosa a Oracle!")
    cursor = conn.cursor()
    cursor.execute("SELECT table_name FROM user_tables")  
    for row in cursor:
        print("Tabla:", row[0])  
    conn.close()
else:
    print("Error en la conexión.")
