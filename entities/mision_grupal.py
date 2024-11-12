from .mision import Mision


class MisionGrupal(Mision):
    def __init__(
        self,
        nombre: str,
        rango: int,
        recompensa: float,
        completado: bool,
        min_miembros: int,
    ):
        super().__init__(nombre, rango, recompensa, completado)
        self.__min_miembros = min_miembros
        self.__aventureros = []

    @property
    def min_miembros(self):
        return self.__min_miembros

    @property
    def aventureros(self):
        return self.__aventureros

    def agregar_aventurero(self, aventurero):
        self.__aventureros.append(aventurero)
