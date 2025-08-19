print(" ## Programa de empréstimos ## \n Responda 0- Não e 1- Sim")

negativado = int(input("Possui nome negativado?"))
if negativado == 1:
    print("Não pode realizar empréstimo no momento.")
else:
    carteiraAssinada = int(input("Possui carteira assinada? "))
    if carteiraAssinada == 0:
        print("Não pode realizar empréstimo no momento.")
    else: 
        casaPropria = input("Possui casa própria? ")
        if casaPropria == 0:
            print("Não pode realizar empréstimo no momento.")
        else: 
            print("Pode soliciar empréstimo!")