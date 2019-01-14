import requests
import re
import time
from bs4 import BeautifulSoup as sp
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"
    }
def loadPage(url):
    response = requests.get(url=url, headers=headers)
    response = response.content.decode('gbk')
    return response
def getLink(url):
    imList = []  # 用来存放图片链接
    content = loadPage(url)
    # html = sp(content, 'html.parser')
    html = sp(content, 'html.parser')
    for link in html.find_all('ul', attrs={'id':'Tag_list'}):
        link = link.find_all('a', attrs={'target':'_blank'})
        for link1 in link:
            link1 = link1.get('href')
            imList.append(link1)
            # rint(link1)
    return imList

def loadImage():
    for j in range(3):
        j += 2
        urlLink = 'https://www.27270.com/tag/333'
        urlLink = urlLink + '_' + str(j) + '.html'
        print("正在爬取第%d页" % j)
        imLinks=getLink(urlLink)
        for imLink in imLinks:
            for i in range(40):
                i += 1
                imLink1 = imLink[0:-5]
                imLink2 = imLink1 + '_' + str(i) + '.html'
                print(imLink2)
                content = loadPage(imLink2)
                html = sp(content, 'html.parser')
                try:
                    link = html.find_all('img', attrs={'alt':True,'height':False})[0]
                    time.sleep(3)
                    # print(link)
                    if link is None:
                        print("爬取完成")
                        pass
                    else:
                        name1 = link.get('alt')
                        name1 = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", name1)
                        link1 = link.get('src')
                        name1 = name1 + str(i)
                        print('正在爬取' + name1)
                        saveImage(link1,name1)
                except:
                    print("爬取完成")
                    break
def saveImage(imglink, name):
    filename ='E:\\pythonstudy\\meinv\\' + name + '.jpg'
    # print(filename)
    img = requests.get(imglink)
    img = img.content
    with open(filename, 'wb') as f:
        f.write(img)


if __name__ == '__main__':
   loadImage()