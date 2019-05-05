# -*- coding: utf-8 -*-
import requests
import json
from lxml import etree

f = open('cs.csv', 'w')
#https://www.ikaoyaner.com/api/pgjg?id=43
#https://www.ikaoyaner.com/api/pgjg?id=44
school211 = []
school985 = []
result = {}

header1 = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'www.ikaoyaner.com',
    'Referer': 'https://www.ikaoyaner.com/pgjg',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
}

r = requests.post('https://daxue.eol.cn/985.shtml')
r.encoding = 'utf-8'
dom = etree.HTML(r.text)
for i in dom.xpath('//html/body/div[3]/div[2]/div[2]/table/tbody/tr'):
    # print(i.xpath('.//td/a/text()'))
    school985.append(i.xpath('.//td/a/text()')[0])
r = requests.post('https://daxue.eol.cn/211.shtml')
r.encoding = 'utf-8'
# print(r.text)
dom = etree.HTML(r.text)
for i in dom.xpath('//html/body/div[3]/div[2]/div[3]/table/tbody/tr'):
    # print(i.xpath('.//td[not(@rowspan)]/a/text()'))
    school211.append(i.xpath('.//td[not(@rowspan)]/a/text()')[0])

r = requests.get('https://www.ikaoyaner.com/api/pgjg?id=44', headers=header1)
data = json.loads(r.text)['data']
details = data['details']
str = "schoolCode"+ "," + "schoolName"+ "," + "subPercent"+ "," + "subRanking"+ "," + "211"+ "," + "985" + "\n"
f.write(str)
for i in details:
    if i['schoolName'] in school211:
        i["211"] = "yes"
    else:
        i["211"] = "no"
    if i['schoolName'] in school985:
        i["985"] = "yes"
    else:
        i["985"] = "no"

    str = i["schoolCode"]+","+i["schoolName"]+","+i["subPercent"]+","+i["subRanking"]+","+i["211"]+","+i["985"]+"\n"
    f.write(str)
# json.dump(details, f)

f.close()
