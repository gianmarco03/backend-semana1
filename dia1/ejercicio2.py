"""
Incorporar un menu de opciones para el programa monedas que tenga 3 opciones 1 - convertir de soles a dolares 2 - convertir de dolares a soles 3 - salir , y que se ejecute con un ciclo while mientras la opción no sea salir, si selecciono la opción salir debe terminar el programa
enviar por retos el ejercicios desarrollado
"""
#ENTRADA
montoOrigen = input ("Ingrese el monto: ")
montoDestino=0
#PROCESO
while True:
    print ("INGRESE LA OPCIÓN A CONVERTIR")
    print ("1. soles a dolares")
    print ("2. dolares a soles")
    print ("3. Salir")
    opcion=input()

    if(opcion=="1"):
        montoDestino = float(montoOrigen)/3.778
        print ("El monto en dolares es: " + str(montoDestino))
    elif(opcion=="2"):
        montoDestino=float(montoOrigen)*3.778
        print ("El monto en soles es: " + str(montoDestino))
    elif(opcion=="3"):
        print ("Gracias por usar el Sistema")
        break
