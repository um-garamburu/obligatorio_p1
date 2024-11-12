class RangoInsuficiente(Exception):
    def __init__(self, mensaje="Rango insuficiente para realizar la mision"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
