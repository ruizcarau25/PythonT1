import random

numero_secreto = random.randint(0, 10)
intentos = 3
adivinado = False

print("¡Bienvenido! He pensado un número entre 0 y 10. Tienes 3 intentos.")

while intentos > 0 and not adivinado:
    intento = int(input(f"\nTe quedan {intentos} intentos. Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
        
    intentos -= 1

if not adivinado:
    print(f"\nSe te acabaron los intentos. El número era {numero_secreto}.")