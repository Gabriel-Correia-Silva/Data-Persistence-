import pandas
import pandas as pd

data = pd.read_csv('./vendas.csv')

data = data[data['Data'].str.contains('01/2023')]

data.to_csv('./vendas_janeiro.csv', index=False)
print(data)