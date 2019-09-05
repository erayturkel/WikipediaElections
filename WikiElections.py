# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

website_url=requests.get("https://en.wikipedia.org/wiki/2000_United_States_House_of_Representatives_elections#Complete_list").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2000=[]
for table in My_tables[1:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2000.append(rowlist)
            
table2000df=pd.DataFrame(tabledata2000,columns=['Dist', 'incum','incparty','firstelect','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2002_United_States_House_of_Representatives_elections#Complete_list").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2002=[]
for table in My_tables[1:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2002.append(rowlist)
            
table2002df=pd.DataFrame(tabledata2002,columns=['Dist', 'incum','incparty','firstelect','result','cands'])




website_url=requests.get("https://en.wikipedia.org/wiki/2004_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2004=[]
for table in My_tables[1:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2004.append(rowlist)
            
table2004df=pd.DataFrame(tabledata2004,columns=['Dist', 'incum','incparty','firstelect','result','cands'])




website_url=requests.get("https://en.wikipedia.org/wiki/2006_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2006=[]
for table in My_tables[3:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2006.append(rowlist)
            
table2006df=pd.DataFrame(tabledata2006,columns=['Dist','2004 res', 'incum','incparty','firstelect','result','cands'])




website_url=requests.get("https://en.wikipedia.org/wiki/2008_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2008=[]
for table in My_tables[2:]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2008.append(rowlist)
            
table2008df=pd.DataFrame(tabledata2008,columns=['Dist', 'incum','incparty','firstelect','result','cands'])





website_url=requests.get("https://en.wikipedia.org/wiki/2010_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2010=[]
for table in My_tables[4:]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2010.append(rowlist)
            
table2010df=pd.DataFrame(tabledata2010,columns=['Dist', 'incum','incparty','firstelect','result','cands'])





website_url=requests.get("https://en.wikipedia.org/wiki/2012_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2012=[]
for table in My_tables[3:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2012.append(rowlist)
            
table2012df=pd.DataFrame(tabledata2012,columns=['Dist', 'incum','incparty','firstelect','result','cands'])






website_url=requests.get("https://en.wikipedia.org/wiki/2014_United_States_House_of_Representatives_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tabledata2014=[]
for table in My_tables[4:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        for cell in cells:
            rowlist.append(str(cell.text))
        tabledata2014.append(rowlist)
            
table2014df=pd.DataFrame(tabledata2014,columns=['Dist','PVI', 'incum','incparty','firstelect','result','cands'])


table2000df['yr']=2000
table2002df['yr']=2002
table2004df['yr']=2004
table2006df['yr']=2006
table2008df['yr']=2008
table2010df['yr']=2010
table2012df['yr']=2012
table2014df['yr']=2014

table2006df=table2006df.drop(columns='2004 res')
table2014df=table2014df.drop(columns='PVI')

HouseElections = pd.concat([table2000df, table2002df,table2004df,table2006df,table2008df,table2010df,table2012df,table2014df], ignore_index=True)

HouseElections.to_csv('HouseElecs')








website_url=requests.get("https://en.wikipedia.org/wiki/2000_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2000=[]
for table in My_tables[5:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2000.append(rowlist)
            
senate2000=pd.DataFrame(tablesenate2000,columns=['state', 'incum','incparty','firstelect','result','cands'])

senate2000=senate2000.loc[np.r_[7:40],:]




website_url=requests.get("https://en.wikipedia.org/wiki/2002_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2002=[]
for table in My_tables[6:]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2002.append(rowlist)
                   
senate2002=pd.DataFrame(tablesenate2002[2:34],columns=['state', 'incum','incparty','firstelect','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2004_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2004=[]
for table in My_tables[4:]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2004.append(rowlist)
                   
senate2004=pd.DataFrame(tablesenate2004[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])
