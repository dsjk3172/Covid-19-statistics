import requests
from bs4 import BeautifulSoup
import pandas as pd

#보도자료전체
datelist =list()
urllist = list()
url=list()
alltdlist = list()
namelist=list()
titlel=list()
urlli=list()
#웹페이지 원본소스 불러오기
req = requests.get("http://ncov.mohw.go.kr/tcmBoardList.do?pageIndex=1&brdId=3&brdGubun=&board_id=&search_item=1&search_content=")
html = req.text
#웹페이지 파싱
soup = BeautifulSoup(html, 'html.parser')
print("--------------------------")
#웹페이지 테이블에서 제목, 담당, 작성일 text로 추출하기
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
                j= j.replace(",", "")
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
#제목 클릭 시 연결할 링크 조합
for k in range(len(urllist)):
    linklist=(('http://ncov.mohw.go.kr/tcmBoardView.do?brdId='
    + str(urllist[k][0]) + '&brdGubun='
    + str(urllist[k][1]) + '&dataGubun=&ncvContSeq='
    + str(urllist[k][2]) + '&contSeq='
    + str(urllist[k][2]) + '&board_id='
    + str(urllist[k][3]) + '&gubun=ALL').replace("'", ""))
    urlli.append(linklist)
print(urlli)
#추출한 data 리스트 만들기
for y in range(len(titlel)):
    alltdlist.append([urlli[y], titlel[y], namelist[y], datelist[y]])
#만든 리스트 csv파일 저장
data = pd.DataFrame(alltdlist)
data.index += 1
data.columns=['','제목','담당','작성일']
data.to_csv('allnews.csv', encoding= 'UTF-8')

print("Complete!")