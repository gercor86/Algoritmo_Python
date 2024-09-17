"""Elaborar un algoritmo que permita calcular el número de micro
discos 3 .5 necesarios para hacer una copia de seguridad, de la
información almacenada en un disco cuya capacidad se conoce.
Hay que considerar que el disco duro está lleno de información,
además expresado en gigabyte. Un micro disco tiene 1.44
megabyte y un gigabyte es igual a 1,024 megabyte."""

import math

print("-"*50)

print("Numero de disketes de 1.44Mb")

print("Ingrese la cantidad de GB")

GB = float(input())

MG = GB*1024

MD = MG/1.44

print("\nResultado de disketes")

print("-"*50)

print(MD)

print("La catidad de disketes necesario son:", math.ceil(MD))