# Importação das bibliotecas (requests, BeautifulSoup, pandas)
import google.cloud.storage as storage
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Url dos Podcasts
url = site_url

# Função para extração de Título e Link
def get_podcast(url):
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text)
    return soup.findAll('h5')

# Definição de variáveis para captura das infos | Loop se inicia na página 1 (um) e receberá incremento
i=1
list_podcast = []
list_get     = get_podcast(url.format(i))

# Loop com incremento da variável e posterior adição à list_podcast
print(f'Foram coletadas: {len(list_get)} entradas na página: {i}.')
while len(list_get)>0:
    list_podcast += list_get
    i+=1
    list_get     =  get_podcast(url.format(i))
    print(f'Foram coletadas: {len(list_get)} entradas na página: {i}.')

# Divindo em listas de listas com dois elementos para criação do Dataframe:
list_href = [[ep.text, ep.a['href']] for ep in list_podcast]
df = pd.DataFrame(columns=['nome', 'link'], data=list_href)


client = storage.Client()
bucket = client.get_bucket('bucketname')
    
bucket.blob('filename.extension').upload_from_string(df.to_csv(sep = ';', index=False, encoding = 'UTF-8'), 'text/csv')