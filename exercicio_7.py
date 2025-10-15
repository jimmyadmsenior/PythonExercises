A = input("Digite o valor de A (True/False): ") == "True"
B = input("Digite o valor de B (True/False): ") == "True"
C = input("Digite o valor de C (True/False): ") == "True"

not_A= not A
not_B = not B
not_C = not C
not_A_and_B = not (A and B)
not_A_or_B = not (A or B)
not_A_and_not_B = not A and not B
not_not_A = not (not A)

print(f"not A: {not_A}")
print(f"not B: {not_B}")
print(f"not C: {not_C}")
print(f"not (A and B): {not_A_and_B}")
print(f"not (A or B): {not_A_or_B}")
print(f"not A and not B: {not_A_and_not_B}")
print(f"not (not A): {not_not_A}")