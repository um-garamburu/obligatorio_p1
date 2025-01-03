from .aventurero import Aventurero


class Ranger(Aventurero):
    def __init__(
        self, nombre: str, id: int, ptos_habilidad: int, experiencia: int, dinero: float
    ):
        super().__init__(nombre, id, ptos_habilidad, experiencia, dinero)
        self.__mascota = None

    @property
    def mascota(self):
        return self.__mascota

    @mascota.setter
    def mascota(self, nueva_mascota):
        self.__mascota = nueva_mascota
    
    def habilidad_total(self):
        if self.__mascota:
            return self.ptos_habilidad + self.__mascota.ptos_habilidad
        else:
            return self.ptos_habilidad
