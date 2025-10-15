maior = None
menor = None

for i in range(1, 6):
    numero = int(input(f"Digite o {i}o número: "))
    
    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")