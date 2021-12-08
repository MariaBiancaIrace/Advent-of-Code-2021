with open("2021-03-input.txt") as arquivo:
    lista_linhas = arquivo.read().splitlines()


oxigenio_bin = ""
co2_bin = ""
oxigenio_dec = 0
co2_dec = 0

total_bits = [0,0,0,0,0,0,0,0,0,0,0,0]
total_bits_co2 = [0,0,0,0,0,0,0,0,0,0,0,0]

lista_linhas_co2 = lista_linhas

for i in range(0,12):
    for linha in lista_linhas:
        total_bits[i] = total_bits[i] + int(linha[i])
    if total_bits[i] < (len(lista_linhas)/2):
        oxigenio_bin += "0"
    else: 
        oxigenio_bin +="1"

    lista_linhas = [linha for linha in lista_linhas if linha[i] == oxigenio_bin[i]]
    print(oxigenio_bin,lista_linhas)


for i in range(0,12):
    for linha in lista_linhas_co2:
        total_bits_co2[i] = total_bits_co2[i] + int(linha[i])
    if total_bits_co2[i] < (len(lista_linhas_co2)/2):
        co2_bin += "1"
        #if len(lista_linhas_co2) = 1:
        #    co2_bin = lista_linhas_co2[0]
        #    break
    else: 
        co2_bin += "0"

    if len(lista_linhas_co2) == 1:
        co2_bin = lista_linhas_co2[0]
        break
    else:
        lista_linhas_co2 = [linha for linha in lista_linhas_co2 if linha[i] == co2_bin[i]]
    print(co2_bin,lista_linhas_co2)


oxigenio_dec = int(oxigenio_bin,2)
co2_dec = int(co2_bin,2)

print(total_bits,oxigenio_bin,co2_bin,oxigenio_dec,co2_dec,oxigenio_dec*co2_dec,lista_linhas)





