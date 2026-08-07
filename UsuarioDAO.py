from Archivo.Usuario import Usuario
import random
from datetime import datetime

class UsuarioDAO:
    def __init__(self, conn):
        self.conn = conn

    def crear(self):
        cursor = self.conn.cursor()
        id_usuario = random.randint(10**10, 10**11 - 1) #genera una id ramdon de como minimo 11 caracteres 
        fecha_registro = datetime.now().strftime("%Y-%m-%d") #utiliza la libreria de datatime la funcion now para obtener la hora y fecha actual 
        disponible = 1
        fk_asesor = None
        nombre = input(str("Ingresa Tu Nombre: "))
        apellido_paterno = input(str("Ingresa Tu Primer Apellido: "))
        apellido_materno = input(str("Ingresa Tu Segundo Apellido: "))
        correo = input(str("Ingresa Tu Correo: "))
        contrasena= input(str("Ingresa Tu Contraseña: "))
        while True:
            confirmacion= input(str("Confirma Tu Contraseña: "))
            if confirmacion == contrasena:
                contraseña=contrasena
                break
            else:
                print("La Contraseña Es Incorrecta Intenta Otra Vez")
        telefono = input(str("Ingresa Tu Numero De Telefono: ")) 
        sql = """INSERT INTO usuario
                 (id_usuario, nombre, apellido_paterno, apellido_materno, correo,
                  disponible, telefono, contraseña, fecha_registro, fk_asesor)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        datoscompletos=(id_usuario, nombre, apellido_paterno, apellido_materno, correo, disponible, telefono, contraseña, fecha_registro, fk_asesor)
        cursor.execute(sql, datoscompletos)
        self.conn.commit()
        return id_usuario

    def obtener_por_id(self, id_usuario):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
        fila = cursor.fetchone()
        if fila:
            return Usuario(fila["id_usuario"], fila["nombre"], fila["apellido_paterno"],
                            fila["apellido_materno"], fila["correo"], fila["disponible"],
                            fila["telefono"], fila["contraseña"], fila["fecha_registro"],
                            fila["fk_asesor"])
        return None

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario")
        filas = cursor.fetchall()
        return [Usuario(f["id_usuario"], f["nombre"], f["apellido_paterno"],
                         f["apellido_materno"], f["correo"], f["disponible"],
                         f["telefono"], f["contraseña"], f["fecha_registro"],
                         f["fk_asesor"]) for f in filas]

    def actualizar(self, id_usuario, datos):
        cursor = self.conn.cursor()
        sql = """UPDATE usuario SET nombre=%s, apellido_paterno=%s,
                 apellido_materno=%s, correo=%s, disponible=%s, telefono=%s,
                 contraseña=%s, fecha_registro=%s, fk_asesor=%s
                 WHERE id_usuario=%s"""
        cursor.execute(sql, (*datos, id_usuario))
        self.conn.commit()
        return cursor.rowcount

    def eliminar(self, id_usuario):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
        self.conn.commit()
        return cursor.rowcount

    def login(self, correo, contrasena):
        cursor = self.conn.cursor(dictionary=True)
        sql = "SELECT * FROM usuario WHERE correo = %s AND contraseña = %s"
        cursor.execute(sql, (correo, contrasena))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Usuario(
                fila["id_usuario"], fila["nombre"], fila["apellido_paterno"],
                fila["apellido_materno"], fila["correo"], fila["disponible"],
                fila["telefono"], fila["contraseña"], fila["fecha_registro"],
                fila["fk_asesor"]
            )
        else:
            return None
