from entities import Guerrero, Mago, Mascota, MisionGrupal, MisionIndividual, Ranger
from exceptions import InformacionInvalida


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

    def registrar_aventurero(
        self,
        clase: int,
        nombre: str,
        id: int,
        ptos_habilidad: int,
        experiencia: int,
        dinero: float,
        adicional: int = None,
        nombre_mascota: str = None,
        habilidad_mascota=None,
    ):
        temp_aventurero = None
        for aventurero in self.__aventureros:
            if aventurero.id == id:
                raise InformacionInvalida()
        match clase:
            case 1:
                temp_aventurero = Guerrero(
                    nombre, id, ptos_habilidad, experiencia, dinero, adicional
                )
            case 2:
                temp_aventurero = Mago(
                    nombre, id, ptos_habilidad, experiencia, dinero, adicional
                )
            case 3:
                temp_mascota = Mascota(nombre_mascota, habilidad_mascota)
                temp_aventurero = Ranger(
                    nombre, id, ptos_habilidad, experiencia, dinero
                )
                temp_aventurero.mascota = temp_mascota
        # if temp_aventurero is None or temp_aventurero in self.__aventureros:
        #     raise InformacionInvalida()
        self.__aventureros.append(temp_aventurero)
        return True

    def registrar_mision(
        self, nombre: int, rango: int, recompensa: float, min_miembros: int = 1
    ):

        if min_miembros == 1:
            MisionIndividual(
                nombre=nombre, rango=rango, recompensa=recompensa, completado=False
            )
        else:
            MisionGrupal(
                nombre=nombre,
                rango=rango,
                recompensa=recompensa,
                miembros=min_miembros,
                completado=False,
            )

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
    gremio = Gremio()
    try:
        gremio.registrar_aventurero(1, "Prueba", 1, 15, 15, 15.15, 45)
        gremio.registrar_aventurero(1, "Prueba", 1, 15, 15, 15.15, 45)
    except InformacionInvalida as e:
        print(f"Error: {e}")

    for aventureros in gremio.aventureros:
        print(aventureros.id)
