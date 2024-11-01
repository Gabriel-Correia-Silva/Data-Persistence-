import pandas
import pandas as pd

data = pd.read_csv('./vendas.csv')


data["Total"] = data["Quantidade"] * data["Preco_Unitario"]

data.to_csv('./vendas.csv', index=False)

print(data)