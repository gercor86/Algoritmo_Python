"""Se necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales N1, N2, N3"""

#Los promedio de la notas

print("-"*50)

print("Programa promedio")

print("-"*50)

print("Ingrese la notas de los alumnos N1, N2 y N3.")

N1 = float(input("N1: "))
N2 = float(input("N2: "))
N3 = float(input("N3: "))

P = float((N1 + N2 + N3)/3)

print("\nTotal de la nota final.")

print(P)