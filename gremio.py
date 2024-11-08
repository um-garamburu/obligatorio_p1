from entities import Guerrero, Mago, Mascota, MisionGrupal, MisionIndividual, Ranger


class Gremio:
    def __init__(self):
        self.__misiones = []
        self.__aventureros = []

    @property
    def misiones(self):
        return self.__misiones

    @property
    def aventureros(self):
        return self.__aventureros

    def registrar_aventurero(self):
        pass

    def registrar_mision(self, nombre: int, rango: int, recompensa:float, min_miembros: int = 1):

        if min_miembros == 1:
            MisionIndividual(nombre=nombre, rango=rango,recompensa=recompensa,completado = False)
        else:
            MisionGrupal(nombre=nombre, rango=rango,recompensa=recompensa,miembros=min_miembros,completado = False) 
            

    def realizar_mision(self):
        pass

    def top_10_misiones_resueltas(self):
        pass

    def top_10_habilidad(self):
        pass

    def top_10_misiones_recompensa(self):
        pass

    def aventureros_por_clase(self):
        pass


if __name__ == "__main__":
    try:
        pass
    except:
        pass
