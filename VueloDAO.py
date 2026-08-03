from Vuelo import Vuelo


class VueloDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO vuelo
                 (aerolinea, precio, destino, origen, disponible, fecha_salida, fecha_llegada)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_vuelo):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vuelo WHERE id_vuelo = %s", (id_vuelo,))
        fila = cursor.fetchone()
        if fila:
            return Vuelo(fila["id_vuelo"], fila["aerolinea"], fila["precio"], fila["destino"],
                        fila["origen"], fila["disponible"], fila["fecha_salida"], fila["fecha_llegada"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vuelo")
        filas = cursor.fetchall()
        return [Vuelo(f["id_vuelo"], f["aerolinea"], f["precio"], f["destino"],
                      f["origen"], f["disponible"], f["fecha_salida"], f["fecha_llegada"]) for f in filas]

    def actualizar(self, id_vuelo, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE vuelo SET aerolinea=%s, precio=%s, destino=%s, origen=%s,
                 disponible=%s, fecha_salida=%s, fecha_llegada=%s WHERE id_vuelo=%s"""
        cursor.execute(sql, (*datos, id_vuelo))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_vuelo):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM vuelo WHERE id_vuelo = %s", (id_vuelo,))
        self.conn.commit()
        return cursor.rowcount
