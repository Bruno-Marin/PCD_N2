# Importação das bibliotecas pandas, para a manipulação de dados e matplotlib para gerar gráfico.
import pandas as pd
import matplotlib.pyplot as plt

# 1 - Carregando os arquvivos .xlsx produto e compras em dataframes.
df_compras = pd.read_excel('compras.xlsx')
df_produtos = pd.read_excel('produtos.xlsx')

# 2 - Uso da função dropna para eliminar linhas que contenham valores ausentes em no DataFrame. O parâmetro inplace=True indica que a operação deve ser feita diretamente no DataFrame, ou seja, ele será modificado permanentemente.
df_compras.dropna(inplace=True)
df_produtos.dropna(inplace=True)

#conversão para tipos de dados.
df_compras['Quantidade'] = df_compras['Quantidade'].astype(int)
df_compras['Data'] = pd.to_datetime(df_compras['Data'])
df_produtos['Preço'] = df_produtos['Preço'].astype(float)

#3. Calcule o total de vendas de cada produto e crie um gráfico de barras para visualizar os resultados com Matplotlib, ou outra biblioteca de sua escolha.

# Uso da função merge para combinar os df_compras e df_produtos, usando o argumento on='Produto' para indicar que a junção deve usar como base a coluna 'Produto'.
df_compras = df_compras.merge(df_produtos[['Produto', 'Preço']], on='Produto')

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
print('Os 5 principais clientes que fizeram mais compras:\n')
print(top_clientes.to_string(header=True),'\n\n')

plt.bar(top_clientes.index, top_clientes.values, color='blue')
plt.title('Os 5 principais clientes que fizeram mais compras')
plt.xlabel('Cliente')
plt.ylabel('Número de Compras')
plt.xticks(fontsize=8)

#Insere valores nas colunas.
for i, v in enumerate(top_clientes.values):
    plt.text(i, v + -1, str(v), ha='center', va='bottom')
    
plt.show()

#5. Calcule a receita mensal de vendas e crie um gráfico de linha para visualizar a tendência ao longo do tempo (Matplotlib).
df_compras['Data'] = pd.to_datetime(df_compras['Data'])
df_compras['Ano'] = df_compras['Data'].dt.year
df_compras['Mês'] = df_compras['Data'].dt.month

# Juntar as informações de preço ao DataFrame de compras
df_compras = df_compras.merge(df_produtos[['Produto', 'Preço']], on='Produto')

receita_mensal = df_compras.groupby(['Ano', 'Mês'])['Receita'].sum()

# Meses e anos formatados para o eixo x
meses_anos = [f'{str(ano)[-2:]}-{mes}' for ano, mes in receita_mensal.index]

plt.plot(meses_anos, receita_mensal.values, color='red')
plt.title('Receita Mensal de Vendas')
plt.xlabel('Mês e Ano')
plt.ylabel('Receita')

plt.xticks(rotation = 90)
plt.xticks(range(len(meses_anos)),fontsize = 8)

plt.show()

# Print das colunas de mês e ano e dos valores formatados
for mes_ano, valor in zip(meses_anos, receita_mensal.values):
    valor_formatado = "{:,.2f}".format(valor).replace(",", ".")
    print(f'{mes_ano}: R$ {valor_formatado}')
    

# 6. Identifique o produto que gerou a maior receita e calcule a contribuição percentual de suas vendas para a receita total.

produto_maior_receita = vendas_por_produto.idxmax()
receita_total = df_compras['Receita'].sum()
receita_produto_maior = vendas_por_produto.max()
contribuicao_percentual = (receita_produto_maior / receita_total) * 100

print('\nO produto que gerou a maior receita foi:\n', produto_maior_receita,'\n')

contribuicao_formatada = '{:.2f}%'.format(contribuicao_percentual)
print('Sua contribuição percentual para a receita total foi de:\n', contribuicao_formatada,'\n')

# 7. Calcule o preço médio por unidade para cada categoria de produto e exiba os resultados em formato tabular.

preco_medio_por_categoria = df_produtos.groupby('Categoria')['Preço'].mean().reset_index()
print('Preço médio por unidade para cada categoria de produto:\n')
print(preco_medio_por_categoria.to_string(index=False))


# 8. Crie uma análise ou visualização adicional.
# Calcular a receita por categoria

# Juntar as informações de categoria ao dataframe de compras
df_compras = df_compras.merge(df_produtos[['Produto', 'Categoria']], on='Produto')

# Calcular a receita por categoria
receita_por_categoria = df_compras.groupby('Categoria')['Receita'].sum()

# Gráfico de barras
receita_por_categoria.plot(kind='bar', color='green')
plt.title('Receita por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Receita')
plt.xticks(rotation = 0, fontsize = 8)
plt.show()