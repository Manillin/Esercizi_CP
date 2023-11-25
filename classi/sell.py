import requests
from bs4 import BeautifulSoup

# URL della pagina web
url = "https://www.ebay.it/sl/prelist"

testo_da_inserire = "Ciao, questo è il testo da inserire!"
target = 'textbox se-search-box__field textbox--icon-end'

response = requests.get(url)
str = str(response.text)

'''soup = BeautifulSoup(str, 'html.parser')
casella_di_testo = soup.find('div')

print(casella_di_testo.get_text())'''

if target in str:
    print("SIIII")
else:
    print("NOOO")
