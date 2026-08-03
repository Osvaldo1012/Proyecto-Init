import mysql.connector
from Asesor import Asesor


class AsesorDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO asesor
                 (nombre, apellido_paterno, apellido_materno, correo, disponible, contraseña)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_asesor):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM asesor WHERE Id_asesor = %s", (id_asesor,))
        fila = cursor.fetchone()
        if fila:
            return Asesor(fila["Id_asesor"], fila["nombre"], fila["apellido_paterno"],
                          fila["apellido_materno"], fila["correo"], fila["disponible"],
                          fila["contraseña"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM asesor")
        filas = cursor.fetchall()
        return [Asesor(f["Id_asesor"], f["nombre"], f["apellido_paterno"],
                       f["apellido_materno"], f["correo"], f["disponible"],
                       f["contraseña"]) for f in filas]

    def actualizar(self, id_asesor, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE asesor SET nombre=%s, apellido_paterno=%s,
                 apellido_materno=%s, correo=%s, disponible=%s, contraseña=%s
                 WHERE Id_asesor=%s"""
        cursor.execute(sql, (*datos, id_asesor))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_asesor):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM asesor WHERE Id_asesor = %s", (id_asesor,))
        self.conn.commit()
        return cursor.rowcount