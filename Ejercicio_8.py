"""Construya un diagrama de flujo tal que, dado como datos la base
y la altura de un rectángulo, calcule el perímetro y la superficie
de este."""

print("-"*50)

print("Calculo de perimetro y superficie de un rectangulo")

print("-"*50)

print("Ingrese la base y el alto: ")

BASE = float(input("Base: "))

ALTO = float(input("Alto: "))

SUP = BASE * ALTO

PER = 2*(BASE + ALTO)

print("\nResultado")

print("-"*50)

print("Superficie:", SUP)

print("Perimetro:", PER)