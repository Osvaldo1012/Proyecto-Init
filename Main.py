from Conexion import DataBase
from ArchivosDAO.UsuarioDAO import UsuarioDAO
from Archivo.Usuario import Usuario
from ArchivosDAO.VueloDAO import VueloDAO
from Archivo.Vuelo import Vuelo
from ArchivosDAO.HotelDAO import HotelDAO
from Archivo.Hotel import Hotel
from ArchivosDAO.HabitacionDAO import HabitacionDAO
from Archivo.Habitacion import Habitacion
from ArchivosDAO.AsesorDAO import AsesorDAO
from Archivo.Asesor import Asesor
from ArchivosDAO.ActividadDAO import ActividadDAO
from Archivo.Actividad import Actividad
from ArchivosDAO.PagoDAO import PagoDAO
from Archivo.Pago import Pago
from ArchivosDAO.ReservacionDAO import ReservacionDAO
from Archivo.Reserva import Reservacion



import os
os.system("Cls")

DB = DataBase()
conexion = DB.conectar()
UsuDAO=UsuarioDAO(conexion)
VueDAO=VueloDAO(conexion)
HotDAO=HotelDAO(conexion)
HabiDAO=HabitacionDAO(conexion)
AseDAO=AsesorDAO(conexion)
ActDAO=ActividadDAO(conexion)
PaDAO=PagoDAO(conexion)
ReserDAO=ReservacionDAO(conexion)


def Encabezado():
    print("================BIENVENIDO A GATEWORLD================")

def PiePagina():
    print("=======================================================")

def Menu():
    while True:
        Encabezado()
        print("1.-Login")
        print("2.-Registrarse")
        print("3.-Salir")
        Opcion=str(input("Ingresa La Accion a Realizar: "))
        PiePagina()
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
                            print("2.-Mis Agendas")
                            print("3.-Mis Favoritos")
                            print("4.-Mis Pagos")
                            print("4.-Ajustes")
                            print("5.-salir")
                            print(Usuario.Nombre_Usuario())
                            Opcion=str(input("Ingresa La Accion a Realizar: "))
                            PiePagina()
                            match Opcion:
                                case "1":
                                        Encabezado()
                                        print("Vuelos Disponibles")
                                        for Vuelo in VueDAO.obtener_todos():
                                            print(Vuelo)
                                        PiePagina()
                                case "2":
                                    while True:
                                        Encabezado()
                                        PiePagina()
                                        break
                                case "3":
                                    while True:
                                        Encabezado()
                                        PiePagina()
                                        break
                                case "4":
                                    while True:
                                        Encabezado()
                                        PiePagina()
                                        break
                                case "5":
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

def Main():
    while True:
        Encabezado()
        print("1.-Login")
        print("2.-Registrarse")
        print("3.-Salir")
        Opcion=str(input("Ingresa La Accion a Realizar: "))
        PiePagina()
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
                            print("1.-Administrar Hoteles")
                            print("2.-Administrar Habitaciones")
                            print("3.-Administrar Vuelos")
                            print("4.-Administrar Usuarios")
                            print("5.-Administrar Aserores")
                            print("6.-salir")
                            Opcion=str(input("Ingresa La Accion a Realizar: "))
                            PiePagina()
                            match Opcion:
                                case "1":
                                    while True:
                                        print("")
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
                                case "5":
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
