class Reservacion:
    def __init__(self, id_reservacion, estado, fecha_reservacion, total,
                 fk_agenda, fk_vuelo, fk_hotel):
        self.id_reservacion = id_reservacion
        self.estado = estado
        self.fecha_reservacion = fecha_reservacion
        self.total = total
        self.fk_agenda = fk_agenda
        self.fk_vuelo = fk_vuelo
        self.fk_hotel = fk_hotel

    def get_id_reservacion(self):
        return self.id_reservacion

    def get_estado(self):
        return self.estado

    def get_fecha_reservacion(self):
        return self.fecha_reservacion

    def get_total(self):
        return self.total

    def get_fk_agenda(self):
        return self.fk_agenda

    def get_fk_vuelo(self):
        return self.fk_vuelo

    def get_fk_hotel(self):
        return self.fk_hotel