class Agenda:
    def __init__(self, id_agenda, nombre, estado, fecha_creacion, fk_usuario):
        self.id_agenda = id_agenda
        self.nombre = nombre
        self.estado = estado
        self.fecha_creacion = fecha_creacion
        self.fk_usuario = fk_usuario

    def get_id_agenda(self):
        return self.id_agenda

    def get_nombre(self):
        return self.nombre

    def get_estado(self):
        return self.estado

    def get_fecha_creacion(self):
        return self.fecha_creacion

    def get_fk_usuario(self):
        return self.fk_usuario