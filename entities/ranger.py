from entities import Aventurero

class Ranger(Aventurero):
    def __init__(self, nombre:str, id:int, ptos_habilidad: int, experiencia: int, dinero: float, mascota):
        super().__init__(nombre, id, ptos_habilidad, experiencia, dinero)
        self._mascota = mascota

        @property
        def mascota(self):
            return mascota