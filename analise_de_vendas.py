# Importação das bibliotecas pandas, para a manipulação de dados e matplotlib para gerar gráfico.
import pandas as pd
import matplotlib.pyplot as plt

# 1 - Caregando os arquvivos xlsx produto e compras em dataframes.
df_compras = pd.read_excel('compras.xlsx')
df_produtos = pd.read_excel('produtos.xlsx')

# 2 - Uso da função dropna para eliminar linhas que contenham valores ausentes em no DataFrame. O parâmetro inplace=True indica que a operação deve ser feita diretamente no DataFrame, ou seja, ele será modificado permanentemente.
df_compras.dropna(inplace=True)
df_produtos.dropna(inplace=True)

# Uso da função merge para combinar os df_compras e df_produtos, usando o argumento on='Produto' para indicar que a junção deve usar como base a coluna 'Produto', how='left' para preservar todas as linhas do dataframe.
df_compras = df_compras.merge(df_produtos[['Produto', 'Preço']], on='Produto', how='left')

#Criação da coluna 'Receita' e a multiplicação das colunas 'Quantidade' e 'Preço'.
df_compras['Receita'] = df_compras['Quantidade'] * df_compras['Preço']

# Uso da função groupby para unir valores da coluna produto e a função sum para somar o valores da coluna quantidade.
df_compras = df_compras.groupby('Produto')['Quantidade','Receita'].sum()

df_compras.plot(kind='bar', y='Receita', width=0.8)
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Quantidade de Vendas')
plt.yticks(fontsize=10)
plt.tight_layout(pad=0.5)
plt.show()

