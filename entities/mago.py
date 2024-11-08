from aventurero import Aventurero


class Mago(Aventurero):
    def __init__(
        self,
        nombre: str,
        id: int,
        ptos_habilidad: int,
        experiencia: int,
        dinero: float,
        mana: int,
    ):
        super().__init__(nombre, id, ptos_habilidad, experiencia, dinero)
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana
