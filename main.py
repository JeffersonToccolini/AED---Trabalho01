import os
from operator import itemgetter
import ArvoreB

"""
Maior valor do carro ?
Mostrar todos os carros de um estado 

Índices = ID(1000 em 1000)  ,valor( Valor ordenado, posião )
Árvore = ano
Listas encadeadas = Estado"""

arq_db_nformatado = "vehicles.csv"
arq_db_formatado = "dbformatado.txt"
arq_indice01 = "indice01.txt"
arq_indice02 = "indice02.txt"
total_linhas = 101464
colunas_planilha = 7
tamanho_seek = [0] * colunas_planilha


def criar_arquivo_inicial_chamada():
    tamanho_seek = calcular_seek(arq_db_nformatado)
    with open(arq_db_nformatado) as arq:
        for linha in arq:
            criar_arquivo_inicial(linha)


def criar_arquivo_inicial(linhha):
    f = open(arq_db_formatado, "a")
    texto_split = linhha.split(",")
    temp_texto = ""
    for tm in range(colunas_planilha):
        if tm == 6:  # Retira o \n do final da linha
            texto_split[6] = texto_split[6].replace("\n", '')
        tamanho = tamanho_seek[tm] - len(texto_split[tm])
        temp_texto += texto_split[tm] + " " * tamanho
    f.writelines(temp_texto + "\n")
    f.close()

def calcular_seek(arquivo):
    custos_seek = [0] * colunas_planilha
    with open(arquivo) as arq:
        for linha in arq:
            texto_split = linha.split(",")
            for ind in range(colunas_planilha):
                if len(texto_split[ind]) > int(custos_seek[ind]):
                    custos_seek[ind] = len(texto_split[ind])
    return custos_seek


def pesquisa_binaria_arquivos(arq, low, high, x, seek, seek_pesquisa):
    # arq.seek(((low * 137) - 137), 0)

    try:  # Tenta fazer o seek, caso estiver fora do arquivo retorna -1
        if low == 0:
            arq.seek(0, 0)
            menor = int(arq.read(seek_pesquisa))
        else:
            arq.seek(((low * seek) - seek), 0)
            menor = int(arq.read(seek_pesquisa))
        arq.seek(((high * seek) - seek), 0)
        maior = int(arq.read(seek_pesquisa))
    except ValueError:
        return -1
    finally:
        pass
    if maior >= menor:
        mid = (maior + menor) // 2
        arq.seek(((mid * seek) - seek), 0)
        meio = int(arq.read(seek_pesquisa))
        if meio == x:
            return meio
        elif meio > x:
            return pesquisa_binaria_arquivos(arq, menor, meio - 1, x, seek, seek_pesquisa)
        else:
            return pesquisa_binaria_arquivos(arq, meio + 1, maior, x, seek, seek_pesquisa)
    else:
        return -1


def pesquisa_binaria_array(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if int(arr[mid]) == x:
            return 1
        elif int(arr[mid]) > x:
            return pesquisa_binaria_array(arr, low, mid - 1, x)
        else:
            return pesquisa_binaria_array(arr, mid + 1, high, x)
    else:
        return -1


def criar_indice_um():
    f = open(arq_indice01, "a")
    i = 0
    while i < total_linhas:
        f.write(str(i) + "\n")
        i += 1000
    return


def pesquisar_indice_um(num):
    with open(arq_indice01) as f:
        lines = f.read().splitlines()
    lines = list(map(int, lines))  # transforma a lista<str> em lista<int>
    indice = min(lines, key=lambda x: abs(x - num))  # calcula o indice
    tamanho_seek = calcular_seek(arq_db_nformatado)
    tamanho_total_seek = sum(tamanho_seek) + 2
    arq = open(arq_db_formatado)
    if num < 1000:
        resultado = pesquisa_binaria_arquivos(arq, 0, 1000, num, tamanho_total_seek, 6)
    else:
        resultado = pesquisa_binaria_arquivos(arq, indice - 500, indice + 500, num, tamanho_total_seek, 6)
    return resultado


def calcular_quantidade_linhas(arq):
    f = open(arq)
    num_linhas = sum(1 for line in open(arq))
    f.close()
    return num_linhas


def criar_indice_dois():
    lista = []
    lista_temp = []
    lista_temp2 = []
    f = open(arq_indice02, "a")
    with open(arq_db_nformatado) as arq:
        for linha in arq:
            lines = linha.split(",")
            lista_temp.append(lines[2])
            lista_temp.append(lines[0])
            lista_temp2 = lista_temp.copy()
            # print(lista_temp)
            lista.append(lista_temp2)
            lista_temp.clear()
            temp = ""

    for i in range(len(lista)):  # transforma as listas dentro da lista em <int>
        lista[i] = list(map(int, lista[i]))
    lista = sorted(lista, key=itemgetter(0))  # ordena a lista
    temp = ""
    for i in range(len(lista)):
        tamanho = tamanho_seek[2] - len(str(lista[i][0]))
        temp = str(lista[i][0]) + tamanho * " " + "  "
        tamanho = tamanho_seek[0] - len(str(lista[i][1]))
        temp += str(lista[i][1]) + tamanho * " " + "\n"
        f.writelines(temp)
        temp = ""
    return


def pesquisa_binaria_array_dois(arr1, low, high, x, arr2):
    if high >= low:
        mid = (high + low) // 2
        if int(arr1[mid]) == x:
            return int(arr2[mid])  # retorna o indice
        elif int(arr1[mid]) > x:
            return pesquisa_binaria_array_dois(arr1, low, mid - 1, x, arr2)
        else:
            return pesquisa_binaria_array_dois(arr1, mid + 1, high, x, arr2)
    else:
        return -1


def pesquisa_indice_dois(num):
    """Pesquisa no arquivo indice 02 , retornando -1 se nao achar e o valor do indice caso achar"""
    i = 0
    lista_custo = []
    lista_indice = []
    with open(arq_indice02) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        temp = lines[i].split()
        lista_custo.append(int(temp[0]))
        lista_indice.append(int(temp[1]))

    return pesquisa_binaria_array_dois(lista_custo, 1, len(lista_custo) - 1, num, lista_indice)


def exbir_linha_arquivo(arq, seek):
    f = open(arq, "r")
    f.seek(seek, 0)
    res = f.readline()
    f.close()
    return res


def criar_indice_tres():
    lista_inicial = []

    with open(arq_db_nformatado) as arq:  # cria a primeira lista com os estados
        for linha in arq:
            lines = linha.split(",")
            if lines[1] not in lista_inicial:
                lista_inicial.append(lines[1])

    lista_secundaria = [""] * len(lista_inicial)

    with open(arq_db_nformatado) as arq:  # cria a lista secundaria dividindo os valores com espaço
        for linha in arq:
            lines = linha.split(",")
            if lines[1] in lista_inicial:
                index = lista_inicial.index(lines[1])
                lista_secundaria[index] = lista_secundaria[index] + " " + lines[0]
    # print(lista_secundaria)
    return lista_inicial, lista_secundaria


def pesquisa_indice_tres(estado):
    lista_inicial, lista_secundaria = criar_indice_tres()
    if estado in lista_inicial:
        index = lista_inicial.index(estado)
        return lista_secundaria[index]
    else:
        return -1


def criar_indice_quatro(num):
    f = open(arq_indice02, "a")
    with open(arq_db_nformatado) as arq:
        for linha in arq:
            lines = linha.split(",")
            # print(lines)
            if int(lines[0]) == 1:
                root = ArvoreB.Node(int(lines[3]), int(lines[0]))
            else:
                if len(lines[3]) > 0:  # campo null
                    root.insert(int(lines[3]), int(lines[0]))
                else:
                    root.insert(0, int(lines[0]))

    f.close()

    return root.findval(num+1)


def pergunta_01():
    """Retorna o indice da ultima linha(maior valor dos carros)"""
    seek = tamanho_seek[2] + tamanho_seek[0] + 4
    f = open(arq_indice02, 'r')
    f.seek(total_linhas*seek - seek)
    temp = f.readline().split()
    return int(temp[1])


tamanho_seek = calcular_seek(arq_db_nformatado)
tamanho_total_seek = sum(tamanho_seek) + 2

while True:
    print("Digite a sua escolha ! \n"
          "1 - Criar Arquivo DB \n"
          "2 - Mostrar os dados do Arquivo DB \n"
          "3 - Pesquisar no Arquivo DB \n"
          "4 - Criar arquivo Indice 01 \n"
          "5 - Pesquisar no arquivo Indice 01 \n"
          "6 - Criar arquivo Indice 02 \n"
          "7 - Pesquisar no arquivo Indice 02 \n"
          "8 - Pesquisa indice 3 \n"
          "9 - Pesquisar indice 4\n"
          "10 - Qual é o carro mais caro vendido ? ")

    escolha = int(input())
    if escolha == 1:
        criar_arquivo_inicial_chamada()
        print("Arquivo {} criado !".format(arq_db_formatado))
    elif escolha == 2:
        with open(arq_db_nformatado) as arq:
            for linha in arq:
                print(linha)
    elif escolha == 3:
        num = int(input("Digite um número :"))
        arq = open(arq_db_formatado, "r")
        resultado = pesquisa_binaria_arquivos(arq, 0, total_linhas, num, tamanho_total_seek, 6)
        if resultado == -1:
            print("Não encontrado")
        else:
            print(exbir_linha_arquivo(arq_db_formatado, resultado * tamanho_total_seek - tamanho_total_seek))

    elif escolha == 4:
        criar_indice_um()
        print("Arquivo {} criado !".format(arq_indice01))

    elif escolha == 5:
        num = int(input("Digite um número :"))
        resultado = pesquisar_indice_um(num)
        if resultado == -1:
            print("Não encontrado")
        else:
            print(exbir_linha_arquivo(arq_db_formatado, resultado * tamanho_total_seek - tamanho_total_seek))

    elif escolha == 6:
        criar_indice_dois()
        print("Arquivo {} criado !".format(arq_indice02))
    elif escolha == 7:
        num = int(input("Digite um número :"))
        resultado = pesquisa_indice_dois(num)
        if resultado == -1:
            print("Não encontrado")
        else:
            print(exbir_linha_arquivo(arq_db_formatado, resultado * tamanho_total_seek - tamanho_total_seek))
    elif escolha == 8:
        estado = input("Digite um estado : ")
        resultado = pesquisa_indice_tres(estado)
        if resultado == -1:
            print("Não encontrado")
        else:
            resultado = resultado.split(" ")
            resultado.pop(0)
            for i in range(len(resultado)):
                print(
                    exbir_linha_arquivo(arq_db_formatado, int(resultado[i]) * tamanho_total_seek - tamanho_total_seek))

    elif escolha == 9:
        num = int(input("Digite um número :"))
        resultado = criar_indice_quatro(num)
        if resultado == -1:
            print("Não encontrado")
        else:
            print(exbir_linha_arquivo(arq_db_formatado, resultado * tamanho_total_seek - tamanho_total_seek))
    elif escolha == 10:
        print(exbir_linha_arquivo(arq_db_formatado, pergunta_01() * tamanho_total_seek - tamanho_total_seek))