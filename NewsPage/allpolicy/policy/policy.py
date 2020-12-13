import requests
from bs4 import BeautifulSoup
import pandas as pd

dtlist = list()
urllist=list()
alltdlist = list()
titlel=list()
#정부정책 일반인(대국민)
#웹페이지 불러오기
req = requests.get("http://ncov.mohw.go.kr/supportPolicyBoardList.do?brdId=5&brdGubun=51")
html = req.text
#원본 소스 파싱
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")
#원본소스에서 li 안의 제목, 작성일자 추출하기
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
#연결된 이미지링크 추출
for trt in tabledate.find_all('span',{'class':'bvc_ttl'}):
    for urlli in trt.find_all('a', {'class': 'bvf_link'}):
        url = urlli.attrs['href']
        url = url.split('=')[-1]
        urllist.append(url)

new_list = []
for v in urllist:
    if v not in new_list:
        new_list.append("http://ncov.mohw.go.kr/shBoardView.do?brdId=5&brdGubun=51&ncvContSeq=" + v)
#추출한 data 리스트로 저장
for i in range(len(titlel)):
    alltdlist.append([titlel[i],dtlist[i],new_list[i]])
# 저장된 리스트 csv 파일로 저장
data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['제목','작성일자','url']
data.to_csv('policy.csv', encoding= 'UTF-8')
print("Complete!")