class Vuelo:
    def __init__(self, id_vuelo, aerolinea, precio, destino, origen,
                 disponible, fecha_salida, fecha_llegada):
        self.id_vuelo = id_vuelo
        self.aerolinea = aerolinea
        self.precio = precio
        self.destino = destino
        self.origen = origen
        self.disponible = disponible
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada

    def get_id_vuelo(self):
        return self.id_vuelo

    def get_aerolinea(self):
        return self.aerolinea

    def get_precio(self):
        return self.precio

    def get_destino(self):
        return self.destino

    def get_origen(self):
        return self.origen

    def get_disponible(self):
        return self.disponible

    def get_fecha_salida(self):
        return self.fecha_salida

    def get_fecha_llegada(self):
        return self.fecha_llegada