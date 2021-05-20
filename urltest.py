import urllib.parse as up

url = 'https://webpack.js.org/concepts/loaders'
result = up.urlparse(url)
print(result.path.split('/')[-1])

q = '%E4%BD%A0%E5%A5%BD'
print(up.unquote(q))
print(up.quote('測試'))