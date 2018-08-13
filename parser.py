# import pandas as pd
# import matplotlib as plt

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
    # descricao = dataset[0]
    # new_dataset = dataset[1::]
    pass

if __name__ == "__main__":
    data_2015 = "data/recife-dados-despesas-2015.csv"
    data_2016 = "data/recife-dados-despesas-2016.csv"
    data_2017 = "data/recife-dados-despesas-2017.csv"
    data_2018 = "data/recife-dados-despesas-2018.csv"
    retorno = concat(data_2015, data_2016, data_2017, data_2018)
    parser(retorno)
