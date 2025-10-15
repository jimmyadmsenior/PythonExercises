num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
diferente = num1 != num2
maior_igual = num1 >= num2
menor_igual = num1 <= num2

print(f"{num1} > {num2} : {maior}")
print(f"{num1} < {num2} : {menor}")
print(f"{num1} == {num2} : {igual}")
print(f"{num1} != {num2} : {diferente}")
print(f"{num1} >= {num2} : {maior_igual}")
print(f"{num1} <= {num2} : {menor_igual}")