with open("2021-03-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()


lista_total = [0,0,0,0,0,0,0,0,0,0,0,0]
gamma_bin = ""
epsilon_bin = ""
gamma_dec = 0
epsilon_dec = 0



for linha in lista_linhas:
    for i in range(0,len(linha)):
        lista_total[i] = int(lista_total[i]) + int(linha[i])
    print(linha,lista_total)
        
for bit_total in lista_total:
    if bit_total < (len(lista_linhas)/2):
        gamma_bin = gamma_bin + "0"
        epsilon_bin = epsilon_bin + "1"
    else:
        gamma_bin = gamma_bin + "1"
        epsilon_bin = epsilon_bin + "0"

gamma_dec=int(gamma_bin,2)
epsilon_dec=int(epsilon_bin,2)


print(gamma_bin,epsilon_bin, gamma_dec,epsilon_dec,gamma_dec*epsilon_dec)



    #linha = linha.split(" ")
    #if linha[0] == "forward":
    #    horizontal = horizontal + int(linha[1])
    #if linha[0] == "down":
    #    vertical = vertical + int(linha[1])
    #if linha[0] == "up":
    #    vertical = vertical - int(linha[1])

    #if int(linha_anterior) < int(linha):
    #    contador_aumentos = contador_aumentos + 1    
    #print(linha,vertical,horizontal,vertical*horizontal)
    #linha_anterior = linha


