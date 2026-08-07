class Usuario:
    def __init__(self, id_usuario, nombre, apellido_paterno, apellido_materno,
                 correo, disponible, telefono, contraseña, fecha_registro, fk_asesor):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.disponible = disponible
        self.telefono = telefono
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.fk_asesor = fk_asesor
    def get_id_usuario(self):
        return self.id_usuario

    def get_nombre(self):
        return self.nombre

    def get_apellido_paterno(self):
        return self.apellido_paterno

    def get_apellido_materno(self):
        return self.apellido_materno

    def get_correo(self):
        return self.correo

    def get_disponible(self):
        return self.disponible

    def get_telefono(self):
        return self.telefono

    def get_contraseña(self):
        return self.contraseña

    def get_fecha_registro(self):
        return self.fecha_registro

    def get_fk_asesor(self):
        return self.fk_asesor
    
    def __str__(self):
        return (f"{self.id_usuario}, {self.nombre}, {self.apellido_paterno}, {self.apellido_materno}, {self.correo}, {self.disponible}, {self.telefono}, {self.fecha_registro}")

    def __repr__(self):
        return self.__str__()

    def to_tuple(self): 
        return (self.id_usuario, self.nombre, self.apellido_paterno, self.apellido_materno,
                self.correo, self.disponible, self.telefono,
                self.contraseña, self.fecha_registro, self.fk_asesor)

    def Nombre_Usuario(self): #Retorna el nombre del usuario#
        return (f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}")
