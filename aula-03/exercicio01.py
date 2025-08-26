letra = input("Informe uma letra simples do alfabeto: ")

match letra:
    case "a":
        print(f"A letra: {letra} é vogal")
    case "e":
        print(f"A letra: {letra} é vogal")
    case "i":
        print(f"A letra: {letra} é vogal")
    case "o":
        print(f"A letra: {letra} é vogal")
    case "u":
        print(f"A letra: {letra} é vogal")
    case _:
        print(f"A letra: {letra} é consoante")