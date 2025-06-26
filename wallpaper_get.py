from wsgiref import headers
import json
import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def load_config():
    """加载配置文件"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("配置文件 config.json 不存在，请先创建配置文件")
        return None
    except json.JSONDecodeError:
        print("配置文件格式错误，请检查JSON格式")
        return None

def main():
    # 加载配置
    config = load_config()
    if not config:
        return
    
    # 从配置文件获取设置
    headers_config = config['headers']
    settings = config['settings']
    proxies_config = config['proxies']
    
    # 设置代理（如果启用）
    proxies = None
    if proxies_config['enabled']:
        proxies = {
            'http': proxies_config['http'],
            'https': proxies_config['https']
        }
    
    ques1 = int(input("请输入你想爬取的页数："))
    pages = []
    print("请输入你想爬取的页码(每输入一页回车)：")
    for n in range(0, ques1, 1):
        p = input()
        pages.append(p)

    # session = requests.Session()

    for page_link in pages:
        url = f"{settings['base_url']}/{settings['category']}/index_{page_link}.htm"
        
        # 使用配置文件中的headers
        hd = headers_config.copy()
        
        # cookies = session.get(url)  # .cookies.get_dict()
        # print(cookies)
        # hd.update(cookies)

        resp = requests.get(url, headers=hd, proxies=proxies)
        resp.encoding = 'gbk'
        # print(resp.text)

        # 创建一个url列表存储要访问的url,创建一个img列表存储壁纸名称
        url_list = []
        bg_name_list = []
        if os.path.isdir(settings['output_dir']):
            pass
        else:
            os.mkdir(settings['output_dir'])

        page = BeautifulSoup(resp.text, 'html.parser')
        alist = page.find('div', class_='list').find_all('a')
        img_name = page.find('div', class_='list').find_all('img')

        f = open(settings['csv_file'], "w", encoding="gbk")
        writer = csv.writer(f)

        i = 0
        for a in alist:
            if i != 2:
                # 把信息写入csv文件中
                writer.writerow([f"{settings['base_url']}{a.get('href').strip()}  {img_name[i].get('alt').strip()}"])
                url_list.append(f"{settings['base_url']}{a.get('href').strip()}")
                bg_name_list.append(img_name[i].get('alt'))
            i += 1
            # 测试
            # break

        j = 0

        # 挨个访问列表里的url
        for URL in url_list:
            url1 = URL
            resp1 = requests.get(url1, headers=hd, proxies=proxies)
            resp1.encoding = 'gbk'
            # 测试
            # print(resp1.text)
            page1 = BeautifulSoup(resp1.text, 'html.parser')
            class_photo = page1.find('div', class_='photops').find('a')
            # 测试
            # print("http://www.netbian.com" + class_photo.get('href'))
            url2 = f"{settings['base_url']}{class_photo.attrs['href']}"
            resp2 = requests.get(url2, headers=hd, proxies=proxies)
            # 测试
            # print(resp2.text)
            page2 = BeautifulSoup(resp2.text, 'html.parser')
            class_photo1 = page2.find('tr').find('a')
            # 测试
            # print(class_photo1.get('href'))
            url3 = class_photo1.get('href')
            resp3 = requests.get(url3, headers=hd, proxies=proxies)

            # bg_name = url3.split('/')[-1]
            img = open(f"{settings['output_dir']}/{bg_name_list[j]}.jpg", "wb")
            img.write(resp3.content)
            print("over!!!  " + bg_name_list[j])
            time.sleep(settings['download_delay'])
            j += 1
            # 关闭文件和网页访问
            img.close()
            resp2.close()
            resp1.close()

        f.close()
        resp.close()

if __name__ == "__main__":
    main()
