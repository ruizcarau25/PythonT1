objetivo = int(input("Introduce el número objetivo: "))

numeros = []
suma_actual = 0

while suma_actual != objetivo:
    num = int(input("Introduce un número entero: "))
    numeros.append(num)
    suma_actual += num
    
    if suma_actual > objetivo:
        print(f"Suma actual ({suma_actual}) superó el objetivo ({objetivo}). Reiniciando intento o continúa ingresando...")

print(f"\n¡Conseguido! La suma alcanza exactamente {objetivo}.")
print("Lista de números introducidos:", numeros)