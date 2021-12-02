with open("2021-01-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()

contador_aumentos = 0
linha_anterior = 11000

for linha in lista_linhas:
    if int(linha_anterior) < int(linha):
        contador_aumentos = contador_aumentos + 1    
    print(linha,contador_aumentos)
    linha_anterior = linha


