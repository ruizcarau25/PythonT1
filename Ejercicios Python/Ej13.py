def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso:
numero = 3
print(f"El factorial de {numero} es {factorial(numero)}")  # Imprime: 6