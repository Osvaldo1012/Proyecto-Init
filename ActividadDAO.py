from Actividad import Actividad


class ActividadDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO actividad
                 (Nombre, descripcion, precio, cupo, Lugar, Fecha_inicio, Fecha_final, fk_reserva)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_actividad):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM actividad WHERE id_actividad = %s", (id_actividad,))
        fila = cursor.fetchone()
        if fila:
            return Actividad(fila["id_actividad"], fila["Nombre"], fila["descripcion"],
                             fila["precio"], fila["cupo"], fila["Lugar"], fila["Fecha_inicio"],
                             fila["Fecha_final"], fila["fk_reserva"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM actividad")
        filas = cursor.fetchall()
        return [Actividad(f["id_actividad"], f["Nombre"], f["descripcion"],
                          f["precio"], f["cupo"], f["Lugar"], f["Fecha_inicio"],
                          f["Fecha_final"], f["fk_reserva"]) for f in filas]

    def actualizar(self, id_actividad, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE actividad SET Nombre=%s, descripcion=%s, precio=%s, cupo=%s,
                 Lugar=%s, Fecha_inicio=%s, Fecha_final=%s, fk_reserva=%s
                 WHERE id_actividad=%s"""
        cursor.execute(sql, (*datos, id_actividad))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_actividad):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM actividad WHERE id_actividad = %s", (id_actividad,))
        self.conn.commit()
        return cursor.rowcount