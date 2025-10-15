A = input("Digite o valor de A (True/False): ") == "True"
B = input("Digite o valor de B (True/False): ") == "True"
C = input("Digite o valor de C (True/False): ") == "True"
D = input("Digite o valor de D (True/False): ") == "True"

resultado1 = A and B
resultado2 = C and D
resultado3 = A and B and C
resultado4 = A and B and C and D
resultado5 = (A and B) and (C and D)

print(f"A and B: {resultado1}")
print(f"C and D: {resultado2}")
print(f"A and B and C: {resultado3}")
print(f"A and B and C and D: {resultado4}")
print(f"(A and B) and (C and D): {resultado5}")