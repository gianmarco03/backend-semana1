"""
Incorporar un menu de opciones para el programa monedas que tenga 3 opciones 1 - convertir de soles a dolares 2 - convertir de dolares a soles 3 - salir , y que se ejecute con un ciclo while mientras la opción no sea salir, si selecciono la opción salir debe terminar el programa
enviar por retos el ejercicios desarrollado
"""
#PROGRAMA PARA CONVERTIR MONEDAS
#VERSIÓN 1.0

opcion = 0

while(opcion != 0):
    print(
    """
    OPCIÓN 1 : convertir de soles a dolares
    OPCIÓN 2 : convertir de dolares a soles
    OPCIÓN 3 : Salir del Programa
    """)
    opcion = int(input("ingrese la opción que desea: "))
    if(opcion == 1):
        pass
    elif(opcion == 2):
        pass
    elif(opcion == 3):
        print("ADIOS!")
    else:
        print("Debe marcar una opción valida")


#ENTRADAS
#PROCESO
#SALIDA