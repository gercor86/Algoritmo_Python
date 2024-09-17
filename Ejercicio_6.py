"""Se tiene los puntos A y B en el cuadrante positivo
del plano cartesiano, elabore el algoritmo que permita obtener
la distancia entre A y B."""

print("-"*50)

print("Distancia entre dos puntos")

print("Ingrese las coordenadas del Punto A")

AX = float(input("Ax: "))

AY = float(input("Ay: "))

print("Ingrese las coordenadas del Punto B")

BX = float(input("Bx: "))

BY = float(input("By: "))

D = ((AX-BX)**2 + (AY + BY)**2)**0.5

print("\nResultado")

print("-"*50)

print("La distancia entre los puntos es de:", D)