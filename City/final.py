#csv 파일의 각 행: 전국 / 서울 / 부산 / 대구 / 인천 / 광주 / 대전 / 울산
#csv 파일의 각 열: 누적 확진 | 신규 확진 | 격리중 | 사망자

from bs4 import BeautifulSoup
import requests
import csv

result = list()

#웹페이지 원본 소스 불러오기
req = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")

#불러온 소스 파싱하기
soup = BeautifulSoup(req.text, 'html.parser')
parsedText = soup.find("tbody")

row = parsedText.findAll('tr')

with open("maindata.csv", 'w', newline='', encoding="utf8") as w:
    writer = csv.writer(w)
    
    for i in range(8):
        r = row[i].findAll("td")
        result.append([r[3].text.replace(",", ""), r[1].text.replace(",", ""), r[4].text.replace(",", ""), r[6].text.replace(",", "")])

    writer.writerows(result)
    result.clear()