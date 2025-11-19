#Pr19_IMC
#Autor: Alexannder Escobar Ruiz 

Nombre = (input("Cual es tu Nombre"))
Peso = int(input("Ingresa tu peso"))
Estatura = float(input("Ingresa tu estratura"))
IMC = 0 
IMC = Peso/(Estatura*Estatura)

if (IMC < 18): 
    print("Tu IMC es de " , IMC , "Por lo tanto tienes Anorexia")

elif (IMC>=18 and IMC< 20):
    print("Tu IMC es de " , IMC , "Por lo tanto estas delgado")

elif(IMC >=20 and IMC < 27):
    print("Tu IMC es de " , IMC , " Por lo tanto estas normal ")

elif(IMC >= 27 and IMC < 30): 
    print("Tu IMC es de " , IMC , " Por lo tanto tienes obesidad grado 1")

elif(IMC >=30 and IMC <35 ):
    print("Tu IMC es de " , IMC , " Por lo tanto tienes obesidad grado 2")

elif (IMC >= 35 and IMC < 40): 
    print ("Tu IMC es de " , IMC , "Por lo tanto tienes obesidad grado 3")

elif (IMC>40): 
    print ("Tu IMC es de ", IMC , "Por lo tanto tienes obesidad morbida ") 