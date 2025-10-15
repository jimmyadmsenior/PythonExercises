import random

numero_secreto = random.randint(1, 50)

print("Tente adivinhar o número entre 1 e 50!")

while True:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print("Muito baixo! Tente novamente.")