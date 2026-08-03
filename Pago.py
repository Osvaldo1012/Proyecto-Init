class Pago:
    def __init__(self, id_pago, total, estado, fecha_pago, metodo_pago, fk_reservacion):
        self.id_pago = id_pago
        self.total = total
        self.estado = estado
        self.fecha_pago = fecha_pago
        self.metodo_pago = metodo_pago
        self.fk_reservacion = fk_reservacion

    def get_id_pago(self):
        return self.id_pago

    def get_total(self):
        return self.total

    def get_estado(self):
        return self.estado

    def get_fecha_pago(self):
        return self.fecha_pago

    def get_metodo_pago(self):
        return self.metodo_pago

    def get_fk_reservacion(self):
        return self.fk_reservacion