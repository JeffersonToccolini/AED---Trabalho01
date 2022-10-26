import sys

NUM_COLUNAS = 7
total = [0] * NUM_COLUNAS
dataset = "vehicles.csv"


# Cria o arquivo de dados
def criar_arquivo01():
    with open(dataset) as infile:
        for line in infile:
            calcular_maior(line)
    with open(dataset) as infile:
        for line in infile:
            #criar_arquivo(line)
            teste(line)


# Calcula o seek
def calcular_maior(linha):
    count = 0
    coluna = 0
    for char in linha:
        if char != ",":
            count += 1
        else:  # entra se for virgula
            if coluna > 6:  # dataset com erro
                return total
            if count > total[coluna]:
                total[coluna] = count
            count = 0
            coluna += 1
    # if coluna > 6:  # dataset com erro
    #    return total
    # if count > total[coluna]:
    #    total[coluna] = count - 1
    return total

def teste(linha):
    #print(linha.split(","))
    temp_string = linha.split(",")
    temp_string2 = ""
    arquivo01 = open("arquivo01.txt", "a")
    for i in range(NUM_COLUNAS):
        if len(temp_string[i]) > 0:
            temp_string2 += temp_string[i] + " "*total[i]
    print(temp_string2)
    #arquivo01.writelines(temp_string)


# "68563,ventura county,10000,1989,jaguar,xjs v12 coupe,12 cylinders"
def criar_arquivo(linha):
    arquivo01 = open("arquivo01.txt", "a")
    temp_string = ""
    count = 0  # quantidade de char antes da ,
    coluna = 0
    for char in linha:
        if char != ",":
            temp_string += char
            count += 1
        else:
            if coluna < 6:  # dataset com erro
                tmp_count = total[coluna] - count
                temp_string += " " * (tmp_count + 2)
            coluna += 1
            count = 0
    arquivo01.writelines(temp_string)
    arquivo01.close()


def mostrar_dados(arquivo):
    with open(arquivo) as arq:
        for linha in arq:
            print(linha)


def criar_indice_um(linhas):
    tamanho = len(str(num_linhas))
    arquivo01 = open("indice01.txt", "a")
    for x in range(linhas):
        tamanho2 = len(str(x))
        tamanho3 = tamanho - tamanho2 + 2
        arquivo01.write(str(x + 1) + (" " * tamanho3) + "\n")
    arquivo01.close()


def pesquisa_binaria(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
            return pesquisa_binaria(arr, low, mid - 1, x)
        else:
            return pesquisa_binaria(arr, mid + 1, high, x)
    else:
        return -1


def pesquisa_binaria_arquivo(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
            return pesquisa_binaria(arr, low, mid - 1, x)
        else:
            return pesquisa_binaria(arr, mid + 1, high, x)
    else:
        return -1


ans = True

while ans:
    print("Digite a sua escolha!\n"
          "1 - Criar o arquivo de dados\n"
          "2 - Mostrar os dados\n"
          "3 - Pesquisar arquivo inicial\n"
          "4 - Criar arquivo de índice sequencial\n"
          "5 - Pesquisar no arquivo de índice\n"
          "9 - Sair")
    choice = input()

    if choice == "1":
        criar_arquivo01()
        print("Aqruivo criado!\n")
    elif choice == "2":
        mostrar_dados('arquivo01.txt')
    elif choice == "3":
        continue
    elif choice == "4":
        num_linhas = sum(1 for line in open(dataset))
        criar_indice_um(num_linhas)
    elif choice == "5":
        num = int(input("Digite um número "))
        arr = []
        with open('indice01.txt') as file:
            for line in file:
                line = line.strip()  # preprocess line
                arr.append(int(line))
        pesq = pesquisa_binaria(arr, 0, len(arr) - 1, num)
        if pesq != -1:
            print("Índice {} encontrado ! ".format(pesq))
        else:
            print("Índice {} não encontrado ! ".format(num))
    elif choice == "9":
        sys.exit
    else:
        print()
        print("Escolha uma opção !")
