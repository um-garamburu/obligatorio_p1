class AventureroNoEncontrado(Exception):
    def __init__(self, mensaje="Aventurero no encontrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
