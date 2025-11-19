#Pr13_Comparar
#Autor:Alexannder Escobar Ruiz 

Pri_Numero = int(input("Escriba el primer numero"))
Seg_Numero = int(input("Escrine el segundo numero"))

if Pri_Numero == Seg_Numero:
    Result = Pri_Numero*Seg_Numero
    print("Sus numeros fueron iguales por lo tanto se multiplicaron y el resultado es",Result)

elif Pri_Numero > Seg_Numero: 
    Result = Pri_Numero-Seg_Numero 
    print("Su primer numero es mayor que el primero, por lo tanto se restan y el resulado de su resta es",Result)

elif Pri_Numero < Seg_Numero: 
     Result = Pri_Numero+Seg_Numero
     print("Su primer numero es menor que el segundo, por lo tanto se suma y el resultado de su suma es",Result)