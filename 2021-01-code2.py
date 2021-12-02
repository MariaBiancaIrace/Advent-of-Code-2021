with open("2021-01-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()

contador_aumentos = 0
linha_anterior = 33000
lista_soma = []

#print(len(lista_linhas))
for i in range(0,len(lista_linhas)-2):
    lista_soma.append(int(lista_linhas[i])+int(lista_linhas[i+1])+int(lista_linhas[i+2]))


for linha in lista_soma:
    print(linha)
    if int(linha_anterior) < int(linha):
        contador_aumentos = contador_aumentos + 1    
    print(linha,contador_aumentos)
    linha_anterior = linha


