from abc import ABC


class Mision(ABC):
    def __init__(self, nombre: str, rango: int, recompensa: float, completado: bool):
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rango(self):
        return self.__rango

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def completado(self):
        return self.__completado
