num = int(input("Informe um número: "))

if num >= 0 :
    if num % 2 == 0:
        resultado = num * num
        print(resultado)
    else: 
        resultado = num * num * num
        print(resultado)
else: 
    print("Informe um valor positivo")