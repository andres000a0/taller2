from Escuderia import Escuderia

escuderias = [];

numeroEscuderias = int(input("Número de escuderias:"));

contador = 1;
while contador <= numeroEscuderias:
    escuderia = Escuderia();
    escuderia.nombre = input("Nombre de la escuderia:")
    escuderia.casaMotor = input("Casamotor de la escuderia:")
    escuderia.pilotoPrincipal.nombre = input("Digite el nombre del piloto")
    escuderia.pilotoPrincipal.salarioAnual = input("Digite el salario del piloto");
    escuderia.pilotoPrincipal.pais = input("Digite el salario del piloto");
    escuderia.piloto2.nombre = input("Digite el nombre del piloto")
    escuderia.piloto2.salarioAnual = input("Digite el salario del piloto");
    escuderia.piloto2.pais = input("Digite el salario del piloto");
    escuderias.append(escuderia)

costoMayor = 0;
nombreEscuderiaMayorCosto = '';
salarioMayor = 0;
pilotoMayorPagado = '';
for escuderia in escuderias:
    print(f"nombre: {escuderia.nombre}, costo: {escuderia.costos}");
    if(escuderia.costos > costoMayor):
        costoMayor = escuderia.costos;
        nombreEscuderiaMayorCosto = escuderia.nombre;
    if(escuderia.pilotoPrincipal.salarioAnual > salarioMayor):
        salarioMayor = escuderia.pilotoPrincipal.salarioAnual
        pilotoMayorPagado = escuderia.pilotoPrincipal.nombre;

print(f"Escuderia mas cara: {nombreEscuderiaMayorCosto} con costo de ${costoMayor}");
print(f"Piloto mas bien pagado: {pilotoMayorPagado} con salario de ${salarioMayor}");