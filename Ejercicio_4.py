"""Elaborar un algoritmo que permita ingresar el número de
partidos ganados, perdidos y empatados, por ABC club en el
torneo apertura, se debe de mostrar su puntaje total,
teniendo en cuenta que por cada partido ganado obtendrá 3
puntos, empatado 1 punto y perdido 0 puntos."""

print("-"*50)

print("Puntaje de partidos")

print("-"*50)

print("Ingrese la cantidad de partidos ganados")

PG = int(input())

print("Ingrese la cantidad de partidos empatados")

PE = int(input())

print("Ingrese la cantidad de partidos perdidos")

PP = int(input())

PPG = PG*3

PPE = PE*1

PPP = PP*0

PF = PPG + PPE + PPP

print("\nResultado")

print("-"*50)

print("El total de puntos es de", PF)