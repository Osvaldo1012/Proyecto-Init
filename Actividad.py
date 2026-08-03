class Actividad:
    def __init__(self, id_actividad, nombre, descripcion, precio, cupo,
                 lugar, fecha_inicio, fecha_final, fk_reserva):
        self.id_actividad = id_actividad
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cupo = cupo
        self.lugar = lugar
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.fk_reserva = fk_reserva

    def get_id_actividad(self):
        return self.id_actividad

    def get_nombre(self):
        return self.nombre

    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio

    def get_cupo(self):
        return self.cupo

    def get_lugar(self):
        return self.lugar

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_fecha_final(self):
        return self.fecha_final

    def get_fk_reserva(self):
        return self.fk_reserva