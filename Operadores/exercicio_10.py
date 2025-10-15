a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado1 = a + b * c
resultado2 = (a + b) * c
resultado3 = a ** b + c
resultado4 = a ** (b + c)
resultado5 = a + b / c
resultado6 = (a + b) / c
resultado7 = a % b + c * 2
resultado8 = (a + b * c) ** 2 - a

print(f"a + b * c = {resultado1}")
print(f"(a + b) * c = {resultado2}")
print(f"a ** b + c = {resultado3}")
print(f"a ** (b + c) = {resultado4}")
print(f"a + b / c = {resultado5}")
print(f"(a + b) / c = {resultado6}")
print(f"a % b + c * 2 = {resultado7}")
print(f"(a + b * c) ** 2 - a = {resultado8}")

print("\nExplicação da precedência:")
print("1. Na expressão 'a + b * c': multiplicação é executada primeiro")
print("2. Na expressão '(a + b) * c': parênteses alteram a precedência")
print("3. Na expressão 'a ** b + c': potenciação é executada primeiro")
print("4. Na expressão 'a ** (b + c)': parênteses alteram a precedência")
print("5. Na expressão 'a + b / c': divisão é executada primeiro")
print("6. Na expressão '(a + b) / c': parênteses alteram a precedência")
print("7. Na expressão 'a % b + c * 2': módulo e multiplicação antes da soma")
print("8. Na expressão '(a + b * c) ** 2 - a': multiplicação, potenciação, depois subtração")