pares = 0
impares = 0
soma_total = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}o número: "))
    soma_total = soma_total + numero
    
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Soma total: {soma_total}")