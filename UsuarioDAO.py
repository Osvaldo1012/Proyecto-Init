from Usuario import Usuario


class UsuarioDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self, datos):
        cursor = self.conn.cursor()
        sql = """INSERT INTO usuario
                 (nombre, apellido_paterno, apellido_materno, correo,
                  disponible, telefono, contraseña, fecha_registro, Fk_asesor)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        self.conn.commit()
        return cursor.lastrowid

    def obtener_por_id(self, id_usuario):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE Id_usuario = %s", (id_usuario,))
        fila = cursor.fetchone()
        if fila:
            return Usuario(fila["Id_usuario"], fila["nombre"], fila["apellido_paterno"],
                            fila["apellido_materno"], fila["correo"], fila["disponible"],
                            fila["telefono"], fila["contraseña"], fila["fecha_registro"],
                            fila["Fk_asesor"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario")
        filas = cursor.fetchall()
        return [Usuario(f["Id_usuario"], f["nombre"], f["apellido_paterno"],
                         f["apellido_materno"], f["correo"], f["disponible"],
                         f["telefono"], f["contraseña"], f["fecha_registro"],
                         f["Fk_asesor"]) for f in filas]

    def actualizar(self, id_usuario, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE usuario SET nombre=%s, apellido_paterno=%s,
                 apellido_materno=%s, correo=%s, disponible=%s, telefono=%s,
                 contraseña=%s, fecha_registro=%s, Fk_asesor=%s
                 WHERE Id_usuario=%s"""
        cursor.execute(sql, (*datos, id_usuario))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_usuario):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE Id_usuario = %s", (id_usuario,))
        self.conn.commit()
        return cursor.rowcount