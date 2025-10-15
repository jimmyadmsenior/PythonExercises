x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))
z = float(input("Digite o valor de z: "))

resultado1 = x > y and y > z
resultado2 = x > y or y > z
resultado3 = x == y or x == z
resultado4 = x != y and y != z
resultado5 = not (x > y) and z > y
resultado6 = (x > y and y > z) or (x == z)

print(f"x > y and y > z: {resultado1}")
print(f"x > y or y > z: {resultado2}")
print(f"x == y or x == z: {resultado3}")
print(f"x != y and y != z: {resultado4}")
print(f"not (x > y) and z > y: {resultado5}")
print(f"(x > y and y > z) or (x == z): {resultado6}")