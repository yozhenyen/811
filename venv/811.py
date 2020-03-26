import re
import urllib.request
import pandas as pd
import tag as tag
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument("--headless")
htp='http://www15.plala.or.jp/gcap/disney/realtime.htm'
#ur=urllib.request.urlopen(htp)
#beauti=BeautifulSoup(ur)
#print(beauti.prettify())
wherename='C:/Users/Asus/Desktop/chromedriver'
driver=webdriver.Chrome(wherename,chrome_options=chrome_options)
driver.get(htp)

soup=BeautifulSoup(driver.page_source,"html.parser")
title=[tag.get('onclick') for tag in soup.find_all("td",{'class':'FPh2'})]

login_form=driver.find_element_by_xpath("//td[contains(@onclick,'createAT2(1)')]")
soap=driver.page_source


data=pd.read_html(soap)
a=data[22]
a.to_csv('C:/Users/Asus/Desktop/專題/0828.csv',index=False)
driver.close()
print(login_form)



#soap_first=driver.page_source
#soup_first=BeautifulSoup(soap_first)
#print(soup_first.prettify())
#titlename=(soup_first.find_all('td',attrs={'class':re.compile("32.ｽﾍﾟｰｽ･ﾏｳﾝﾃﾝ")}))
#titlename=soup_first.find('td',attrs={'class':re.compile("FPh2")})
#gettitle=titlename.get('title')
#driver.find_element_by_class_name('FPh2').click()

#jamat > table > tbody > tr:nth-child(4) > td:nth-child(32) > span
