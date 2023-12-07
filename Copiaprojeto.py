# importar módulo
import pandas as pd #importando p módulo pandas e nomeamos ele "pd" para trabalhar com arquivos excel

#importar base de dados
tabela=pd.read_excel("Vendas.xlsx") #definimos a variavel tabela, que é a leitura da tabela no excel

# visualizar base de dados #não é obrigatória para o funcionamento
pd.set_option("display.max_columns",None) #  aumentamos a visualização no terminal, definindo o metodo "set_option(opção,valor) com uma opção de todas e um valor"
print(tabela) #visualizar tabela

# faturamento por loja # Soma das vendas por loja
# quantidade de produtos vendidos por loja # Contagem da quantidades do produtos vendidos por loja
# ticket medio por produto em cada loja # faturamento do produto dividido pela quantidade de itens vendidos em cada loja
# enviar um email com relatorio
