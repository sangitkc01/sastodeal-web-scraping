from bs4 import BeautifulSoup
import requests


final_data=[]
name=input("enter what you want = ")
n=int(input('enter pages = '))
for i in range(1,n+1):
    url=BeautifulSoup(f"https://www.sastodeal.com/catalogsearch/result/index/?p={i}&q={name}","html.parser")
    res=requests.get(url)
    content=res.text
    soup=BeautifulSoup(content,"lxml")

    pants=soup.find_all("div",class_="product details product-item-details")

    for pant in pants:
        pname=pant.find("a",class_="product-item-link").text
        prices=pant.find_all("span",class_="price-container price-final_price tax weee")
        for price in prices:
            newprice=price.find("span",class_="price").text
        l={f"{name} Name ":pname,f"{name} Price ":newprice}
        final_data.append(l)


import pandas as pd

df=pd.DataFrame(final_data)
dff=df.to_csv('pant-data.csv')
print(df)