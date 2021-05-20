def hello(v):
  for i in [0,1,2,3]:
    if i % 2 == 0:
      print(f'hello: %s {i}')

if __name__ == '__main__':
  hello(__name__)

# String
str = 'hello world'

# List
list = [0,1,2,3]

# Dictionary
dic = {'a':0,'b':1,'c':2}
print(dic.values())
print(dic.items())
# Tuple
(0,1,2)

# List/String slice
print(list[1:3])
print(str[-5:]) # slice 可以負數 從後面數
print(str[3])
print(str[-3])

## filter
c = [0,1,2,3,4,5,6]
odds = [i for i in c if i % 2 != 0]
print(odds)

list = [{
  'name': '001',
  'price': 20
},{
  'name': '002',
  'price': 80
},{
  'name': '003',
  'price': 150
},{
  'name': '004',
  'price': 10
}]

print([
  l['name']
  for l in list
  if l['price'] < 30
])