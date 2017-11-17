#-*-coding: utf-8 -*-º
def rectangle (x,y,caracter):
	for i in range (x):
		for j in range (y):
			print caracter,
		print " "

altura = int(input("Introdueix la amplaria del rectangle "))
amplaria = int(input("Introdueix l'altura del rectangle "))
caracter = raw_input("Introdueix el dibuix que vols que tinga el rectangle ")
rectangle (amplaria,altura,caracter)
