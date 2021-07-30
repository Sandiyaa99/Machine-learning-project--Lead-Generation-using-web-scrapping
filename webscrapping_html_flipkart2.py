#web scrapping using html parser method
from bs4 import BeautifulSoup as bs
import requests

link='https://www.flipkart.com/portronics-harmonics-216-bluetooth-headset/product-reviews/itm56304ccc8e996?pid=ACCFHHWUEXCFBMST&lid=LSTACCFHHWUEXCFBMSTGHSLHL&marketplace=FLIPKART'

page=requests.get(link)
page
page.content

soup=bs(page.content,'html.parser')
soup
soup.prettify()

'''names=soup.find_all('span',class_='a-profile-name')

cust_name=[]
for i in range(0,len(names)):
    cust_name.append(names[i].get_text())
cust_name
    
cust_name.pop(0)

cust_name'''

title=soup.find_all('p',class_='_2-N8zT')
title

review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title

'''review_title[:]=[titles.lstrip('\n')for titles in review_title]
review_title

review_title[:]=[titles.rstrip('\n')for titles in review_title]
review_title'''

rating=soup.find_all('div',class_='_3LWZlK _1BLPMq')
rating

rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate

#rate.pop(0)

rate

review=soup.find_all('div',class_='t-ZTKy')
review

review_content=[]
for i in range(0,len(review)):
    review_content.append(review[i].get_text())
review_content

'''review_content[:]=[reviews.lstrip('\n')for reviews in review_content]
review_content

review_content[:]=[reviews.rstrip('\n')for reviews in review_content]
review_content'''

#cust_name
review_title
rate
review_content

import pandas as pd

df=pd.DataFrame()

#df['Customer_Name']=cust_name
df['Review_title']=review_title
df['Ratings']=rate
df['Reviews']=review_content

df
df.to_csv(r'F:\MLP_SPYDER\headset_review2.csv',index=True)
    