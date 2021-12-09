import sys

with open("2021-04-input.txt") as arquivo:
    lista_linhas = arquivo.read()
    #.splitlines()

lista_linhas = lista_linhas.replace("\n\n","@@@")
lista_linhas = lista_linhas.replace("\n"," ")
lista_linhas = lista_linhas.replace("@@@","\n")

lista_linhas = lista_linhas.splitlines()

lista_cartelas = []
lista_sorteio = []
soma_numeros_restantes = 0
cartelas_sorteadas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


lista_sorteio = lista_linhas[0].split(',')

print(lista_sorteio)


for i in range(1,len(lista_linhas)):
    print(i)
    lista_cartelas.append(lista_linhas[i].split())

print(lista_cartelas)

contador_cartela = -1

for numero_sorteado in lista_sorteio:
    for cartela in lista_cartelas:
        for item_cartela in range(0,len(cartela)):
            if numero_sorteado == cartela[item_cartela]:
                cartela[item_cartela] = "*"
        if (cartela[0] == "*" and cartela[5] == "*" and cartela[10] == "*" and cartela[15] == "*" and cartela[20] == "*") or (cartela[1] == "*" and cartela[6] == "*" and cartela[11] == "*" and cartela[16] == "*" and cartela[21] == "*") or (cartela[2] == "*" and cartela[7] == "*" and cartela[12] == "*" and cartela[17] == "*" and cartela[22] == "*") or (cartela[3] == "*" and cartela[8] == "*" and cartela[13] == "*" and cartela[18] == "*" and cartela[23] == "*") or (cartela[4] == "*" and cartela[9] == "*" and cartela[14] == "*" and cartela[19] == "*" and cartela[24] == "*") or (cartela[0] == "*" and cartela[1] == "*" and cartela[2] == "*" and cartela[3] == "*" and cartela[4] == "*")or (cartela[5] == "*" and cartela[6] == "*" and cartela[7] == "*" and cartela[8] == "*" and cartela[9] == "*") or (cartela[10] == "*" and cartela[11] == "*" and cartela[12] == "*" and cartela[13] == "*" and cartela[14] == "*") or (cartela[15] == "*" and cartela[16] == "*" and cartela[17] == "*" and cartela[18] == "*" and cartela[19]=="*") or (cartela[20] == "*" and cartela[21] == "*" and cartela[22] == "*" and cartela[23] == "*" and cartela[24] == "*"):
            print("A cartela vencedora foi " + str(cartela))
            print("O ultimo numero sorteado foi:" + numero_sorteado)
            for numero_restante in cartela:
                soma_numeros_restantes += int(numero_restante.replace("*","0"))
            print("A soma dos numeros restantes foi: " + str(soma_numeros_restantes))
            print("O valor final é: ", soma_numeros_restantes*int(numero_sorteado))
            print(cartelas_sorteadas)
            sys.exit()

        
#print(lista_cartelas)

#print(lista_linhas)
#print(len(lista_linhas))


#matriz_teste = [[1,2,3],[4,5,6],[7,8,9]]
#print(type(matriz_teste))
#print(matriz_teste[0][0],matriz_teste[2][2])
