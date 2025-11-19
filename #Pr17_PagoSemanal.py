#Pr17_PagoSemanal
#Autor: Alexannder Escobar Ruiz 

D = int(input("Ingresa los dias trabajados"))
Sueldo_Diario = int(input("Ingresa el sueldo diario"))
Sueldo_Semanal = 0 
Sueldo_Final = 0 
Sueldo_Semanal = D * Sueldo_Diario

if (D > 5 ): 
    Sueldo_Final = Sueldo_Semanal+100
    print(" Su desempeño ha sido bueno y por los dias de trabajo le hemos un poco extra, su sueldo es de", Sueldo_Final)

elif (D < 5 ):
    Sueldo_Final=Sueldo_Semanal  
    print(" Su desempeño fue bueno pero no suficiente, debido a eso no obtendra el monton extra, su sueldo es de",Sueldo_Final)
