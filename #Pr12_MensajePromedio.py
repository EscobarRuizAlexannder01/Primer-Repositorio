#Pr12_MensajePromedio
#Autor:Alexannder Escobar Ruiz

Nombre = (input("Escribe el nombre del alumno"))
Califiacion1 = int(input("Escibre tu Promedio"))
Califiacion2 = int(input("Escribe tu Pronedio"))
Califiacion3 = int(input("Escribe tu Promedio"))

Promdeio_Final = (Califiacion1+Califiacion2+Califiacion3)/3
print ("Tu Promedio final es",Promdeio_Final)
if Promdeio_Final>=6: 
    print("Aprobaste")
else: print("Reprobaste")