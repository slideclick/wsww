# -*- coding: UTF-8 -*-
#python 3
import lxml.html
import requests
import datetime
import csv


url='http://www.bjjs.gov.cn/bjjs/fwgl/fdcjy/fwjy/index.shtml'
headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0',
    }
)#http://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python

result = requests.get(url, headers=headers)
html = result.text

tree=lxml.html.fromstring(html)
divs=((tree.cssselect('div.fwgl_content')[0]).getchildren())[1]
clfwsqw=divs.getchildren()[1].getchildren()[1]
tb=clfwsqw.cssselect('table')[1]
filter=1
result=[]
for c in tb.xpath('//tr/td/table/tr[@bgcolor="#f9f4e8"]/td[@width="35%"]'):
    filter +=1
    if filter%4 == 0:
        (result.append(int(c.text.strip())))
print(result)        
with open('cfdcsjtj.csv','a',encoding='utf-8') as csvFile:   
    csvout = csv.writer(csvFile)
    now =   datetime.date.today()#utcnow()
    result.append(now.isoformat())#strftime()
    #line= str(result)[1:-1]
    csvout.writerow(result)#print(line,file=csvFile,end='\n')         