a = int(input("Digite el numero 1: "))
b = int(input("Digite el numero 2: "))

print("""
==========

Bienvenido a mi calculadora... 

Ingrese 1 para una suma.
Ingrese 2 para resta.
Ingrese 3 para Multiplicacion
------
Para salir oprima 0

===========

""")
opc = 10

while opc != 0:
    opc = int(input("Digite su opcion: "))
    if opc == 1:
        resultado = a + b 
    elif opc == 2:
        resultado = a - b 
    else: 
        resultado = a * b
    
    print(f"Su resultado fue: {resultado}")

