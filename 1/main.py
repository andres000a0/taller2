from Coctel import Coctel
contador = 1;
coctel = Coctel
coctel.nombre = input("Nombre del coctel: ");
coctel.precio = int(input("Precio: "));
cantidad = int(input("Cantidad: "));
coctel.grado_alcohol = float(input("Grado de alcohol: "));

def calcularCostoShot():
    return cantidad*coctel.precio;

def calcularCostoJugo(añejamiento):
    costo = 0;
    if(añejamiento == 1):
        costo = cantidad*coctel.precio;
    elif(añejamiento == 2):
        costo = cantidad*coctel.precio - (cantidad*coctel.precio * 0.2);
    elif(añejamiento == 3):
        costo = cantidad*coctel.precio - (cantidad*coctel.precio * 0.5);
    elif(añejamiento == 4):
        costo = 0;
    return costo;
        




opcionValida = False

while(opcionValida == False):
    print("=========================================")
    print("Tipo del coctel: ")
    print("1. Coctel con jugo de frutas.")
    print("2. Shot de alcohol.")
    print("=========================================")
    tipoCoctel = int(input("=>"));

    if(tipoCoctel == 1):
        añejamiento = int(input("Añejamiento: "));
        coctel.grado_frescura = int(input("Grado de frescura: "));
        print(f"Costo de venta: ${calcularCostoJugo(añejamiento)}")
        opcionValida = True

    elif(tipoCoctel == 2):
        coctel.temperatura = int(input("Temperatura:"));
        print(f"Costo de venta: ${calcularCostoShot()}")
        opcionValida = True



            


    




