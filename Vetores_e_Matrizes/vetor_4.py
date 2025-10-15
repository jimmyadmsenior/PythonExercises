nomes = []

for i in range(1, 6):
    nome = input(f"Digite o {i}o nome: ")
    nomes.append(nome)

nome_busca = input("Digite um nome para buscar: ")

if nome_busca in nomes:
    print(f'O nome "{nome_busca}" está na lista.')
else:
    print(f'O nome "{nome_busca}" não está na lista.')