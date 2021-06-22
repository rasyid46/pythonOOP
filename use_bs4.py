import requests
from bs4 import BeautifulSoup

url = 'https://kompas.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success {response}')
        # print(f'content {response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan url {url}')
        print(f'Title : {soup.title.string}')
    else:
        print(f'ada kesalahan request  {response.status_code}')
except Exception as e:
    print('There is an error ', e)

print('program end')
