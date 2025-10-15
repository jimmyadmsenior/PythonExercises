idade = int(input("Digite a idade: "))

if idade < 12:
    print("Categoria: Criança")
elif idade >= 12 and idade <= 17:
    print("Categoria: Adolescente")
elif idade >= 18 and idade <= 59:
    print("Categoria: Adulto")
else:
    print("Categoria: Idoso")