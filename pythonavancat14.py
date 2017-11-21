#-*-coding: utf-8 -*-

def crealista(lista):
	cantidad = int(input("Que numeros vols que es sumen? "))
	if cantidad < 0:
		print "Es imposible!"
	else:
		for i in range(cantidad):
			num = int(input("Introdueix un numero "))
			lista+=[num]
		print lista
		return
def promediolista(lista):
		suma = 0
		for i in (lista):
			suma+=i
		promedio= suma/len(lista)
		print promedio
		return
			
lista = []
crealista(lista)
promediolista(lista)

