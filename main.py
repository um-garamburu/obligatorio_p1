from gremio import Gremio
from exceptions import InformacionInvalida, MisionNoEncontrada, AventureroNoEncontrado, RangoInsuficiente, MisionCompletada


def bienvenida():
    titulo = "Bienvenido al Simulador de Gremio de Aventureros!"
    len_titulo = len(titulo) + 4
    print("*" * len_titulo)
    print("* " + titulo + " *")
    print("*" * len_titulo)


def menu_principal():
    gremio = Gremio()

    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Salir")

        opcion = input("Ingresar Opcion: ")

        if opcion == "1":

            try:
                clase = input(
                    "\nElija la clase del aventurero:\n1. Guerrero\n2. Mago\n3. Ranger\nInrgese numero de opcion: ")
                if clase == '':
                    raise InformacionInvalida
                clase = int(clase)
                if clase not in [1, 2, 3]:
                    raise InformacionInvalida

                nombre = input("Ingrese el nombre del aventurero: ")

                id = input("Ingresar el ID: ")
                if id =='':
                    raise InformacionInvalida
                id = int(id)

                ptos_habilidad = input("Ingrese puntos de habilidad (0-100): ")
                if ptos_habilidad == '':
                    raise InformacionInvalida
                ptos_habilidad = int(ptos_habilidad)
                if ptos_habilidad < 0 or ptos_habilidad > 100:
                    raise InformacionInvalida

                experiencia = input("Ingrese Experiencia del aventurero: ")
                if experiencia == '':
                    raise InformacionInvalida
                experiencia = int(experiencia)

                dinero = input("Ingresar Dinero del aventurero: ")
                if dinero == '':
                    raise InformacionInvalida
                dinero = float(dinero)

                nombre_mascota = None
                habilidad_mascota = None
                adicional = None

                match clase:
                    case 1:
                        adicional = input("Ingresar Fuerza (0-100): ")
                        if adicional == '':
                            raise InformacionInvalida
                        adicional = int(adicional)
                        if adicional < 0 or adicional > 100:
                            raise InformacionInvalida

                    case 2:
                        adicional = input("Ingresar mana (0-1000): ")
                        if adicional == '':
                            raise InformacionInvalida
                        adicional = int(adicional)
                        if adicional < 0 or adicional > 1000:
                            raise InformacionInvalida

                    case 3:
                        adicional = None
                        tiene_mascota = input("Agregar una mascota? (S/N): ").upper()
                        # tiene_mascota.upper()
                        if tiene_mascota == "S":
                            nombre_mascota = input("Ingresar Nombre de la mascota: ")
                            habilidad_mascota = input(
                                "ingresar Puntos de habilidad de la mascota: "
                            )
                            if habilidad_mascota == '':
                                raise InformacionInvalida
                            habilidad_mascota = int(habilidad_mascota)
                        elif tiene_mascota != "N":
                            raise InformacionInvalida

                result = gremio.registrar_aventurero(
                    clase,
                    nombre,
                    id,
                    ptos_habilidad,
                    experiencia,
                    dinero,
                    adicional,
                    nombre_mascota,
                    habilidad_mascota,
                )
                if result:
                    print("\nAventurero registrado con éxito!\n")

            except InformacionInvalida as e:
                print(f"*** Error: {e} ***")

        elif opcion == "2":
            try:

                nombre = input("Ingresar Nombre: ")
                rango = input("Ingresar Rango: ")
                if rango == '':
                    raise InformacionInvalida
                rango = int(rango)
                if rango not in [1, 2, 3, 4, 5]:
                    raise InformacionInvalida
                recompensa = input("Ingresar Recompensa: ")
                if recompensa == '':
                    raise InformacionInvalida
                recompensa = float(recompensa)
                mision_grupal = input("La mision es Grupal? (S/N): ")
                mision_grupal = mision_grupal.upper()
                if mision_grupal == "S":
                    min_miembros = input("Ingresar cantidad minima de miembros: ")
                    if min_miembros == '':
                        raise InformacionInvalida
                    min_miembros = int(min_miembros)
                elif mision_grupal == "N":
                    min_miembros = 1
                else:
                    raise InformacionInvalida

                reult = gremio.registrar_mision(nombre, rango, recompensa, min_miembros)
                if result:
                    print("\nMision registrada con éxito!\n")

            except InformacionInvalida as e:
                print(f"*** Error: {e} ***")

        elif opcion == "3":
            try:
                nombre_mision = input(
                    "Ingresar el nombre de la mision que desea realizar: "
                )
                mision_elegida = None
                for mision in gremio.misiones:
                    if mision.nombre == nombre_mision:
                        mision_elegida = mision.nombre

                if mision_elegida == None:
                    raise MisionNoEncontrada

                aventureros = []
                while True:
                    nuevo_aventurero = input("Ingresar ID de aventurero: ")
                    if nuevo_aventurero == '':
                        raise InformacionInvalida
                    nuevo_aventurero = int(nuevo_aventurero)
                    aventureros.append(nuevo_aventurero)
                    mas_aventureros = input("Desea Ingresar mas aventureros? (S/N): ")
                    mas_aventureros = mas_aventureros.upper()
                    if mas_aventureros == "N":
                        break
                result = gremio.realizar_mision(mision_elegida, aventureros)
                if result:
                    print("\nMision realizada con éxito!\n")

            except InformacionInvalida as e:
                print(f"*** Error: {e}*** ")
            except MisionNoEncontrada as e:
                print(f"*** Error: {e}*** ")
            except AventureroNoEncontrado as e:
                print(f"*** Error: {e}*** ")
            except RangoInsuficiente as e:
                print(f"*** Error: {e}*** ")
            except MisionCompletada as e:
                print(f"*** Error: {e}*** ")

        elif opcion == "4":
            submenu_consultas(gremio)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, elija una opción del menú.")


def submenu_consultas(gremio):
    while True:
        print("\nSeleccione una opción de consulta:")
        print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
        print("2. Ver Top 10 Aventureros con Mayor Habilidad")
        print("3. Ver Top 5 Misiones con Mayor Recompensa")
        print("4. Ver Aventureros por Tipo (Guerrero, Mago, Ranger)")
        print("5. Volver al Menú Principal")

        opcion = input("Elija una opción: ")
        if opcion == "1":
            gremio.top_10_misiones_resueltas()
        elif opcion == "2":
            gremio.top_10_habilidad()
        elif opcion == "3":
            gremio.top_5_misiones_recompensa()
        elif opcion == "4":
            gremio.aventureros_por_clase()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, elija una opción del submenú.")


if __name__ == "__main__":

    bienvenida()
    menu_principal()
