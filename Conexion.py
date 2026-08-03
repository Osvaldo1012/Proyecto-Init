import mysql.connector

class DataBase:

    def __init__(self, Db="interworld", Host="localhost", Usuario="root", Contraseña=""):
        self.datos = {
            "host": Host,
            "user": Usuario,
            "password": Contraseña,
            "database": Db
        }
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.datos)
            print("Conexión exitosa a", self.datos["database"])
            return self.conexion

        except mysql.connector.Error as e:
            print(f"Error al conectar: {e}")
            return None

    def cerrar(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada.")