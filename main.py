import random

numSorteado = random.randint(1,10)
numeroUsuario = 0

def contraCaracter():
    while True:
        try:
            return int(input("Adivinhe o numero sorteado de 1 a 10: "))
        except ValueError:
            print("ATENÇÃO - Valor invalido!")

def contraCaracterSecond():
    while True:
        try:
            return int(input("Tente novamente: "))
        except ValueError:
            print("ATENÇÃO - Valor invalido!")

numeroUsuario = contraCaracter()

while numeroUsuario != numSorteado:

    if numeroUsuario <= 10:
        print(f"Não é o numero {numeroUsuario}!")
        numeroUsuario = contraCaracterSecond()
    elif numeroUsuario > 10:
        print(f"Numero {numeroUsuario} é maior que 10, escolha entre 1 a 10!")
        numeroUsuario = contraCaracterSecond()


print(f"ACERTOU!!!, numero {numSorteado} era o sorteado, PARABÉNS!!")
