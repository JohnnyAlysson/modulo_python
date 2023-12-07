# importar módulo
import pandas as pd #importando p módulo pandas e nomeamos ele "pd" para trabalhar com arquivos excel

#importar base de dados
tabela=pd.read_excel("Vendas.xlsx") #definimos a variavel tabela, que é a leitura da tabela no excel

# visualizar base de dados
pd.set_option("display.max_columns",) #  aumentamos a visualização no terminal, definindo a metodo "set_option(opção,valor) com uma opção e um valor"
print(tabela) #visualizar tabela

# faturamento por loja
# quantidade de produtos vendidos por loja
# ticket medio por produto em cada loja
# enviar um email com relatorio
