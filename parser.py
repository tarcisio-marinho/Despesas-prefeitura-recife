# import pandas as pd
from matplotlib import pyplot as plt

#download link -> http://dados.recife.pe.gov.br/dataset/despesas-orcamentarias

# This function will concat all the 4 files into one list and return the dataset
# also will write the new dataset to disk if wanted
def concat(arq1, arq2, arq3, arq4, write_file=False):

    desc = []
    with open(arq1, encoding="utf8") as f:
        dataset1 = f.read()
    linhas1 = dataset1.split('\n')
    descricao = linhas1[0]
    new_dataset1 = linhas1[1::]

    with open(arq2, encoding="utf8") as f:
        dataset2 = f.read()
    linhas2 = dataset2.split('\n')
    new_dataset2 = linhas2[1::]

    with open(arq3, encoding="utf8") as f:
        dataset3 = f.read()
    linhas3 = dataset3.split('\n')
    new_dataset3 = linhas3[1::]

    with open(arq4, encoding="utf8") as f:
        dataset4 = f.read()
    linhas4 = dataset4.split('\n')
    new_dataset4 = linhas4[1::]

    desc.append(descricao)
    # data will be a list
    data = desc + new_dataset1 + new_dataset2 + new_dataset3 + new_dataset4

    if(write_file):
        print('writing file to disk')
        with open("data/dados-2015-2016-2017-2018.csv", 'w') as f:
            f.write('\n'.join(data))

    return data

# this function will parse the dataset treating and cleaning the data
def parser(dataset):
    with open(dataset, encoding="utf8") as f:
        dataset1 = f.read()
    linhas = dataset1.split('\n')
    descricao = linhas[0].split(';')
    new_dataset = linhas[1::]
    
    total_gasto_2015_2018 = 0 
    total_gasto_2015 = 0
    total_gasto_2016 = 0
    total_gasto_2017 = 0
    total_gasto_2018 = 0
    total_credor_nao_informado = 0
    funcao_nome = [] # Nome dos locais onde o dinheiro foi gasto

    for linha in new_dataset:
        data = linha.split(';')
        if(len(data) >= 38):

            valor = data[38].replace(',', '.') # posição da lista que contém o valor pago
            valor = float(valor)


            if("CREDOR NÃO INFORMADO" == data[33]):
                total_credor_nao_informado += valor

            if(data[0] == "2015"):
                total_gasto_2015 += valor

            if(data[0] == "2016"):
                total_gasto_2016 += valor

            if(data[0] == "2017"):
                total_gasto_2017 += valor

            if(data[0] == "2018"):
                total_gasto_2018 += valor

            
            if(data[19] not in funcao_nome):
                funcao_nome.append(data[19])
            
            total_gasto_2015_2018 += valor 
    
    print("Gastos totais de 2015 até 2018: {}\nGastos 2015: {}\nGastos 2016: {}\n\
Gastos 2017: {}\nGastos 2018: {}".format(
        total_gasto_2015_2018, total_gasto_2015, total_gasto_2016,
        total_gasto_2017, total_gasto_2018
    ))

    print("Total com credor não informado, de 2015 - 2018: {}".format(total_credor_nao_informado))
    
    
    print("porcentagem credor não informado {}%".format(round((total_credor_nao_informado * (1/100)) / total_gasto_2015_2018 * 10000, 4)))
    print("Na esquerda, o total de gastos por credor não informado, a direita o gasto total.")
    plt.bar(range(2), [total_credor_nao_informado, total_gasto_2015_2018])
    plt.show()


if __name__ == "__main__":
    data_2015 = "data/recife-dados-despesas-2015.csv"
    data_2016 = "data/recife-dados-despesas-2016.csv"
    data_2017 = "data/recife-dados-despesas-2017.csv"
    data_2018 = "data/recife-dados-despesas-2018.csv"
    new_file = "data/dados-2015-2016-2017-2018.csv"
    # retorno = concat(data_2015, data_2016, data_2017, data_2018, True)
    parser(new_file)
