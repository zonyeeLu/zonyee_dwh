from bs4 import BeautifulSoup
import requests

def main():
    # xml_file = open("D:\\temp\\test.xml",'w+',encoding="utf-8")
    res = requests.get('http://www.stat-nba.com/index.php#superstarList')
    res.encoding = 'utf-8'
    # xml_file.write(str(res.text.replace(u'\xa9', u'')))
    soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html')
    res = soup.find_all('div')
    list = get_content(res, 'superstarList', '0pts0')
    for tmp in list:
        print(tmp['卡里姆-贾巴尔'])

def get_content(result,main_tag,sub_tag):
    list = []
    for str in result:
        if str.get('id') == main_tag:
            res1 = str.find_all('div')
            for str1 in res1:
                if str1.get('id') == sub_tag:
                    res2 = str1.find_all('div')
                    for str2 in res2:
                        res3 = str2.find_all('div')
                        for str3 in res3:
                            dict = {}
                            dict[str3.select('a')[0].get_text()]=str3.select('p')[0].get_text()
                            list.append(dict)
    return list
# main
if __name__ == '__main__':
    main()