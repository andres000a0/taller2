from Piloto import Piloto
class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__casaMotor = None
        self.__pilotoPrincipal = Piloto();
        self.__piloto2 = Piloto();
        self.__costos = None
        
    
    @property
    def nombre(self):
        return self.__nombre;
    
    @property
    def casaMotor(self):
        return self.__casaMotor;
    
    @property
    def pilotoPrincipal(self):
        return self.__pilotoPrincipal;
    
    @property
    def piloto2(self):
        return self.__piloto2;
    
    @property
    def costos(self):
        return self.__costos;
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @casaMotor.setter
    def casaMotor(self,casaMotor):
        self.__casaMotor = casaMotor
    
    @pilotoPrincipal.setter
    def pilotoPrincipal(self,pilotoPrincipal):
        self.__pilotoPrincipal = pilotoPrincipal
    
    @piloto2.setter
    def piloto2(self,piloto2):
        self.__piloto2 = piloto2
    
    @costos.setter
    def costos(self,costos):
        self.__costos = costos
        