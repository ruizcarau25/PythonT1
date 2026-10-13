palabras = []

while True:
    palabra = input("Introduce una palabra (o presiona Enter para terminar): ")
    if palabra == "":
        break
    palabras.append(palabra)

print("\nListado de palabras introducidas:")
for p in palabras:
    print(p)