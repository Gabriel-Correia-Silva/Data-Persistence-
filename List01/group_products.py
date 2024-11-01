import pandas as pd

data = pd.read_csv('./vendas.csv')

grouped = data.groupby('Produto')

with pd.ExcelWriter('./total_vendas_produto.xlsx') as writer:
    for produto, group in grouped:
        group.to_excel(writer, sheet_name=produto, index=False)

data2 = pd.read_excel('./total_vendas_produto.xlsx', sheet_name=produto)

print(data2)