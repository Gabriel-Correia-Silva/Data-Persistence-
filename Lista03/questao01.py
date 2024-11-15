import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
print("Título da página:", title)

print("\nLinks encontrados:")
for link in soup.find_all('a', href=True):
    print(link['href'])
