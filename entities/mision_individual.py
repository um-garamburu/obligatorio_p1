from .mision import Mision


class MisionIndividual(Mision):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool):
        super().__init__(nombre, rango, recompensa, completado)
        self.__aventureros = None

    @property
    def aventureros(self):
        return self.__aventureros

    def agregar_aventurero(self, aventurero):
        self.__aventureros = aventurero
