import requests
from bs4 import BeautifulSoup
import json
url ="https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E8%9E%A2%E5%B9%95&page=1&sort=sale/dc"
res=requests.get(url)       '''讀網站內文'''
data=json.loads(res.text)   '''改成json檔'''
webdatas = data['prods']
for product in webdatas:
    print(product['name'])
    print(product['price'])
    
