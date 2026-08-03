class Habitacion:
    def __init__(self, id_habitacion, precio, disponibilidad, capacidad, tipo, fk_hotel):
        self.id_habitacion = id_habitacion
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.capacidad = capacidad
        self.tipo = tipo
        self.fk_hotel = fk_hotel

    def get_id_habitacion(self):
        return self.id_habitacion

    def get_precio(self):
        return self.precio

    def get_disponibilidad(self):
        return self.disponibilidad

    def get_capacidad(self):
        return self.capacidad

    def get_tipo(self):
        return self.tipo

    def get_fk_hotel(self):
        return self.fk_hotel