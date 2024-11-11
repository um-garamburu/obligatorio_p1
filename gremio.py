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

    def registrar_mision(self, nombre: str, rango: int, recompensa: float, min_miembros: int = 1):
        for mision in self.__misiones:
            if mision.nombre == nombre:
                raise InformacionInvalida()

        if min_miembros == 1:
            nueva_mision = MisionIndividual(nombre=nombre, rango=rango, recompensa=recompensa, completado=False)
            self.__misiones.append(nueva_mision)
        else:
            nueva_mision = MisionGrupal(nombre=nombre,rango=rango,recompensa=recompensa,miembros=min_miembros,completado=False)
            self.__misiones.append(nueva_mision)

    def realizar_mision(self,mision: object, aventureros:list):
        
        if len(aventureros) == 1:
            habilidad = aventureros[0].habilidad_total
            nivel = 0

            if habilidad <= 20:
                nivel = 1
            elif habilidad <= 40:
                nivel = 2
            elif habilidad <= 60:
                nivel = 3
            elif habilidad <= 80:
                nivel = 4 
            else:
                nivel = 5
            
            if nivel >= mision.rango:
                mision.completado(True)
                aventureros[0].ptos_habilidad += mision.recompensa
             

        
        

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
        gremio.registrar_mision('mision1',3,100,5)
        gremio.registrar_mision('mision2',3,100)
        gremio.registrar_aventurero(1,'av1',1,24,10,0)

    except InformacionInvalida as e:
        print(f"Error: {e}")

    for mision in gremio.misiones:
        print(mision.nombre)
    
    for aventurero in gremio.aventureros:
        print(aventurero.nombre)


