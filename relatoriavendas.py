# 1º pecorrer todas as pastar de vendas 
import os
from sys import displayhook
import pandas as pd 

lista_arquivos = os.listdir("Vendas")
#print(lista_arquivos)

#2º importar base de vendas 

tabela_total = pd.DataFrame()

for arquivos in lista_arquivos:
       
    if "Vendas" in arquivos:
        print()
        print('')
        #importar arquivo
        tabela = pd.read_csv(f'Vendas/{arquivos}')
        # print(arquivos)
        # displayhook(tabela)
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
displayhook(tabela_total)
print(arquivos)
displayhook(tabela)

#3º tratar ou fazer a compilação 
#4º realizar calculo de produto mais vendido 
tabela_prduto = tabela_total.groupby('Produto').sum()
tabela_prduto = tabela_prduto[["Quantidade Vendida" , "Primeiro Nome"]]
displayhook(tabela_prduto)

#5º produto que mais faturou


#6º loja que mais vendou em faturamento
