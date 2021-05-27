import requests
import chardet

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def search(url):
  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    print('request error')
    return
  print(response.text[:100])
  print(chardet.detect(response.content))
  return response.content
 

# TODO
zeze = 'https://www.zeczec.com/projects/blackpower'
if __name__ == '__main__':
  content = search(zeze)
  print(content)
  with open('test.html', 'wb') as f:
    f.write(content)
