numero = int(input("Digite um número: "))

resto_2 = numero % 2
resto_3 = numero % 3
resto_5 = numero % 5
resto_10 = numero % 10

if resto_2 == 0:
    tipo = "par"
else:
    tipo = "ímpar"

print(f"Resto por 2: {resto_2} (Número {tipo})")
print(f"Resto por 3: {resto_3}")
print(f"Resto por 5: {resto_5}")
print(f"Resto por 10: {resto_10}")