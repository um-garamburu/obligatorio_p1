from abc import ABC


class Aventurero(ABC):
    def __init__(
        self, nombre: str, id: int, ptos_habilidad: int, experiencia: int, dinero: float
    ):
        self.__nombre = nombre
        self.__id = id
        self.__ptos_habilidad = ptos_habilidad
        self.__experiencia = experiencia
        self.__dinero = dinero
        self.__misiones = []

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

    @property
    def misiones(self):
        return self.__misiones

    @ptos_habilidad.setter
    def ptos_habilidad(self, nuevos_ptos_habilidad):
        self.ptos_habilidad = nuevos_ptos_habilidad

    def agregar_mision_completada(self, mision):
        self.__misiones.append(mision)
    
    def cantidad_misiones_resueltas(self):
        return len(self.__misiones)

    def agregar_recompensa(self, recompensa):
        self.__dinero += round(recompensa, 2)

    def agregar_experiencia(self, exp):
        self.__experiencia += exp

    def __eq__(self, nuevo_aventurero):
        if isinstance(nuevo_aventurero, Aventurero):
            return self.__id == nuevo_aventurero.id
        return False
