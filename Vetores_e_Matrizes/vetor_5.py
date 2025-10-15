numeros = []

for i in range(1, 8):
    numero = int(input(f"Digite o {i}o número: "))
    numeros.append(numero)

lista_invertida = numeros[::-1]

print(f"Lista original: {numeros}")
print(f"Lista invertida: {lista_invertida}")