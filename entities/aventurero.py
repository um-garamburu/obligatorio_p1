from abc import ABC

class aventurero(ABC):
    def __init__(self, nombre:str, id:int, ptos_habilidad: int, experiencia: int, dinero: float)
        self._nombre = nombre
        self._id = id
        self._ptos_habilidad = ptos_habilidad
        self._experiencia = experiencia
        self._dinero = dinero

        @property
        def nombre(self):
            return self._nombre
        @property
        def id(self):
            return self._id
        @property
        def ptos_habilidad(self):
            return self._ptos_habilidad
        @property
        def experiencia(self):
            return self._experiencia
        @property
        def dinero(self):
            return self._dinero
                