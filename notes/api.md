## json
```python
import json
jsonRow = '{"name": "hello"}'
obj = {'a':1,'b':2}
json.loads(jsonRow)
json.dumps(obj)
```

## url

### parse

```python
import urllib.parse as up

url = 'https://webpack.js.org/concepts/loaders'
result = up.urlparse(url)
print(result.path.split('/')[-1])
```

### encode/decode

```python
import urllib.parse as up
q = '%E4%BD%A0%E5%A5%BD'
up.unquote(q)
up.quote('測試')
```
