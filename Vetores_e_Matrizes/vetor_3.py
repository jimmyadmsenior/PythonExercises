numeros = []
pares = []
impares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}o número: "))
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Todos os números: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")