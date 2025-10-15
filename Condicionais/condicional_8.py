num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Operador inválido!")