from abc import ABC, abstractmethod

class IColeccion(ABC):
    @abstractmethod
    def insertarElemento(self, elemento, posicion):
        pass

    @abstractmethod
    def agregarElemento(self, elemento):
        pass

class Coleccion(IColeccion):
    __listaE: list

    def __init__(self):
        self.__listaE = []

    def insertarElemento(self, elemento, posicion):
        if posicion <= 0 and posicion > len(self.__listaE):
            raise Exception ("Error, posicion invalida")
        self.__listaE.insert(posicion, elemento)
    
    def agregarElemento(self, elemento):
        self.__listaE.append(elemento)

    def mostrarElemento(self, posicion):
        if posicion <= 0 and posicion > len(self.__listaE):
            raise Exception("Error, posicion invalida")
        print(self.__listaE[posicion])
        