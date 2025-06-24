from wsgiref import headers

import requests
from bs4 import BeautifulSoup
import csv
import time
import os

ques1 = int(input("请输入你想爬取的页数："))
pages = []
print("请输入你想爬取的页码(每输入一页回车)：")
for n in range(0, ques1, 1):
    p = input()
    pages.append(p)

# session = requests.Session()

for page_link in pages:
    url = "http://www.netbian.com/dongman/index_" + page_link + ".htm"
    hd = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
        'Cookie': 'cf_clearance=lFwZEjrhK4_NrtSf1nXXqb3reqlvXIilccTqaVdBu4Q-1741871113-1.2.1.1-U3AQW6xJXgTp8SHUfSQkD8inLbvijd0vq9HY9TfytGbz_mn5vqBechHtKatWNFupWCpWso1Y_yirnKFIBg8Iy7VMFMp9ueGGBjxUQbELsVBqKOz3ox1YivcATwusirkZBNnQ1xuKVD4jMLL2jVJUq_EgvlHJPZyZJ.5kOvpWYfP6kXteAa7.ms_Z1MZmOXavHUPSvYOG0BZFZc0U6eI57cUGCtJ5JMVuTIfVJJAjRrJ87cke6LbGQs9PelObFhUL9q2ByvUP4dox9ofL52ECAh_IrCjZ62MDdpB4vRxBaAj6KkpQDVkeq6Pj0jwoowyb0us8CPOrY4vZyPwluCV_9oLrg.P93tn4Btt8sCRx8Ev.153SD_AwlZsBQ08nIU1URnW84DJrxZW2Khao_Kvc_YJ05fl.HELyyY_Llw._u5E; trenvecookieclassrecord=%2C19%2C',
        # 'Host': 'www.netbian.com'
    }
    # cookies = session.get(url)  # .cookies.get_dict()
    # print(cookies)
    # hd.update(cookies)

    # 使用代理切换IP
    # proxies = {
    #     'http': '106.15.194.169:9100'
    # }

    resp = requests.get(url, headers = hd)
    resp.encoding = 'gbk'
    # print(resp.text)

    # 创建一个url列表存储要访问的url,创建一个img列表存储壁纸名称
    url_list = []
    bg_name_list = []
    if os.path.isdir("wallpapers"):
        pass
    else:
        os.mkdir("wallpapers")

    page = BeautifulSoup(resp.text, 'html.parser')
    alist = page.find('div', class_='list').find_all('a')
    img_name = page.find('div', class_='list').find_all('img')

    f = open("wallpapers_ifmt.csv", "w", encoding="gbk")
    writer = csv.writer(f)

    i = 0
    for a in alist:
        if i != 2:
            # 把信息写入csv文件中
            writer.writerow(["http://www.netbian.com"+a.get('href').strip() + "  " + img_name[i].get('alt').strip("\n")])
            url_list.append("http://www.netbian.com"+a.get('href').strip())
            bg_name_list.append(img_name[i].get('alt'))
        i += 1
        # 测试
        # break

    j = 0

    # 挨个访问列表里的url
    for URL in url_list:
        url1 = URL
        resp1 = requests.get(url1, headers = hd)
        resp1.encoding = 'gbk'
        # 测试
        # print(resp1.text)
        page1 = BeautifulSoup(resp1.text, 'html.parser')
        class_photo = page1.find('div', class_='photops').find('a')
        # 测试
        # print("http://www.netbian.com" + class_photo.get('href'))
        url2 = "http://www.netbian.com"+class_photo.attrs['href']
        resp2 = requests.get(url2, headers = hd)
        # 测试
        # print(resp2.text)
        page2 = BeautifulSoup(resp2.text, 'html.parser')
        class_photo1 = page2.find('tr').find('a')
        # 测试
        # print(class_photo1.get('href'))
        url3 = class_photo1.get('href')
        resp3 = requests.get(url3, headers = hd)

        # bg_name = url3.split('/')[-1]
        img = open("wallpapers/" + bg_name_list[j] + ".jpg", "wb")
        img.write(resp3.content)
        print("over!!!  " + bg_name_list[j])
        time.sleep(1)
        j += 1
        # 关闭文件和网页访问
        img.close()
        resp2.close()
        resp1.close()

    f.close()
    resp.close()
