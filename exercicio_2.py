num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

divisao_real = num1 / num2
divisao_inteira = num1 // num2
diferenca = divisao_real - divisao_inteira

print(f"Divisão real: {divisao_real}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Diferença: {diferenca}")