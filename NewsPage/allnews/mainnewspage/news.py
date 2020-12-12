import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

datelist =list()
urllist = list()
url=list()
alltdlist = list()
namelist=list()
titlel=list()
urlli = list()
#보도자료

req = requests.get("http://ncov.mohw.go.kr/tcmBoardList.do?brdId=&brdGubun=&dataGubun=&ncvContSeq=&contSeq=&board_id=140&gubun=")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")

tabletr = soup.findAll('a', {'class': 'bl_link'})
for link_tag in tabletr:
    url.append(link_tag["onclick"])
for i in range(len(url)):
    urllist.append(url[i].split(',')[1:5])

tabledate =soup.find('table')
for tr in tabledate.find_all('tr'):
        td = list(tr.find_all('td'))

        for i in td :
            if i.find('a'):
                j = i.find('a').text
                j = j.replace(",", "")
                titlel.append(j)
                dat = td[3].text
                datelist.append(dat)
                name = td[2].text
                namelist.append(name)

                url.append(link_tag["onclick"])
print(url)
for w in range(len(url)):
    urllist.append(url[w].split(','))
print(urllist)

for k in range(len(urllist)):
    linklist=(('http://ncov.mohw.go.kr/tcmBoardView.do?brdId=&brdGubun=&dataGubun=&ncvContSeq='
    +str(urllist[k][2])+'&contSeq='
    +str(urllist[k][2])+'&board_id=140&gubun=BDJ').replace("'",""))
    urlli.append(linklist)
print(urlli)
for y in range(len(titlel)):
    alltdlist.append([urlli[y], titlel[y], namelist[y], datelist[y]])

data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['','제목','담당','작성일']
data.to_csv('news.csv', encoding= 'UTF-8')
print("Complete!")