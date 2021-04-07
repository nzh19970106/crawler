# -*- coding: utf-8 -*-#
globals()

import sys,time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options=Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver=webdriver.Chrome(options=chrome_options)
# driver=webdriver.Chrome(executable_path=r'‪D:\Anaconda3\chromedriver.exe',options=chrome_options)
# driver=webdriver.PhantomJS()
driver.get("https://cn.investing.com/rates-bonds/u.s.-10-year-bond-yield")
element=driver.find_element_by_id("last_last")
print(element.text)
driver.get("https://cn.investing.com/crypto/bitcoin/btc-usd")
print(driver.find_element_by_id("last_last").text)
driver.get("https://cn.investing.com/equities/saic-motor")
print(driver.find_element_by_id("last_last").text)
driver.close()
# ac=ActionChains(driver)
# element=driver.find_elements_by_name("tj_settingicon")
# print(len(element))
# print(element[1].text)
# ac.move_to_element(element[1])
# ac.perform()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# driver.close()
sys.exit()
# driver=webdriver.PhantomJS()
baseurl = 'http://chain.info/'
bitcoinAddress = '3MKjSPE9MsNDnPGxBMYeruhaTBYhadL3E7'
url="https://www.blockchain.com/btc/address/1KKyjDWaSPtKG7yZsV4Vkg4WytwVgw3Lff?page=2"
driver.get(url)
print(driver.current_url)
# print(driver.page_source)
result=driver.find_elements_by_class_name("iWKmuA")
print(result)
print(len(result))
print("hh")
print(result[0].text)

ac=ActionChains(driver)
element=driver.find_elements_by_class_name("iHbBNh")
flag=False
for i in range(len(element)):
    if element[i].text:
        print(element[i].text)
        ac.move_to_element(element[i])
        ac.click().perform()
        flag=True
print("ee")
time.sleep(20)
while flag:
    flag=False
    element=driver.find_elements_by_class_name("iHbBNh")
    for i in range(len(element)):
        if element[i].text:
            print(element[i].text)
            ac.move_to_element(element[i])
            ac.click().perform()
            flag=True
res=driver.find_elements_by_class_name("iWKmuA")
print(res)
print(len(res))
driver.close()
sys.exit()
print(result.get_attribute('href'))
print(result.get_attribute('href').startswith('/btc/block/'))
# /btc/block/000000000000000000045e5bc5e7fea9f9191caaaba52db503b05ef4afee9eb2
driver.close()
import requests
from bs4 import BeautifulSoup
import re
import sys
import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# for i in range(1):
#     print(i)
#     response =requests.get("https://www.blockchain.com/btc/blocks?page="+str(i+1),headers=headers,verify=False)
#     # print(response.content)
#     # <a href="/btc/block/00000000000000000009935b084016f150d6a7ddf7a1388ba7bbd8f4b6527e34" class="sc-1r996ns-0 dkIjuo sc-1tbyx6t-1 fDJjsh iklhnl-0 dBPJKC" opacity="1">0..9935b084016f150d6a7ddf7a1388ba7bbd8f4b6527e34</a>
#     soup=BeautifulSoup(response.content,'lxml')
#     print(type(soup))
#     first=[]
#     pattern='/btc/block/'
#     print(type(soup.find_all('a')))
#     print(len(soup.find_all('a')))
#     for link in soup.find_all('a'):
#         print(link.get('href'))
#     for link in soup.find_all('a'):
#              # print(type(link.get('href')))
#         if link.get('href').startswith(pattern):
#             # print(len(link.get('href').lstrip(pattern)))
#             # sys.exit()
#             first.append(link.get('href').lstrip(pattern))
#     second=[]
#     for i in first:
#         if i not in second:
#             second.append(i)
#     import pandas as pd
#     df=pd.DataFrame(second,columns=['values'])
#     # print(df)
#     # df.to_csv('./1.csv',mode='a',index=False,header=False)
#     print("ok")

response = requests.get("https://www.blockchain.com/btc/address/1KKyjDWaSPtKG7yZsV4Vkg4WytwVgw3Lff?page=2", headers=headers, verify=False)
print(response.content)
soup=BeautifulSoup(response.content,'lxml')
transactions = soup.find_all('div', class_='azsi2v-1 iHbBNg')
i=0
for transaction in transactions:
    eve=transaction.find_all('div',class_='sc-19pxzmk-0 iWKmuA')
    print(len(eve))
    print(eve[1].a.text)
    sys.exit()
    print(transaction.div.a.get_text())
    print(transaction.div.span.get_text())
    sys.exit()
    i=i+1
    if i==14:
        sys.exit()


html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
response=requests.get('https://www.baidu.com',headers=headers)
