from Agenda import Agenda


class AgendaDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO agenda (Nombre, Estado, Fecha_creacion, Fk_usuario)
                 VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_agenda):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agenda WHERE Id_Agenda = %s", (id_agenda,))
        fila = cursor.fetchone()
        if fila:
            return Agenda(fila["Id_Agenda"], fila["Nombre"], fila["Estado"],
                          fila["Fecha_creacion"], fila["Fk_usuario"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agenda")
        filas = cursor.fetchall()
        return [Agenda(f["Id_Agenda"], f["Nombre"], f["Estado"],
                       f["Fecha_creacion"], f["Fk_usuario"]) for f in filas]

    def actualizar(self, id_agenda, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE agenda SET Nombre=%s, Estado=%s, Fecha_creacion=%s, Fk_usuario=%s
                 WHERE Id_Agenda=%s"""
        cursor.execute(sql, (*datos, id_agenda))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_agenda):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM agenda WHERE Id_Agenda = %s", (id_agenda,))
        self.conn.commit()
        return cursor.rowcount
