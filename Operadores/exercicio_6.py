A = input("Digite o valor de A (True/False): ") == "True"
B = input("Digite o valor de B (True/False): ") == "True"
C = input("Digite o valor de C (True/False): ") == "True"
D = input("Digite o valor de D (True/False): ") == "True"

resultado1 = A or B
resultado2 = C or D
resultado3 = A or B or C
resultado4 = A or B or C or D
resultado5 = (A or B) or (C or D)

print(f"A or B: {resultado1}")
print(f"C or D: {resultado2}")
print(f"A or B or C: {resultado3}")
print(f"A or B or C or D: {resultado4}")
print(f"(A or B) or (C or D): {resultado5}")