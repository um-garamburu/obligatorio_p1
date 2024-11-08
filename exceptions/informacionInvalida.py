class InformacionInvalida(Exception):
    def __init__(self, mensaje="Informacion Invalida"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
