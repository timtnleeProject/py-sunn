# Python, 拍ㄙㄣˋ

## string, print

%s: 字串
%d: 整數

```python
i = 10
j = 'test'
print('i = %d, j = %s' % (i, j))
```

### f-string (python 3.6 之後)

```python
i = 10
j = 'test'
print(f'i = {i}, j = {j}')
```

### raw-string

跳脫字元視為 string

```python
print('C:\\Window\\Download')
# raw string
print(r'C:\Window\Download')
print(r'\n')
```

## Slice

```python
# String
str = 'hello world'
# List
list = [0,1,2,3]

# List/String slice
list[1:3] # [1,2]
str[-5:] # world
str[3] # l
str[-3] # r
```

## Filter

```python
c = [0,1,2,3,4,5,6]
odds = [
  i
  for i in c
  if i % 2 != 0
]
# or
odds = [i for i in c if i % 2 != 0]
```

```python
list = [{
  'name': '001',
  'price': 20
},{
  'name': '002',
  'price': 80
}]

cheap = [
  l['name']
  for l in list
  if l['price'] < 30
]
```

## dictionary

```python
dictionary.values()
dictionary.items()
```

## in

```python
if char in string:
  # ...
if item in list:
  # ...
if key in dictionary:
  # ...
if value in dictionary.values():
  # ...
```