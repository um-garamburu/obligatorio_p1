from entities import Guerrero, Mago, Mascota, MisionGrupal, MisionIndividual, Ranger
from exceptions import (
    InformacionInvalida,
    RangoInsuficiente,
    MisionNoEncontrada,
    AventureroNoEncontrado,
    MisionCompletada)


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
            case _:
                raise InformacionInvalida()

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
            raise MisionNoEncontrada()
        if mision.completado:
            raise MisionCompletada()

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
                raise AventureroNoEncontrado()

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
        aventureros_ordenados = sorted(
            self.__aventureros,
            key=lambda a: (-a.cantidad_misiones_resueltas(), a.nombre),
        )
        aventureros_con_mision = []
        for aventurero in aventureros_ordenados:
            if aventurero.cantidad_misiones_resueltas() > 0:
                aventureros_con_mision.append(aventurero)
        print("\n**************************")
        if len(aventureros_con_mision):
            lista_minima = min(len(aventureros_con_mision), 10)
            for i in range(lista_minima):
                print(
                    f"{i+1}. Aventurero: {aventureros_con_mision[i].nombre}, habilidad total: {aventureros_con_mision[i].habilidad_total()}, Misiones resueltas: {aventureros_con_mision[i].cantidad_misiones_resueltas()}"
                )
        else:
            print('No hay aventureros con misiones resueltas!')
        print("**************************")

    def top_10_habilidad(self):
        aventureros_ordenados = sorted(
            self.__aventureros, key=lambda a: (-a.habilidad_total(), a.nombre)
        )
        lista_minima = min(len(aventureros_ordenados), 10)
        print("\n**************************")
        if len(aventureros_ordenados):
            for i in range(lista_minima):
                print(
                    f"{i+1}. Aventurero: {aventureros_ordenados[i].nombre}, habilidad total: {aventureros_ordenados[i].habilidad_total()}"
                )
        else:
            print('No hay aventureros creados!')
        print("**************************")

    def top_5_misiones_recompensa(self):
        misiones_ordenadas = sorted(
            self.__misiones, key=lambda m: (-m.recompensa, m.nombre)
        )
        lista_minima = min(len(misiones_ordenadas), 5)
        print("\n**************************")
        if len(misiones_ordenadas):

            for i in range(lista_minima):
                print(
                    f"{i+1}. Mision: {misiones_ordenadas[i].nombre}, recompensa: {misiones_ordenadas[i].recompensa}"
                )
        else:
            print('No hay misiones registradas!')
        print("**************************")

    def aventureros_por_clase(self):
        rangers = []
        magos = []
        guerreros = []
        for aventurero in self.__aventureros:
            if isinstance(aventurero, Ranger):
                rangers.append(aventurero)
            elif isinstance(aventurero, Mago):
                magos.append(aventurero)
            elif isinstance(aventurero, Guerrero):
                guerreros.append(aventurero)
        rangers = sorted(rangers, key=lambda a: a.nombre)
        magos = sorted(magos, key=lambda a: a.nombre)
        guerreros = sorted(guerreros, key=lambda a: a.nombre)
        print("\n**************************")
        if len(rangers):
            print("Rangers:")
            for ranger in rangers:
                print(
                    f"- Nombre: {ranger.nombre}, ID: {ranger.id}, Habilidad: {ranger.habilidad_total()}"
                )
        if len(magos):
            print("Magos:")
            for mago in magos:
                print(
                    f"- Nombre: {mago.nombre}, ID: {mago.id}, Habilidad: {mago.habilidad_total()}"
                )
        if len(guerreros):
            print("Guerreros:")
            for guerrero in guerreros:
                print(
                    f"- Nombre: {guerrero.nombre}, ID: {guerrero.id}, Habilidad: {guerrero.habilidad_total()}"
                )
        if len(rangers) + len(magos) + len(guerreros) == 0:
            print('No hay aventureros registrados!')
        print("**************************")
