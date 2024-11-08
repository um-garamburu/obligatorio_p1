

class Mascota:
    def __init__(self,nombre: str,ptos_habilidad: int):
        self.__nombre = nombre
        self.__ptos_habilidad = ptos_habilidad
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def ptos_habilidad(self):
        return self.__ptos_habilidad