import requests

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def search(url):
  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print('request error')
    return
  print(response.text)
  with open('test.html', 'wb') as f:
    f.write(response.content)

zeze = 'https://www.zeczec.com/categories'
if __name__ == '__main__':
  search('https://blog.timtnlee.me/')
