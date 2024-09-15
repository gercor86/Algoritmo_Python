"""Se necesita un algoritmo que solicite el numero de respuestas correctas, incorrectas y en blanco,
correspondientes a postulantes, y muestre su puntaje final considerando que por cada respuesta 
correcta tendra 3 puntos, por respuestas incorrectas tendra -1 y respuesta en blanco 0."""

print("-"*50)

print("Obtener el puntaje final")

print("-"*50)

print("Ingrese el numero de respuestas correctas: ")

RC = int(input())

print("Ingrese el numero de respuestas inconrrectas: ")

RI = int(input())

print("Ingrese el numero de respuestas en blanco: ")

RB = int(input())

PCR = RC*3

PRI = RI*-1

PRB = RB*0

PF = PCR + PRI + PRB

print("El total de puntaje es:", PF)
