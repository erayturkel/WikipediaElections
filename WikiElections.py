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



website_url=requests.get("https://en.wikipedia.org/wiki/2006_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2006=[]
for table in My_tables[4:5]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2006.append(rowlist)
                   
senate2006=pd.DataFrame(tablesenate2006[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2008_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2008=[]
for table in My_tables[6:7]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2008.append(rowlist)
                   
senate2008=pd.DataFrame(tablesenate2008[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2010_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2010=[]
for table in My_tables[9:10]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2010.append(rowlist)
                   
senate2010=pd.DataFrame(tablesenate2010[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])




website_url=requests.get("https://en.wikipedia.org/wiki/2012_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2012=[]
for table in My_tables[4:5]:
    for row in table.findAll('tr'):
        rowlist=[]
        title=row.findAll(['th'])
        title=title[0].text
        rowlist.append(title)
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2012.append(rowlist)
                   
senate2012=pd.DataFrame(tablesenate2012[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])





website_url=requests.get("https://en.wikipedia.org/wiki/2014_United_States_Senate_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablesenate2014=[]
for table in My_tables[6:7]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablesenate2014.append(rowlist)
                   
senate2014=pd.DataFrame(tablesenate2014[2:35],columns=['state', 'incum','incparty','firstelect','result','cands'])



senate2000['yr']=2000
senate2002['yr']=2002
senate2004['yr']=2004
senate2006['yr']=2006
senate2008['yr']=2008
senate2010['yr']=2010
senate2012['yr']=2012
senate2014['yr']=2014

SenateElections = pd.concat([senate2000, senate2002,senate2004,senate2006,senate2008,senate2010,senate2012,senate2014], ignore_index=True)

SenateElections.to_csv('SenateElects')






website_url=requests.get("https://en.wikipedia.org/wiki/2000_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2000=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2000.append(rowlist)
            
gov2000=pd.DataFrame(tablegov2000,columns=['state', 'incum','incparty','result','cands'])




website_url=requests.get("https://en.wikipedia.org/wiki/2002_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2002=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2002.append(rowlist)
            
gov2002=pd.DataFrame(tablegov2002,columns=['state', 'incum','incparty','result','cands'])

website_url=requests.get("https://en.wikipedia.org/wiki/2004_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2004=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2004.append(rowlist)
            
gov2004=pd.DataFrame(tablegov2004,columns=['state', 'incum','incparty','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2006_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2006=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2006.append(rowlist)
            
gov2006=pd.DataFrame(tablegov2006,columns=['state', 'incum','incparty','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2008_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2008=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2008.append(rowlist)
            
gov2008=pd.DataFrame(tablegov2008,columns=['state', 'incum','incparty','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2010_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2010=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2010.append(rowlist)
            
gov2010=pd.DataFrame(tablegov2010,columns=['state', 'incum','incparty','result','cands'])



website_url=requests.get("https://en.wikipedia.org/wiki/2012_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2012=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2012.append(rowlist)
            
gov2012=pd.DataFrame(tablegov2012,columns=['state', 'incum','incparty','result','cands'])


website_url=requests.get("https://en.wikipedia.org/wiki/2014_United_States_gubernatorial_elections").text
soup=bs(website_url, 'lxml')

My_tables = soup.find_all('table',{'class':'wikitable'})

tablegov2014=[]
for table in My_tables[0:1]:
    for row in table.findAll('tr'):
        rowlist=[]
        cells=row.findAll('td')
        for cell in cells:
            rowlist.append(str(cell.text))
        tablegov2014.append(rowlist)
            
gov2014=pd.DataFrame(tablegov2014,columns=['state', 'incum','incparty','result','cands'])




gov2000['yr']=2000
gov2002['yr']=2002
gov2004['yr']=2004
gov2006['yr']=2006
gov2008['yr']=2008
gov2010['yr']=2010
gov2012['yr']=2012
gov2014['yr']=2014

GovElections = pd.concat([gov2000, gov2002,gov2004,gov2006,gov2008,gov2010,gov2012,gov2014], ignore_index=True)

GovElections.to_csv('GovElections')

