# Este es mi primer programa en Python
# Autor: ______________________
# Objetivo: saludar al usuario y mostrar su edad el próximo año

print("¡Hola, mundo!") # Mensaje en pantalla

nombre = input("¿Cómo te llamas? ") # Pedir un dato (string)
edad = input("¿Cuántos años tienes? ")

# input siempre devuelve texto; si necesito operar con números convierto:
edad = int(edad)

print() # Línea en blanco
print("Encantado de conocerte,", nombre)
print("El año que viene tendrás", edad + 1, "años.") 