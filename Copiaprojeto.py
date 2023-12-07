# importar módulo
import pandas as pd #importando p módulo pandas e nomeamos ele "pd" para trabalhar com arquivos excel

#importar base de dados
tabela=pd.read_excel("Vendas.xlsx") #definimos a variavel tabela, que é a leitura da tabela no excel

# visualizar base de dados
pd.set_option() #
print(tabela)

# faturamento por loja
# quantidade de produtos vendidos por loja
# ticket medio por produto em cada loja
# enviar um email com relatorio
