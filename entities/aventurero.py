from abc import ABC

class aventurero(ABC):
    def __init__(self, nombre:str, id:int, ptos_habilidad: int, experiencia: int, dinero: float):
        self.__nombre = nombre
        self.__id = id
        self.__ptos_habilidad = ptos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero

    @property
    def nombre(self):
        return self.__nombre
    @property
    def id(self):
        return self.__id
    @property
    def ptos_habilidad(self):
        return self.__ptos_habilidad
    @property
    def experiencia(self):
        return self.__experiencia
    @property
    def dinero(self):
        return self.__dinero
                