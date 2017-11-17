#-*-coding: utf-8 -*-
def suma (a,b):
	resultado = a+b
	return resultado
	
def resta (a,b):
	resultado = a-b
	return resultado
	
def multi (a,b):
	resultado = a*b
	return resultado 
	
def divi (a,b):
	resultado = a/b
	return resultado
global resultado
resultado = 0

operacion = raw_input("Que operación desea realizar (S,R,M,D): ")

a = int(input("Que valor vols utilitzar en la operació? "))
b = int(input("Que segon valor vols utilitzar en la operació? "))

if operacion == "S":
	resultado=suma(a,b)
	print "La suma da ", resultado
	
if operacion == "R":
	resultado=resta(a,b)
	print "La resta da ", resultado
	
if operacion == "M":
	resultado=multi(a,b)
	print "La multiplicación da ", resultado
	
if operacion == "D":
	resultado=divi(a,b)
	print "La división da ", resultado




