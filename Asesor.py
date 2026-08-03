class Asesor:
    def __init__(self, id_asesor, nombre, apellido_paterno, apellido_materno,
                 correo, disponible, contraseña):
        self.id_asesor = id_asesor
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.correo = correo
        self.disponible = disponible
        self.contraseña = contraseña

    def get_id_asesor(self):
        return self.id_asesor

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

    def get_contraseña(self):
        return self.contraseña