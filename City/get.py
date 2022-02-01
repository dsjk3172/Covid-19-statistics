#csv 파일의 각 행: 전국 / 서울 / 부산 / 대구 / 인천 / 광주 / 대전 / 울산
#csv 파일의 각 열: 확진 누적 | 신규 확진 | 격리 해제 누적 | 사망 누적

from bs4 import BeautifulSoup
import requests
import csv

temp1 = list()
temp2 = list()
result = list()
count = 0
findresult = ["전국", "서울", "부산" , "대구" , "인천" , "광주" , "대전" , "울산"]

#웹페이지 원본 소스 불러오기
req = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")

#불러온 소스 파싱하기
soup = BeautifulSoup(req.text, 'html.parser')

parsedText = soup.find_all('ul', {'class': 'cityinfo total'})
for i in parsedText:
    for j in i.findAll('span', {'class': 'num'}):
        j = j.text
        j = j.replace(",", "")
        temp1.append(j)

    for j in i.findAll('span', {'class': 'sub_num red'}):
        j = j.text
        j = j.replace(",", "")
        j = j.replace("(", "")
        j = j.replace(")", "")
        j = j.replace("+", "")
        temp2.append(j)

result.append([temp1[3], temp2[1], 629487, temp1[0]])
temp1 = list()
temp2 = list()

parsedText = soup.find_all('ul', {'class': 'cityinfo subset'})
for i in parsedText:
    for j in i.findAll('span', {'class': 'num'}):
        j = j.text
        j = j.replace(",", "")
        temp1.append(j)

    for j in i.findAll('span', {'class': 'sub_num red'}):
        j = j.text
        j = j.replace(",", "")
        j = j.replace("(", "")
        j = j.replace(")", "")
        j = j.replace("+", "")
        temp2.append(j)

    result.append([temp1[0], temp2[0], temp1[1], temp1[2]])
    temp1 = list()
    temp2 = list()

    count += 1
    if(count == 7):
        break;



for i in parsedText:
    j = i.text
    print(j)
print(result)

with open("maindata.csv", 'w', newline='', encoding="utf8") as w:
    writer = csv.writer(w)
    writer.writerows(result)

print("complete!")