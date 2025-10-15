quantidade = int(input("Quantas notas você vai informar? "))
soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma = soma + nota

media = soma / quantidade

print(f"Média: {media}")

if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")