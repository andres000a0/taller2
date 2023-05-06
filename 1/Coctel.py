class Coctel:
    def __init__(self):
        self.__nombre = None
        self.__precio = None
        self.__grado_alcohol = None
        self.__temperatura = None
        self.__grado_frescura = None
    @property
    def nombre(self):
        return self.__nombre;
    
    @property
    def precio(self):
        return self.__precio;
    
    @property
    def grado_alcohol(self):
        return self.__grado_alcohol;
    
    @property
    def temperatura(self):
        return self.__temperatura;
    @property
    def grado_frescura(self):
        return self.__grado_frescura;
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
    
    @grado_alcohol.setter
    def grado_alcohol(self,grado_alcohol):
        self.__grado_alcohol = grado_alcohol
    @grado_alcohol.setter
    def temperatura(self,temperatura):
        self.__temperatura = temperatura
        
    @grado_alcohol.setter
    def temperatura(self,grado_frescura):
        self.__grado_frescura = grado_frescura