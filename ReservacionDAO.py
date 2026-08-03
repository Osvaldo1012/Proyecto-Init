import mysql.connector
from Reserva import Reservacion


class ReservacionDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO reservacion
                 (Estado, Fecha_Reservacion, Total, fk_agenda, fk_vuelo, fk_hotel)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_reservacion):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reservacion WHERE Id_Reservacion = %s", (id_reservacion,))
        fila = cursor.fetchone()
        if fila:
            return Reservacion(fila["Id_Reservacion"], fila["Estado"], fila["Fecha_Reservacion"],
                               fila["Total"], fila["fk_agenda"], fila["fk_vuelo"], fila["fk_hotel"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM reservacion")
        filas = cursor.fetchall()
        return [Reservacion(f["Id_Reservacion"], f["Estado"], f["Fecha_Reservacion"],
                            f["Total"], f["fk_agenda"], f["fk_vuelo"], f["fk_hotel"]) for f in filas]

    def actualizar(self, id_reservacion, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE reservacion SET Estado=%s, Fecha_Reservacion=%s, Total=%s,
                 fk_agenda=%s, fk_vuelo=%s, fk_hotel=%s WHERE Id_Reservacion=%s"""
        cursor.execute(sql, (*datos, id_reservacion))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_reservacion):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM reservacion WHERE Id_Reservacion = %s", (id_reservacion,))
        self.conn.commit()
        return cursor.rowcount