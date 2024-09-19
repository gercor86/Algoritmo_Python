"""Construya un diagrama de flujo (DF) que resuelva un problema
que tiene una gasolinera. Los dispensadores de esta registran lo
que “surten” en galones, pero el precio de la gasolina está fijado
en litros. El DF debe calcular e imprimir lo que hay que cobrarle
al cliente."""

print("-"*50)

print("Estacion de Servicio")

print("-"*50)

consu = float(input("Ingrese el consumo:"))

LITXG = 1.500

PRECIOXL = 75.50

total = consu * LITXG * PRECIOXL

print("\n Resultado")

print("-"*50)

print("El total del importes es de:", total)