import csv
import os

def Criar_tabela(nomeArquivo,l0,l1):
    with open(nomeArquivo,"w",newline="") as arquivo:
        arqwriter = csv.writer(arquivo,delimiter=";")

        arqwriter.writerow(l0)
        arqwriter.writerows(l1)

    arquivo.close()

def Gravar_tabela_no_arquivo(arquivoVelho,arquivoNovo):
    with open(arquivoVelho) as arqvelho:
        arqreader = csv.reader(arqvelho)

        with open(arquivoNovo,"w",newline="") as arqnovo:
            arqwriter = csv.writer(arqnovo)

            for linha in arqreader:
                arqwriter.writerow(linha)

    arqnovo.close()
    arqvelho.close()

def Ler_tabela(nomeArquivo):
    with open(nomeArquivo) as arquivo:
        arqreader = csv.reader(arquivo,delimiter=";")

        lista = []

        for linha in arqreader:
            lista.append(linha)
        print(lista[0])
        for linha in lista[1:]:
            for i in range(len(linha)):
                if i != len(linha)-1:
                    print(linha[i],end="\t\t")
                else:
                    print(linha[i])


def Apagar_tabela(nomeArquivo):
    os.unlink(nomeArquivo)

def Ordenar_tabela(nomeArquivo,campo_ordenado,tipo_ordenacao):
   with open(nomeArquivo) as arquivo:
       arqreader = csv.reader(arquivo,delimiter=";")

       l = []
       for linha in arqreader:
           l.append(linha)

       ord = l[0].index(campo_ordenado)

       if tipo_ordenacao == "C":
           lista = sorted(l[1:],key=lambda x:x[ord])
       elif tipo_ordenacao == "D":
           lista = sorted(l[1:],key=lambda x:x[ord],reverse=True)

       print(l[0])
       for linha in lista:
           for i in range(len(linha)):
               if i != len(linha)-1:
                   print(linha[i],end="\t")
               else:
                   print(linha[i])

def Consultar_registro(nomeArquivo,campo,item):
    with open(nomeArquivo) as arquivo:
        arqreader = csv.reader(arquivo,delimiter=";")

        l = []
        lista = []
        for linha in arqreader:
            l.append(linha)

        print(l[0])
        ord = l[0].index(campo.strip())
        for linha in l:
            if linha[ord] == item:
                lista.append(linha)
        if lista != []:
            for linha in lista:
                for i in range(len(linha)):
                    if i != len(linha)-1:
                        print(linha[i],end="\t\t")
                    else:
                        print(linha[i])
        else:
            print("Não há nenhum registro que contém esse item...")

def Inserir_registro(nomeArquivo,registro):
    with open(nomeArquivo,"a",newline="") as arquivo:
        arqwriter = csv.writer(arquivo,delimiter=";")

        arqwriter.writerow(registro)
    arquivo.close()

def Apagar_registro(nomeArquivo,regisitro):
    with open(nomeArquivo) as arquivo:
        arqreader = csv.reader(arquivo,delimiter=";")

        lista = []

        for linha in arqreader:
            lista.append(linha)

        with open(nomeArquivo,"w",newline="") as arq:
            arqwriter = csv.writer(arq,delimiter=";")

            for linha in lista:
                if linha != registro:
                    arqwriter.writerow(linha)
    arquivo.close()

def Listagem_total_ou_filtrada(nomeArquivo,campo,filtro):
    with open(nomeArquivo) as arquivo:
        arqreader = csv.reader(arquivo,delimiter=";")

        lista = []

        for linha in arqreader:
            lista.append(linha)

        indice = lista[0].index(campo)

        print(lista[0])
        for linha in lista[1:]:
            if linha[indice] in filtro:
                for i in range(len(linha)):
                    if i != len(linha)-1:
                        print(linha[i],end="\t\t")
                    else:
                        print(linha[i])

print("1 – criar uma tabela")
print("2 – gravar tabela no arquivo")
print("3 – ler tabela do arquivo")
print("4 – apagar tabela do arquivo")
print("5 – listar dados da tabela: C - crescente e D - descrescente")
print("6 – consultar um registro")
print("7 –  inserir novo registro na tabela")
print("8 – apagar registro")
print("9 – listagem total ou filtrada")
print("0 – sair do programa")

opcao = int(input("Qual ação deseja?"))

while opcao != 0:
    if opcao == 1:
        nomeArquivo = input("Nome do arquivo")
        quantDados = int(input("Quantas linha de dados serão?"))
        linhaBase = list(map(str,input("Digite os campos da linha base separado por virgulas: ").split(",")))
        lista_com_dados = []
        for i in range(quantDados):
            lista_com_dados.append(list(map(str,input("Preencha os campos separando por virgulas: ").split(","))))

        Criar_tabela(nomeArquivo,linhaBase,lista_com_dados)

    elif opcao == 2:
        velho = input("Qual arquivo deseja copiar?")
        novo = input("Onde deseja gravar?")
        Gravar_tabela_no_arquivo(velho,novo)

    elif opcao == 3:
        nomeArquivo = input("Qual arquivo será lido?")
        Ler_tabela(nomeArquivo)

    elif opcao == 4:
        nomeArquivo = input("Qual arquivo será apagado?")
        Apagar_tabela(nomeArquivo)

    elif opcao == 5:
        nomeArquivo = input("Qual arquivo será ordenado?")
        campo_ordenado = input("Digite o campo que sera ordenado: ")
        tipo_ordenacao = input("Digite C para crescente ou D para decrescente: ").upper()
        Ordenar_tabela(nomeArquivo,campo_ordenado,tipo_ordenacao)

    elif opcao == 6:
        nomeArquivo = input("Qual arquivo será lido?")
        campo = input("Em qual campo deseja procurar?")
        item = input("Qual(s) item(s) deseja procurar?")
        Consultar_registro(nomeArquivo,campo,item)

    elif opcao == 7:
        nomeArquivo = input("Qual arquivo será adicionado o registro novo?")
        registro = input("Digite os dados separados por virgula: ").split(",")
        Inserir_registro(nomeArquivo,registro)

    elif opcao == 8:
        nomeArquivo = input("Em qual arquivo está o registro?")
        registro = input("Digite os dados do registro que será apagado separados por vírgula: ").split(",")
        Apagar_registro(nomeArquivo,registro)

    elif opcao == 9:
        nomeArquivo = input("Em qual arquivo será feito a consulta?")
        pergunta = int(input("Se deseja ver a listagem total, digite: 0. Se deseja algum filtro, digite: 1 : "))
        if pergunta == 0:
            Ler_tabela(nomeArquivo)
        elif pergunta == 1:
            campo = input("Em qual campo o filtro será aplicado?")
            filtro = input("Quais os dados que devem aparecer desse campo (separados por vírgula)?").split(",")
            Listagem_total_ou_filtrada(nomeArquivo,campo,filtro)
        else:
            print("Entrada invalida!")

    opcao = int(input("Qual ação deseja?"))