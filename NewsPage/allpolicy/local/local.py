import requests
from bs4 import BeautifulSoup
import pandas as pd
#지역주민
dtlist = list()
urllist=list()
alltdlist = list()
titlel=list()

req = requests.get("http://ncov.mohw.go.kr/supportPolicyBoardList.do?brdId=5&brdGubun=55")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")

tabledate =soup.find('div', {'class': 'faq_list'})
for tr in tabledate.find_all('li'):
    td = tr.find('a')
    if td != None :
        tt = td.find('span', {'class': 'fl_ttl'})
        if tt != None :
            tt = tt.text
            tt = tt.replace("/n", "")
            tt = tt.replace("/t", "")
            tt = tt.replace(",","")
            tt = tt.rstrip()
            titlel.append(tt)

        tda = td.find('span', {'class': 'list_date'})
        if tda != None :
            tda = tda.text
            date =tda
            dtlist.append(tda)

for trt in tabledate.find_all('span',{'class':'bvc_ttl'}):
    for urlli in trt.find_all('a', {'class': 'bvf_link'}):
        url = urlli.attrs['href']
        url = url.split('=')[-1]
        urllist.append(url)

new_list = []
for v in urllist:
    if v not in new_list:
        new_list.append("http://ncov.mohw.go.kr/shBoardView.do?brdId=5&brdGubun=55&ncvContSeq=" + v)

for i in range(len(titlel)):
    alltdlist.append([titlel[i],dtlist[i],new_list[i]])

data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['제목','작성일자','url']
data.to_csv('local.csv', encoding= 'UTF-8')
print("Complete!")