#Pr24_Descuento
#Autor Alexannder Escobar Ruiz 
i = 0 
Total = 0 

while i <= 4 : 
    Art = float (input("Ingresa el precio del articulo"))
    Total = Art + Art 
    i = Total + Art + Art 
     
    if (i>500):
        Desc = i * 0.05
        Resul_F = i - Desc  
        print ("El precio a pagar es de",Resul_F)

    else : 
        print ("No revasa la cantidad deseada no resivira descuento, el resultado de su compra es de", i )