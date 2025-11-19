#Pr21_Banco
#Autor: Alexannder Escobar Ruiz 

Efectivo = int(input("Ingrese el cheque dentro de la maquina porfavor"))

ML=int(Efectivo/1000)
res = (Efectivo%1000) 

QT = int(res/500)
Resul = (res%500)

DC = int (Resul/200)
Res = (Resul%200)

CE = int (Res/100)
REs = (Res%100)

CU = int (REs/50)
ReZ = (REs%50)

VT = int (ReZ/20)
Rez = (ReZ%20)

DS = int (Rez/10)
Resultado = (Rez%10)

CO = int (Resultado/5)
Re = (Resultado%5)

DS = int (Re/2)
R = (Re&2)

PS = int (R/1)
RE = (R%1)

print("Los billetes de MIl seran de",ML )
print("Los billetes de Quinientos seran de",QT )
print("Los billetes de Docientos seran de",DC )
print("Los billetes de Cien seran de",CE )
print("Los billetes de Cincuenta seran de",CU )
print("Los billetes de Veinte seran de",VT )
print("Las Monedas de Dies seran de ",DS )
print("Los Monedas de Cinco seran de",CO )
print("Los Monedas de Dos pesos seran de",DS )
print("Los Monedas de Pesos  seran de",PS )