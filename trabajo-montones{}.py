class Monton():
    
    __stuff = {}  # Diccionario vacío en lugar de lista
    
    def __init__(self, *algo):
        # Almacenamos los elementos pasados al monton en el diccionario.
        self.__stuff = {}
        for item in algo:
            self.amontona(item)

    def __str__(self) -> str:
        # Representamos el monton como un diccionario.
        return f"{self.__stuff}"

    def amontona(self, algo):
        # Si 'algo' es un objeto de tipo Monton, agregamos sus elementos.
        if isinstance(algo, Monton):
            for item in algo.__stuff:
                self.__stuff[item] = self.__stuff.get(item, 0) + algo.__stuff[item]
        else:
            # Si es un solo objeto, lo agregamos con un contador.
            self.__stuff[algo] = self.__stuff.get(algo, 0) + 1

    def contiene(self, algo) -> bool:
        # Verificamos si 'algo' está en el diccionario.
        return algo in self.__stuff

    def copiar(self, algo) -> object:
        # Si el objeto existe, lo devolvemos (solo devolvemos el valor).
        if algo in self.__stuff:
            return algo
        return None

    def tomar(self, algo) -> object:
        # Intentamos eliminar el objeto del diccionario y devolverlo.
        if algo in self.__stuff:
            del self.__stuff[algo]
            return algo
        return None


if __name__ == "__main__":
    
    m0 = Monton()        # m0 es un nuevo monton vacío
    print(f"este es el contenido del monton m0: {m0}")
    
    m1 = Monton("algo")  # m1 es un nuevo monton con "algo"
    print(f"este es el contenido del monton m1 ahora: {m1}")
    
    m1.amontona("algo más")
    print(f"este es el contenido del monton m1 ahora: {m1}")  # Esperamos que imprima algo como {'algo': 1, 'algo más': 1}

    # Ahora agregamos más elementos
    m1.amontona("perla")
    print(f"este es el contenido del monton m1 ahora: {m1}")  # Esperamos que imprima {'algo': 1, 'algo más': 1, 'perla': 1}
    
    m1.amontona("mas mierdas")
    print(f"este es el contenido del monton m1 ahora: {m1}")
    
    m0.amontona(m1)
    print(f"este es el contenido del monton m0 ahora: {m0}, y del m1: {m1}")
    
    predicado = m0.contiene("perla") # predicado == True
    print(f"¿m0 tiene perla? {predicado}")
    
    copia = m0.copiar("perla") # copia == "perla"
    print(f"la cojo de mi monton m0, ({copia})")
    
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
    print(f"saco ({copia}), y el contenido de mi monto m0 es: {m0}")
