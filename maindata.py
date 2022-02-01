import requests
from bs4 import BeautifulSoup
import pandas as pd
#메인 페이지 확진자 수

datalist1 =list()
datalist2 =list()
url=list()
alltdlist = list()
namelist=list()
titlel=list()

req = requests.get("http://ncov.mohw.go.kr/")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")

tabledata = soup.find('div', {'class': 'occurrenceStatus'})
for tr in tabledata.find_all('div', {'class': 'box'}):
        td = list(tr)
        for i in td :
                j = i.text
                datalist1.append(j)

tabledata = soup.find('div', {'class': 'occur_graph'})
tr = tabledata.find("tbody")
tr = tr.find("tr")
for i in tr.find_all('span'):
        i = i.text
        datalist2.append(i)

alltdlist.append([datalist1[3], datalist2[4], datalist2[3], datalist1[1]])

#숫자 리스트 csv 파일로 저장
data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['누적 확진','일일 확진자','신규 입원','누적 사망']
data.to_csv('maindata.csv', encoding= 'UTF-8')
print("Complete!")