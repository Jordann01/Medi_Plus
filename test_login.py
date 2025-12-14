from models.usuario import Usuario

if Usuario.login("admin3", "admin123"):
    print(" Login correcto")
else:
    print(" Login incorrecto")
