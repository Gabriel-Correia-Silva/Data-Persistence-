import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./vendas.csv')

data.head()

total_vendas = data.groupby('Produto')['Quantidade'].sum()

total_vendas.head()
total_vendas.plot(kind='bar')

data.plot(kind='bar')
plt.show()  
 
data["Quantidade"].plot()
plt.show()