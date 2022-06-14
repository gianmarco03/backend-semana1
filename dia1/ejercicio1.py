"""
Ejercicio 01:
Ingrese un texto y un divisor y luego muestre el mismo texto pero dividido por el divisor
EJEMPLO:
INGRESO
TEXTO = ABCDEFG
DIVISOR=2
RESULTADO:
AB
CD
EF
G
"""

#ENTRADA
texto = input("Ingrese el texto : ")
divisor = int(input("Ingrese divisor: "))
#PROCESO
for contador in range(0, len(texto), divisor):
#SALIDA
    print(texto[contador:divisor+contador])