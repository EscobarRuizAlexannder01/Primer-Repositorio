#Pr18_Descuento2
#Autor: Alexannder Escobar Ruiz

Producto_1 = int (input ("Ingresa el precio del producto"))
Producto_2 = int (input ("Ingresa el precio del segundo producto"))
Producto_3 = int (input ("Ingresa el precio del tercer producto"))
Result = 0    
Desc = 0 
Result_Final = 0
Result = Producto_1 + Producto_2 + Producto_3

if (Result < 1000 ): 
    Desc = Result * 0.5 
    Result_Final = Result - Desc 
    print (" Su compra fue un monto de menos de 1000 por lo tanto se le dara un descuento de 5 porciento, el resultado de su monton es", Result_Final)

elif (Result >= 1000 and Result < 2500) : 
    Desc = Result * 0.10 
    Result_Final = Result - Desc 
    print ("Su compra revaso el monto de 1000 pero no de 2500 por lo tanto solo se le aplicara un 10 porciento de descuento, el monton a pagar es de",Result_Final)

elif (Result >= 2500) : 
    Desc = Result * 0.20 
    Result_Final = Result - Desc  
    print (" Su compra revaso los 2500 por lo tanto se le apliara un descuento del 20 porciento, el total a pagar es de", Result_Final)
