class Hotel:
    def __init__(self, id_hotel, nombre, telefono, direccion, pais, ciudad):
        self.id_hotel = id_hotel
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.pais = pais
        self.ciudad = ciudad

    def get_id_hotel(self):
        return self.id_hotel

    def get_nombre(self):
        return self.nombre

    def get_telefono(self):
        return self.telefono

    def get_direccion(self):
        return self.direccion

    def get_pais(self):
        return self.pais

    def get_ciudad(self):
        return self.ciudad