# 爬虫具有时限性如果不能运行请及时联系作者 
## 做数据分析适合想找个python太烦了，组员一起写了一个

### 功能，爬取链家各个城市的租房数据，由于页数限制，最多爬取3000左右条数据，爬取结果如下：  
![image](https://github.com/996jack555/ljia/assets/108218093/77ccd1ee-1500-435e-9625-ab99fdd1ee54)

### 环境: python3

### 运行步骤：  
`
pip install requirement.txt  
`
```python
python pachong.py
```
### 将会在当前文件夹生成对应的csv文件  

### 讲解：  
  其实这个爬虫非常简单，只涉及一级爬取  
  1=====先分析要爬取的网站数据<br>
![image](https://github.com/996jack555/ljia/assets/108218093/a9edf6b0-9549-4ba2-ac70-29cd5a295728)  
  2=====可知所有的数据都在:'class':'content__list'中<br>
![image](https://github.com/996jack555/ljia/assets/108218093/916f7143-b838-48a4-a6af-23464ca5c4a3)<br>   
  3=====而且每个租房数据都有'div',{'class':'content__list--item'}这个标识<br>  
  4=====所以在申请访问后，获取到网页的内容后，通过匹配语法：
```python
BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')  
```
  5=====就可以获取到一个字符串列表，其中每个字符串中都有一部分中含有我们需要的字符内容  
  6=====利用list的属性，在遍历过程中通过各种字符串匹配方法以及各种包就可以获取到需要的内容  
## 注意在某些城市中，会插入一些类似“精选”的字符串，会干扰我们原本的匹配顺序
### 解决方法就是通过列表切片等方法
  例如精选在第一个位置，就逆转列表从后向前读取字符串；在第二个位置就在第二个位置处切片再逆转

## 老师要求做热力图，没做出来，老师提供了一个根据位置提供经纬度的代码
### 生成经纬度  

环境 : python3

运行步骤：

注册百度开放api,新建应用获取ak

把ak复制到所需（获取经纬度.py）的代码处

等待获取所有csv文件中所有的位置信息即可输出到本地文档

author : zjl , yzh ，csy , ztc ，zkj , zwj

qq:2480657459

2023.7.8
