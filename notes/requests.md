# requests

```python
import requests

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

url = 'https://www.zeczec.com/categories'
response = requests.get(url, headers=headers)
if response.status_code != 200:
  print('request error')
  return
print(response.text)
with open('test.html', 'wb') as f:
  f.write(response.content)
```

`response.text` 會用 content-type 編碼來解析，但有時候網站內容編碼和 content-type會不一樣

此時要使用 `response.content` (抓圖片也是)