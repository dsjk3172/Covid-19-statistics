import requests
from bs4 import BeautifulSoup
import pandas as pd
#메인 페이지 확진자 수

datalist =list()
dtlist = list()
url=list()
alltdlist = list()
namelist=list()
titlel=list()

req = requests.get("http://ncov.mohw.go.kr/")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")

tabledate =soup.find('ul', {'class': 'liveNum'})
for tr in tabledate.find_all('li'):
        td = list(tr.find_all('span', {'class' : 'num'}))
        for i in td :
                j = i.text
                j = j.replace(",", "")
                j = j.replace("(누적)", "")
                datalist.append(j)

        data = list(tr.find_all('span', {'class': 'before'}))
        for w in data:
            t = w.text
            t = t.replace("전일대비 (+", "")
            t = t.replace(")", "")
            t = t.replace(" ","")
            dtlist.append(t)

ch = datalist[0]
ho = datalist[2]
dp = datalist[3]
de = dtlist[0]
alltdlist.append([ch, de, ho, dp])

#숫자 리스트 csv 파일로 저장
data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['총 확진자 수','금일 발생','격리 중','사망자수']
data.to_csv('maindata.csv', encoding= 'UTF-8')
print("Complete!")