# 1º pecorrer todas as pastar de vendas 
import os
import pandas as pd 

lista_arquivos = os.listdir("Vendas")
#print(lista_arquivos)

#2º importar base de vendas 

tabela_total = pd.DataFrame()

for arquivos in lista_arquivos:
       
    if "Vendas" in arquivos:
        tabela = pd.read_csv(f'Vendas/{arquivos}')
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)
        
        

#3º tratar ou fazer a compilação 

#4º realizar calculo de produto mais vendido 

#5º produto que mais faturou


#6º loja que mais vendou em faturamento
