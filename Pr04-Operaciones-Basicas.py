#3-B Programacion Matutino
#Autor: Alexannder Escobar Ruiz 
 
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
res = 0 
print("\n")
print("Menu")
print("1.sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5: Salir")

opcion = input("Elije una opcion:")
if opcion == "1":
    res = numero1+numero2
    print("El resultado de la Suma es:",res)
elif opcion == "2":
    res = numero1-numero2
    print("El resultado de la Resta es",res)
elif opcion == "3": 
    res = numero1*numero2
    print("El resultado de la Multiplicacion es",res)
elif opcion == "4":
    res = numero1/numero2 
    print("El resultado de la Division es ",res) 
