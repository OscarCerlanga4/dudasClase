class monton():
 
    __stuff = ""
    
    def __init__(self, *args):
        self.__stuff = ",".join(args)
        pass

    def __str__(self)-> str:
        return self.__stuff
    
    def amontona(self, algo):
        if isinstance(algo, monton):
            if self.__stuff: 
                self.__stuff += "," + algo.__stuff
                print(algo)
            else:
                self.__stuff = algo.__stuff
        else:
            palabra = str(algo)
            if self.__stuff:
                self.__stuff += "," + palabra
                print(palabra)
            else:
                self.__stuff = palabra
                
        
    def contiene(self, algo) -> bool:
        palabra = str(algo)
        numero_perlas = self.__stuff.count(palabra)
        if numero_perlas >= 1:
            print(numero_perlas)
            return True
        else:
            print("No hay perlas")
            return False

    def copiar(self, algo) -> object:
        """doc..."""
        return "Foo" # pass

    def tomar(self, algo) -> object:
        palabra = str(algo)
        num_perlas = 0
        if palabra in self.__stuff:
            num_perlas = self.__stuff.count(palabra)
            self.__stuff = self.__stuff.replace(palabra, '', num_perlas)
            self.__stuff = self.__stuff.replace(",,", ',', num_perlas)
            print(num_perlas)
            return palabra
        else:
            print("No hay perlas, por lo tanto no hemos sacado ninguna")
        return None

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print(m0)

    m1 = monton("algo")  # m0 es un nuevo monton con "algo"
    m1.amontona("algo mas")
    # assert: en m1 hay "algo" y "algo mas" y NADA MAS.

    exit(0) # ==ir bajando...===========================

    m1.amontona("perla")
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...

    # puedo amontonar -todo lo que haya- en un monton 
    # en otro moton.
    # Esto no vacia el monton argumentado (m1 aqui)
    # Esto no vacia previamente el monton invocado (m0 aqui)
    # no ~ m0 = m1
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    copia = m0.copiar("perla") # copia == "perla"
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"