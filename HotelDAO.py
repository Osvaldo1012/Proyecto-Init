import mysql.connector
from Hotel import Hotel


class HotelDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO hotel (Nombre, telefono, direccion, pais, ciudad)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_hotel):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM hotel WHERE Id_Hotel = %s", (id_hotel,))
        fila = cursor.fetchone()
        if fila:
            return Hotel(fila["Id_Hotel"], fila["Nombre"], fila["telefono"],
                        fila["direccion"], fila["pais"], fila["ciudad"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM hotel")
        filas = cursor.fetchall()
        return [Hotel(f["Id_Hotel"], f["Nombre"], f["telefono"],
                      f["direccion"], f["pais"], f["ciudad"]) for f in filas]

    def actualizar(self, id_hotel, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE hotel SET Nombre=%s, telefono=%s, direccion=%s, pais=%s, ciudad=%s
                 WHERE Id_Hotel=%s"""
        cursor.execute(sql, (*datos, id_hotel))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_hotel):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM hotel WHERE Id_Hotel = %s", (id_hotel,))
        self.conn.commit()
        return cursor.rowcount