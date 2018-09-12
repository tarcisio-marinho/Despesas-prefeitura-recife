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
    subfuncao_nome = []
    orgao_nome = []
    elemento_nome = []

    valor2 = 0
    
    for linha in new_dataset:
        data = linha.split(';')
        if(len(data) >= 38):

            valor = data[38].replace(',', '.') # posição da lista que contém o valor pago
            valor = float(valor)


            if(data[13] == "AQUISIÇÃO DE IMÓVEIS"):
                valor2 += valor
                

            if(data[3] not in orgao_nome):
                orgao_nome.append(data[3])





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

            if(data[21] not in subfuncao_nome):
                subfuncao_nome.append(data[21])

            if(data[19] not in funcao_nome):
                funcao_nome.append(data[19])
            
            total_gasto_2015_2018 += valor 
    print(valor2)
    # da = {}
    # for orgao in orgao_nome:
    #     valor = 0
    #     for linha in new_dataset:
    #         data = linha.split(';')
    #         if(len(data) >= 38):
    #             if(orgao == data[3]):
    #                 valor += float(data[38].replace(',', '.'))

    #     da[orgao] = valor
    #     valor = 0

    # print(da)

    '''
    {'SECRETARIA DE CULTURA - ADMINISTRAÇÃO SUPERVISIONADA': 264169745.3800002, 'SECRETARIA DE PLANEJAMENTO URBANO': 35517341.95999998, 'ASSESSORIA ESPECIAL DO PREFEITO': 0.0, 'SECRETARIA DE FINANÇAS - ADMINISTRAÇÃO SUPERVISIONADA': 207552126.2699991, 'PROCURADORIA GERAL DO MUNICÍPIO - ADMINISTRAÇÃO SUPERVISIONADA': 837466.6699999999, 'SECRETARIA DE RELAÇÕES INSTITUCIONAIS': 6021992.57999999, 'SECRETARIA DE SAÚDE': 124743501.98, 'SECRETARIA DE PLANEJAMENTO, ADMINISTRAÇÃO E GESTÃO DE PESSOAS': 78604069.48000008, 'ENCARGOS GERAIS DO MUNICÍPIO': 878651416.3899977, 'SECRETARIA DE INFRAESTRUTURA E HABITAÇÃO': 59922955.71999994, 'SECRETARIA DE INFRAESTRUTURA E HABITAÇÃO - ADMINISTRAÇÃO SUPERVISIONADA': 366904856.06999964, 'SECRETARIA DE DESENVOLVIMENTO SOCIAL E DIREITOS HUMANOS - ADMINISTRAÇÃO SUPERVISIONADA': 50999056.739999965, 'SECRETARIA DE ENFRENTAMENTO AO CRACK E OUTRAS DROGAS': 3844933.1000000015, 'SECRETARIA DE ESPORTES': 2919017.050000003, 'SECRETARIA DE SANEAMENTO - ADMINISTRAÇÃO SUPERVISIONADA': 31527681.019999977, 'SECRETARIA DE DESENVOLVIMENTO SOCIAL, JUVENTUDE, POLÍTICAS SOBRE DROGAS E DIREITOS HUMANOS': 42489581.379999876, 'ENCARGOS GERAIS DO MUNCÍPIO': 231143274.21999997, 'SECRETARIA PLANEJAMENTO, ADMINISTRAÇÃO E GESTÃO DE PESSOAS - ADMINISTRAÇÃO SUPERVISIONADA': 285742675.73999983, 'GABINETE DE PROJETOS ESPECIAIS - ADMINISTRAÇÃO SUPERVISIONADA': 16565537.540000001, 'SECRETARIA DE SEGURANÇA URBANA': 172192850.25999287, 'SECRETARIA DE HABITAÇÃO': 9569975.559999999, 'SECRETARIA DE ASSUNTOS JURÍDICOS - ADMINISTRAÇÃO SUPERVISIONADA': 20015940.489999983, 'SECRETARIA DE TURISMO, ESPORTES E LAZER': 62441375.58999941, 'SECRETARIA DE DESENVOLVIMENTO SOCIAL E DIRETOS HUMANOS - ADMINISTRAÇÃO SUPERVISIONADA': 80035248.72999991, 'CONTROLADORIA GERAL DO MUNICÍPIO': 26544154.14999995, 'SECRETARIA DE SAÚDE - ADMINISTRAÇÃO SUPERVISIONADA': 3296516596.8899965, 'SECRETARIA DE DESENVOLVIMENTO E PLANEJAMENTO URBANO - ADMINISTRAÇÃO SUPERVISIONADA': 8000.0, 'SECRETARIA DE JUVENTUDE E QUALIFICAÇÃO PROFISSIONAL': 10170168.619999995, 'PROCURADORIA GERAL DO MUNICÍPIO': 59165780.27, 'SECRETARIA DE MOBILIDADE E CONTROLE URBANO - ADMINISTRAÇÃO SUPERVISIONADA': 299400441.0300021, 'SECRETARIA DE PLANEJAMENTO E GESTÃO': 12908948.549999995, 'GABINETE DE REPRESENTAÇÃO EM BRASÍLIA E RELAÇÕES INTERNACIONAIS': 860969.0799999998, 'SECRETARIA DE FINANÇAS': 193097110.43999946, 'SECRETARIA DE SANEAMENTO': 145095074.19999984, 'SECRETARIA DE MEIO AMBIENTE E SUSTENTABILIDADE - ADMINISTRAÇÃO SUPERVISIONADA': 6867699.099999999, 'SECRETARIA DE DESENVOLVIMENTO SUSTENTÁVEL E MEIO AMBIENTE - ADMINISTRAÇÃO SUPERVISIONADA': 3852356.329999999, 'GABINETE DO PREFEITO': 57417997.079999976, 'REPRESENTAÇÃO EM BRASÍLIA E RELAÇÕES INTERNACIONAIS': 1517611.4500000014, 'SECRETARIA DE DESENVOLVIMENTO E EMPREENDEDORISMO': 3718395.719999996, 'SECRETARIA DE INFRAESTRUTURA E SERVIÇOS URBANOS': 94929717.17000003, 'SECRETARIA DE ASSUNTOS JURÍDICOS': 65513665.91999995, 'SECRETARIA DE TURISMO E LAZER': 49294878.559999846, 'GABINETE DO VICE-PREFEITO': 5103393.339999993, 'SECRETARIA DE ADMINISTRAÇÃO E GESTÃO DE PESSOAS': 89793802.3899998, 'SECRETARIA DE DESENVOLVIMENTO SUSTENTÁVEL E MEIO AMBIENTE': 31790977.93999999, 'SECRETARIA DE INFRAESTRUTURA E SERVIÇOS URBANOS - ADMINISTRAÇÃO SUPERVISIONADA': 2112716501.170018, 'GABINETE DE REPRESENTAÇÃO EM BRASÍLIA': 2374050.5000000033, 'SECRETARIA DE DESENVOLVIMENTO SOCIAL E DIREITOS HUMANOS': 23526733.139999915, 'SECRETARIA DE IMPRENSA': 10801818.150000025, 'GABINETE DE IMPRENSA': 7947583.549999998, 'SECRETARIA DE CULTURA': 111981530.1500002, 'SECRETARIA DE MULHER': 14338388.359999985, 'SECRETARIA DE MOBILIDADE E CONTROLE URBANO': 236230419.89999986, 'SECRETARIA DE DESENV. SOCIAL, JUVENTUDE, POLÍT. SOBRE DROGAS E DIR. HUMANOS - ADM. SUPERVISIONADA': 21943540.94999999, 'SECRETARIA DE EDUCAÇÃO': 2927374164.359991, 'SECRETARIA DE ADMINISTRAÇÃO E GESTÃO DE PESSOAS - ADMINISTRAÇÃO SUPERVISIONADA': 1423178880.4099998, 'GABINETE DE PROJETOS ESPECIAIS': 49267329.5499999, 'SECRETARIA DE MEIO AMBIENTE E SUSTENTABILIDADE': 16978339.089999985, 'SECRETARIA DE ESPORTES - ADMINISTRAÇÃO SUPERVISIONADA': 36543548.96000008, 'SECRETARIA DE GOVERNO E PARTICIPAÇÃO SOCIAL': 135811451.38000026}
    '''

#     print("Gastos totais de 2015 até 2018: {}\nGastos 2015: {}\nGastos 2016: {}\n\
# Gastos 2017: {}\nGastos 2018: {}".format(
#         total_gasto_2015_2018, total_gasto_2015, total_gasto_2016,
#         total_gasto_2017, total_gasto_2018
#     ))

#     print("Total com credor não informado, de 2015 - 2018: {}".format(total_credor_nao_informado))
    
    
    # print("porcentagem credor não informado {}%".format(round((total_credor_nao_informado * (1/100)) / total_gasto_2015_2018 * 10000, 4)))
    # print("Na esquerda, o total de gastos por credor não informado, a direita o gasto total.")
    # plt.bar(range(2), [total_credor_nao_informado, total_gasto_2015_2018])
    # plt.show()


if __name__ == "__main__":
    data_2015 = "data/recife-dados-despesas-2015.csv"
    data_2016 = "data/recife-dados-despesas-2016.csv"
    data_2017 = "data/recife-dados-despesas-2017.csv"
    data_2018 = "data/recife-dados-despesas-2018.csv"
    new_file = "data/dados-2015-2016-2017-2018.csv"
    # retorno = concat(data_2015, data_2016, data_2017, data_2018, True)
    parser(new_file)
