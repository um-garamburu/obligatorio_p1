from .mision import Mision


class MisionGrupal(Mision):
    def __init__(
        self,
        nombre: str,
        rango: int,
        recompensa: float,
        completado: bool,
        miembros: int,
    ):
        super().__init__(nombre, rango, recompensa, completado)
        self.__miembros = miembros

    @property
    def miembros(self):
        self.__miembros
