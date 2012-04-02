#!/usr/bin/python
#Autor: Jesus Fabian Cubas <jfabian@computer.org>

#listas
l = [22, True, "lista uno", [1, 2]]
print type(l)
print l
print l[0]
l[3] = [2, 3 , 4]
print l
print l[0:3]

#tuplas
t = 1, 2, 3
print type(t)

#diccionario
d = {"arriba" : "abajo", "izquierda": "derecha", "encima":"debajo"}
print type(d)
print d["arriba"]
