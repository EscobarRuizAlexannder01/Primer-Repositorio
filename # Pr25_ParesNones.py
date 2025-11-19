# Pr25_ParesNones  
# Autor: Alexannder Escobar Ruiz

N = int(input("Ingresa hasta que numero quieres que llegue"))
X = int(input("Ingresa hasta que numero quieres que llegue"))

print("Los numero van a ir subiendo de 2 en 2 ya que son pares",N)
for i in range (2, N+1, 2 ) : 
    print(i)

print("Los numero van a ir subiendo de 1 en 1 ya que son Nones",X )
for i in range(1, X+1, 2) :
    print(i)
    