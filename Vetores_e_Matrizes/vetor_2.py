numeros = []

for i in range(1, 7):
    numero = float(input(f"Digite o {i}o número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")