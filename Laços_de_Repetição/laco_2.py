n = int(input("Digite um número: "))
soma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma = soma + i

print(f"Soma dos números pares entre 1 e {n}: {soma}")