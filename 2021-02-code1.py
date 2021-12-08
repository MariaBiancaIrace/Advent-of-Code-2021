with open("2021-02-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()

horizontal = 0
vertical = 0

for linha in lista_linhas:
    linha = linha.split(" ")
    if linha[0] == "forward":
        horizontal = horizontal + int(linha[1])
    if linha[0] == "down":
        vertical = vertical + int(linha[1])
    if linha[0] == "up":
        vertical = vertical - int(linha[1])

    #if int(linha_anterior) < int(linha):
    #    contador_aumentos = contador_aumentos + 1    
    print(linha,vertical,horizontal,vertical*horizontal)
    #linha_anterior = linha


