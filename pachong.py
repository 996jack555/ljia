import requests, time, re, csv
from bs4 import BeautifulSoup
import codecs

#with open('静安.csv', 'w')as fp:
#    fp.write(codecs.BOM_UTF8)

Flag = 1 
    
f = open('zjl连云港.csv','w',newline='', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(('名称', '租金', '面积', '具体地址', '门朝向', '户型', '地区'))
f.close()
urls = ['https://lyg.lianjia.com/zufang/pg{}/#contentList'.format(str(i)) for i in range(1, 100)]

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
}
for url in urls:
    #time.sleep(3)
    res = requests.get(url, headers=headers)
# print(res.text)  网页内容  文本
# print(res.content.decode('utf-8'))  #网页内容 二进制
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
# print(soup)
    infos = soup.find('div',{'class':'content__list'}).find_all('div',{'class':'content__list--item'})
    #print(infos)
    f = open('zjl连云港.csv','a',newline='', encoding='utf-8')
    writer = csv.writer(f)
    for info in infos:
        #print(type(info))
        #info = str(info)
        #print(type(info))
        #name = info.find('a',{'class': 'twoline'}).get_text()   #南京连云港
        name = info.find('p',{'class': 'content__list--item--title'}).get_text()#南通
        
        #print(name+"aaaaaaa")
        #print(info)
        #name = info.find("title=").get_text()
        #print(name)
        #name = name.find('a').get_text()
        #print(name)
        name = name.strip()
        price = info.find('span',{'class': 'content__list--item-price'}).get_text()
        mix = info.find('p', {'class': 'content__list--item--des'}).get_text()
        #print("mix = " + mix)
        mix = re.split(r'/', mix)
        #print(mix)
        #if(mix[0].find("精选")!=None):
        #    mix.pop(0)
        #print("删除后")
        #print(mix)
        
        #print(mix)
        #print(len(mix) , mix)
        #南京连云港南通（屏蔽不完善的内容）
        if (len(mix) <= 4):
            continue
        mix.reverse()
        area = mix[3].strip()
        address = mix[4].strip()
        door_orientation = mix[2].strip()
        style = mix[1].strip()
        # advantage = info.find('p',{'class':'content__list--item--bottom oneline'}).get_text()
        region = re.split(r'-', address)[0]
        #print("mix0 =  "  + str(len(mix[0])) + "mix 1 = " + mix[1] + "mix 2 = " + mix[2] + " mix[3] = " + mix[3])
        writer.writerow( ( name , price, area, address, door_orientation, style, region ) )
        #print(name , price, area, address, door_orientation, style, region)
        print("增加数据",Flag)
        Flag = Flag + 1
        f.flush()
        #time.sleep(1)
        
        """南通
        print(mix)
        area = mix[1].strip()
        address = mix[0].strip()
         mix = mix[2,-1]
        mix.reverse()
        door_orientation = mix[2].strip()
        style = mix[1].strip()
        # advantage = info.find('p',{'class':'content__list--item--bottom oneline'}).get_text()
        region = re.split(r'-', address)[0]
        #print("mix0 =  "  + str(len(mix[0])) + "mix 1 = " + mix[1] + "mix 2 = " + mix[2] + " mix[3] = " + mix[3])
        writer.writerow( ( name , price, area, address, door_orientation, style, region ) )
        #print(name , price, area, address, door_orientation, style, region)
        print("增加数据",Flag)
        Flag = Flag + 1
        f.flush()
        time.sleep(1)
        """
f.close()

