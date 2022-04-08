from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

page=urllib.request.urlopen("https://www.flipkart.com/search?q=iphone%2013&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup=BeautifulSoup(page,"html.parser")

pname=[]
pprice=[]
pstarrating=[]
pfeatures=[]

for i in soup.findAll("div",class_="_3pLy-c row"):
    getProductName=i.find("div",attrs={"class":"_4rR01T"})
    getPrice=i.find("div",attrs={"class":"_30jeq3 _1_WHN1"})
    getstarrating=i.find("div",attrs={"class":"gUuXy-"})
    getfeatures=i.find("div",attrs={"class":"fMghEO"})

    pname.append(getProductName.text)
    pprice.append(getPrice.text)
    pstarrating.append(getstarrating.text)
    pfeatures.append(getfeatures.text)
data=pd.DataFrame({'product_name':pname,'price':pprice,'star_rating':pstarrating,'features':pfeatures})
print(data.head())

data.to_csv("Filpkart.csv")