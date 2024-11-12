from gremio import Gremio
from exceptions import InformacionInvalida

def bienvenida():
    titulo = 'Bienvenido al Simulador de Gremio de Aventureros!'
    len_titulo = len(titulo) + 4
    print('*'*len_titulo)
    print('* '+titulo+' *')
    print('*'*len_titulo)

def menu_principal():
    gremio = Gremio()
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar Aventurero")
        print("2. Registrar Misión")
        print("3. Realizar Misión")
        print("4. Otras Consultas")
        print("5. Salir\n")
        
        opcion = input("Ingresar Opcion: ")

        if opcion == '1':
        
            try:
                clase = input('\nElija la clase del aventurero:\n1. Guerrero\n2. Mago\n3. Ranger\nInrgese numero de opcion: ')
                clase = int(clase)
                if clase not in [1,2,3]:
                    raise InformacionInvalida

                nombre = input('Ingrese el nombre del aventurero: ')

                id = input('Ingresar el ID: ')
                id = int(id)
                
                ptos_habilidad = input('Ingrese puntos de habilidad (0-100): ')
                ptos_habilidad = int(ptos_habilidad)
                if  ptos_habilidad < 0 or ptos_habilidad > 100:
                    raise InformacionInvalida
                
                experiencia = input('Ingrese Experiencia del aventurero: ')
                experiencia = int(experiencia)
                
                dinero = input ('Ingresar Dinero del aventurero: ')
                dinero = float(dinero)

                nombre_mascota = None
                habilidad_mascota = None
                adicional = None

                match clase:
                    case 1:
                        adicional = input('Ingresar Fuerza (0-100): ')
                        adicional = int(adicional)
                        if adicional < 0 or adicional > 100:
                            raise InformacionInvalida
                    
                    case 2:
                        adicional = input('Ingresar mana (0-100): ')
                        adicional = int(adicional)
                        if adicional < 0 or adicional > 100:
                            raise InformacionInvalida
                    
                    case 3:
                        adicional = None
                        tiene_mascota = input('Agregar una mascota? (S/N): ')
                        tiene_mascota.upper()
                        if tiene_mascota == 'S':
                            nombre_mascota = input('Ingresar Nombre de la mascota: ')
                            habilidad_mascota = input('ingresar Puntos de habilidad de la mascota: ')
                        elif tiene_mascota != 'N':
                            raise InformacionInvalida



                gremio.registrar_aventurero(clase,nombre,id,ptos_habilidad,experiencia,dinero,adicional,nombre_mascota,habilidad_mascota)
                print('\nAventurero registrado!\n')
                for aventureros in gremio.aventureros:
                    print(aventureros.id)
                
                        
            except InformacionInvalida as e:                    
                print(f"*** Error: {e}*** ")
                
            
        elif opcion == '2':
            try:
                
                nombre = input('Ingresar Nombre: ')
                rango = input('Ingresar Rango: ')
                rango = int(rango)
                if rango not in [1,2,3,4,5]:
                    raise InformacionInvalida
                recompensa = input('Ingresar Recompensa: ')
                recompensa = float(recompensa)
                mision_grupal = input('La mision es Grupal? (S/N): ')
                mision_grupal = mision_grupal.upper()
                if mision_grupal == 'S':
                    min_miembros = input('Ingresar cantidad minima de miembros: ')
                    min_miembros = int(min_miembros)
                elif mision_grupal == 'N':
                    min_miembros = 1 
                else:
                    raise InformacionInvalida

                gremio.registrar_mision(nombre,rango,recompensa,min_miembros)
                for misiones in gremio.misiones:
                    print(misiones.nombre)
                    
            except InformacionInvalida as e:                    
                print(f"*** Error: {e}*** ")

        elif opcion == '3':
            gremio.realizar_mision()
        elif opcion == '4':
            submenu_consultas(gremio)
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, elija una opción del menú.")

# Submenú para consultas
def submenu_consultas(gremio):
    while True:
        print("\nSeleccione una opción de consulta:")
        print("1. Ver Top 10 Aventureros con Más Misiones Resueltas")
        print("2. Ver Top 10 Aventureros con Mayor Habilidad")
        print("3. Ver Top 5 Misiones con Mayor Recompensa")
        print("4. Ver Aventureros por Tipo (Guerrero, Mago, Ranger)")
        print("5. Volver al Menú Principal")
        
        opcion = input("Elija una opción: ")

        if opcion == '1':
            gremio.ver_top_10_aventureros_misiones()
        elif opcion == '2':
            gremio.ver_top_10_aventureros_habilidad()
        elif opcion == '3':
            gremio.ver_top_5_misiones_recompensa()
        elif opcion == '4':
            gremio.ver_aventureros_por_tipo()
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, elija una opción del submenú.")






if __name__ == "__main__":
    
    bienvenida()
    menu_principal()

   
    
   