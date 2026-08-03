from Pago import Pago


class PagoDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO pago (total, Estado, Fechapago, Metodo_pago, fk_reservacion)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_pago):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pago WHERE id_pago = %s", (id_pago,))
        fila = cursor.fetchone()
        if fila:
            return Pago(fila["id_pago"], fila["total"], fila["Estado"],
                       fila["Fechapago"], fila["Metodo_pago"], fila["fk_reservacion"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pago")
        filas = cursor.fetchall()
        return [Pago(f["id_pago"], f["total"], f["Estado"],
                     f["Fechapago"], f["Metodo_pago"], f["fk_reservacion"]) for f in filas]

    def actualizar(self, id_pago, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE pago SET total=%s, Estado=%s, Fechapago=%s,
                 Metodo_pago=%s, fk_reservacion=%s WHERE id_pago=%s"""
        cursor.execute(sql, (*datos, id_pago))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_pago):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pago WHERE id_pago = %s", (id_pago,))
        self.conn.commit()
        return cursor.rowcount