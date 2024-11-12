from entities import Guerrero, Mago, Mascota, MisionGrupal, MisionIndividual, Ranger
from exceptions import InformacionInvalida, RangoInsuficiente


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

                temp_aventurero = Ranger(
                    nombre, id, ptos_habilidad, experiencia, dinero
                )
                if nombre_mascota and habilidad_mascota:
                    temp_mascota = Mascota(nombre_mascota, habilidad_mascota)
                    temp_aventurero.mascota = temp_mascota
        # if temp_aventurero is None or temp_aventurero in self.__aventureros:
        #     raise InformacionInvalida()
        self.__aventureros.append(temp_aventurero)
        return True

    def registrar_mision(
        self, nombre: str, rango: int, recompensa: float, miembros: int = 1
    ):
        for mision in self.__misiones:
            if mision.nombre == nombre:
                raise InformacionInvalida()

        if miembros == 1:
            nueva_mision = MisionIndividual(
                nombre=nombre, rango=rango, recompensa=recompensa, completado=False
            )
            # self.__misiones.append(nueva_mision)
        else:
            nueva_mision = MisionGrupal(
                nombre=nombre,
                rango=rango,
                recompensa=recompensa,
                completado=False,
                min_miembros=miembros,
            )
            # self.__misiones.append(nueva_mision)
        self.__misiones.append(nueva_mision)

    def realizar_mision(self, mision_a_completar: str, aventureros_id: list):
        temp_mision = None
        for mision in self.__misiones:
            if mision.nombre == mision_a_completar:
                temp_mision = mision
                break
        if mision is None:
            raise InformacionInvalida()

        if isinstance(temp_mision, MisionIndividual):
            if len(aventureros_id) > 1:
                raise InformacionInvalida()
        if isinstance(temp_mision, MisionGrupal):
            if len(aventureros_id) < temp_mision.min_miembros:
                raise InformacionInvalida()
        aventureros_list = []
        for id in aventureros_id:
            temp_avent = None
            for aventurero in self.__aventureros:
                if id == aventurero.id:
                    temp_avent = aventurero
                    aventureros_list.append(temp_avent)
            if temp_avent is None:
                raise InformacionInvalida()

        for aventurero_encontrado in aventureros_list:
            # print(aventurero_encontrado.habilidad_total())
            match temp_mision.rango:
                case 1:
                    if aventurero_encontrado.habilidad_total() < 1:
                        raise RangoInsuficiente()
                case 2:
                    if aventurero_encontrado.habilidad_total() < 21:
                        raise RangoInsuficiente()
                case 3:
                    if aventurero_encontrado.habilidad_total() < 41:
                        raise RangoInsuficiente()
                case 4:
                    if aventurero_encontrado.habilidad_total() < 61:
                        raise RangoInsuficiente()
                case 5:
                    if aventurero_encontrado.habilidad_total() < 81:
                        raise RangoInsuficiente()
                    if isinstance(aventurero_encontrado, Ranger):
                        if aventurero_encontrado.ptos_habilidad < 81:
                            raise RangoInsuficiente()

        for aventurero_luego_mision in aventureros_list:
            aventurero_luego_mision.agregar_recompensa(
                temp_mision.recompensa / len(aventureros_id)
            )
            match temp_mision.rango:
                case 1:
                    aventurero_luego_mision.agregar_experiencia(5)
                case 2:
                    aventurero_luego_mision.agregar_experiencia(10)
                case 3:
                    aventurero_luego_mision.agregar_experiencia(20)
                case 4:
                    aventurero_luego_mision.agregar_experiencia(50)
                case 5:
                    aventurero_luego_mision.agregar_experiencia(100)
            aventurero_luego_mision.agregar_mision_completada(temp_mision)
            temp_mision.agregar_aventurero(aventurero_luego_mision)
        temp_mision.completado = True
        return temp_mision.completado

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
        gremio.registrar_mision("mision1", 1, 100, 5)
        gremio.registrar_mision("mision3", 2, 100, 2)
        gremio.registrar_mision("mision2", 3, 100)
        gremio.registrar_aventurero(1, "av1", 1, 24, 0, 150, 50)
        gremio.registrar_aventurero(2, "av2", 2, 10, 0, 150, 200)
        gremio.registrar_aventurero(3, "av3", 3, 7, 0, 150, 0, "msc1", 40)
        gremio.registrar_aventurero(3, "av4", 4, 7, 0, 150)
        gremio.registrar_aventurero(1, "av5", 5, 24, 0, 150, 50)
        gremio.realizar_mision("mision1", [1, 2, 3, 4, 5])

    except InformacionInvalida as e:
        print(f"Error: {e}")
    except RangoInsuficiente as e:
        print(f"Error: {e}")

    for mision in gremio.misiones:
        print(mision.nombre)

    for aventurero in gremio.aventureros:
        print(
            aventurero.nombre,
            aventurero.id,
            aventurero.experiencia,
            aventurero.dinero,
        )
