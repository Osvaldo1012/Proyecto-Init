from Conexion import DataBase

DB = DataBase()
conexion = DB.conectar()

if conexion:
    print("Todo listo para comenzar.")
    conexion.close()