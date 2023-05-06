class Piloto:
    def __init__(self):
        self.__nombre= None
        self.__fechaNacimiento= None
        self.__salarioAnual= None
        self.__pais= None
        
        @property
        def nombre(self):
            return self.__nombre;
        
        @property
        def fechaNacimiento(self):
            return self.__fechaNacimiento;
        
        @property
        def salarioAnual(self):
            return self.__salarioAnual;
        
        @property
        def pais(self):
            return self.__pais;
        
        @nombre.setter 
        def nombre(self,nombre):
            self.__nombre = nombre;
            
        @fechaNacimiento.setter 
        def nombre(self,fechaNacimiento):
            self.fechaNacimiento = fechaNacimiento;
            
        @salarioAnual.setter 
        def nombre(self,salarioAnual):
            self.salarioAnual = salarioAnual;
            
        @pais.setter 
        def nombre(self,pais):
            self.pais = pais