#Pr16_Descuento
#Autor: Alexannder Escobar Ruiz

Pri_Compra = int(input("Escribe el precio del producto")) 
Seg_Compra = int(input("Ingresa el precio del producto"))

Result = Pri_Compra + Seg_Compra 
if Result >= 500 : 
    Result = Pri_Compra + Seg_Compra * 0.15
    print ("El monto de la compra revasa los 500 asi que se le aplicara un descuento del 15 porciento, el monto final es de",Result)

elif Result<500 : 
    Result = Pri_Compra + Seg_Compra * 0.02
    print("El monton de la compra es menor de 500 asi que solo se aplicara el 2 por ciento de descunto, el monton a pagar es",Result)    