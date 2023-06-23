# Importação das bibliotecas pandas, para a manipulação de dados e matplotlib para gerar gráfico.
import pandas as pd
import matplotlib.pyplot as plt

# 1 - Caregando os arquvivos xlsx produto e compras em dataframes.
df_compras = pd.read_excel('compras.xlsx')
df_produtos = pd.read_excel('produtos.xlsx')

# 2 - Uso da função dropna para eliminar linhas que contenham valores ausentes em no DataFrame. O parâmetro inplace=True indica que a operação deve ser feita diretamente no DataFrame, ou seja, ele será modificado permanentemente.
df_compras.dropna(inplace=True)
df_produtos.dropna(inplace=True)

#3. Calcule o total de vendas de cada produto e crie um gráfico de barras para visualizar os resultados com Matplotlib, ou outra biblioteca de sua escolha.

# Uso da função merge para combinar os df_compras e df_produtos, usando o argumento on='Produto' para indicar que a junção deve usar como base a coluna 'Produto', how='left' para preservar todas as linhas do dataframe.
df_compras = df_compras.merge(df_produtos[['Produto', 'Preço']], on='Produto', how='left')

#Criação da coluna 'Receita' e a multiplicação das colunas 'Quantidade' e 'Preço'.
df_compras['Receita'] = df_compras['Quantidade'] * df_compras['Preço']

# Uso da função groupby para unir valores da coluna produto e a função sum para somar o valores da coluna quantidade.

vendas_por_produto = df_compras.groupby('Produto')['Receita'].sum()

#Gráfico de barras.
vendas_por_produto.plot(kind='bar', y='Receita', width=0.8)
plt.title('Total de Vendas por Produto')
plt.xlabel('Produto')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Quantidade de Vendas')
plt.yticks(fontsize=10)
plt.show()

# 4. Determine os 5 principais clientes que fizeram mais compras e exiba seus nomes junto com o número de pedidos que fizeram.
top_clientes = df_compras['Cliente'].value_counts().head(5)
print('Os 5 principais clientes que fizeram mais compras:')
print(top_clientes)

plt.bar(top_clientes.index, top_clientes.values, color='blue')
plt.title('Os 5 principais clientes que fizeram mais compras')
plt.xlabel('Cliente')
plt.ylabel('Número de Compras')
plt.xticks(fontsize=8)

for i, v in enumerate(top_clientes.values):
    plt.text(i, v + -1, str(v), ha='center', va='bottom')
    
plt.show()



# 6. Identifique o produto que gerou a maior receita e calcule a contribuição percentual de suas vendas para a receita total.

# 7. Calcule o preço médio por unidade para cada categoria de produto e exiba os resultados em formato tabular.

# 8. Crie uma análise ou visualização adicional, que achar interessante ou relevante, para o conjunto de dados