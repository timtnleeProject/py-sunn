from requeststest import search
from pyquery import PyQuery
import json, codecs

list = []

def parsea_data(raw):
  d = PyQuery(raw)
  elems = d('div.mb4.w-100.w-25-l.w-50-m')
  for el in elems.items():
    titleEl = PyQuery(el.find("h3.mt3.mb0.b"))
    imgEl = PyQuery(el.find("div[data-bg-src]"))
    groupEl = PyQuery(el.find("span.f7"))
    userEl = PyQuery(el.find("span.f7>a"))
    # title
    title = titleEl.text()
    # img
    image = imgEl.attr("data-bg-src")
    # get group
    byIdx = groupEl.text().index(" By ")
    group = groupEl.text()[:byIdx]
    # user
    user_name = userEl.text()
    user_link = userEl.attr("href")
    # type
    icon = PyQuery(el.find("i.material-icons.v-mid"))
    print(icon.next())
    if icon.text() == 'timelapse':
      type = 'sales'
    else:
      type = 'subscription'
    
    info = icon.parents('span').text()
    info = info.replace('timelapse', '')
    info = info.replace('all_inclusive', '')

    # price
    priceEl = PyQuery(el.find("div.w-100.absolute.bottom-0.mb3.black>div:nth-of-type(3)"))
    price = priceEl.text()
    list.append({
      'title': title,
      'image': image,
      'group': group,
      'user': {
        'name': user_name,
        'link': user_link
      },
      'type': type,
      'info': info,
      'price': price
    })

for i in range(10):
  print(f'page {i}')
  url = f'https://www.zeczec.com/categories?page={i + 1}'
  html_content = search(url)
  parsea_data(html_content)

with open("result.json", "wb") as f:
  json.dump(list, codecs.getwriter('utf-8')(f), ensure_ascii=False)