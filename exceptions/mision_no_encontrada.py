class MisionNoEncontrada(Exception):
    def __init__(self, mensaje="Mision no encontrada"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
