class MisionCompletada(Exception):
    def __init__(self, mensaje="Esta mision ya fue completada!"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
