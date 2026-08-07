from Conexion import DataBase
from ArchivosDAO.UsuarioDAO import UsuarioDAO
from Archivo.Usuario import Usuario
from Conexion import DataBase
import os
os.system("Cls")

DB = DataBase()
conexion = DB.conectar()
UsuDAO=UsuarioDAO(conexion)

def Encabezado():
    print("================BIENVENIDO A GATEWORLD================")

def PiePagina():
    print("=======================================================")

def Menu():
    while True:
        while True:
            Encabezado()
            print("1.-Login")
            print("2.-Registrarse")
            print("3.-Salir")
            Opcion=str(input("Ingresa La Accion a Realizar: "))
            match Opcion:
                case "1":
                    while True:
                        Encabezado()
                        Correo=input("Ingresa Tu Correo: ")
                        Contraseña=input("Ingresa Tu Contraseña: ")
                        Usuario=UsuDAO.login(Correo, Contraseña)
                        if Usuario:
                            print(f"Bienvenido De Vuelta", Usuario.Nombre_Usuario())
                            PiePagina()
                            while True:
                                Encabezado()
                                print("1.-Buscador")
                                print("2.-Agendas")
                                print("3.-Favoritos")
                                print("4.-Ajustes")
                                print(Usuario.Nombre_Usuario())
                                Opcion=str(input("Ingresa La Accion a Realizar: "))
                                PiePagina()
                                match Opcion:
                                    case "1":
                                        while True:
                                            
                                            break
                                    case "2":
                                        while True:

                                            break
                                    case "3":
                                        while True:

                                            break
                                    case "4":
                                        while True:

                                            break
                        else:
                            print("El Usuario o La contraseña Son Incorrectas")
                            PiePagina()
                case "2":
                    i = False
                    while not i:
                        Usuario = UsuDAO.crear()
                        if Usuario:
                            print("Registro Exitoso")
                            PiePagina()
                            i = True
                        else:
                            print("Registro Fallido, intenta de nuevo")
                            PiePagina()
                case "3":
                    break

Menu()
