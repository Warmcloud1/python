import requests
from bs4 import BeautifulSoup
import json
url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E8%9E%A2%E5%B9%95&page=1&sort=sale/dc"
res=requests.get(url)
data=json.loads(res.text)
webdatas = data['prods']
for product in webdatas:
    print(product['name'])
    print(product['price'])
    
