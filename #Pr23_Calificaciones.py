#Pr23_Calificaciones
#Autor: Alexannder Escobar Ruiz

Nombre = input("Ingrese su nombre ")
SM = 0 
for i in range(3): 
    calificaciones = float (input("Ingresa tu calificacion"))
    SM = SM + calificaciones
    Promedio = SM /3  
    print (Nombre,"Tu promedio es de",Promedio)
    if Promedio >= 6 : 
        print (Nombre,"Tu aprobaste") 
    else: 
        print (Nombre,"Tu reprobaste")   