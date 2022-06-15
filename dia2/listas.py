dias = ["lunes","martes","miercoles"]
print(dias)
print(dias[1])
dias.append("miercoles")
print(dias)
dias.pop()
print(dias)
dias[0]="domingo"
print(dias)

for dia in dias:
    #print("Hoy es " + dia)
    print(dia,end=" ")

alumnos = []
totalAlumnos = int(input("Ingrese el numero de alumnos a registrar:"))
for contador in range(totalAlumnos):
    nuevoAlumno=input("Nombre del alumno " + str(contador)+ " : ")
    alumnos.append(nuevoAlumno)
print("Relación de alumnos : ")
for alumno in alumnos:
    print(alumno,end= " | ")