import urllib.parse
import urllib.request

#response = urllib.request.urlopen("https://www.python.org")
#print(response.read().decode('utf-8'))                      #decode用于解码， read是直接获取网页的信息（h5）

#print(type(response))                                       #<class 'http.client.HTTPResponse'>

#尝试请求京东网页
#jingdong = urllib.request.urlopen('https://promotion.jdcloud.com/productTrialforPay?uuid=ada8afd783dd4772b8b9e356b8e018e0')
#print(jingdong.post())                                      #AttributeError: 'HTTPResponse' object has no attribute 'post'
#print(jingdong.status)                                       #200 表示请求成功

'''
#模拟表格提交

data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding='utf-8')     #使用二进制类型进行传输，编码方式为utf-8
resonse = urllib.request.urlopen('http://httpbin.org/post', data=data)      #发送post请求，datac参数必须是字节流的
print(resonse.read())
'''
'''
#urllib.request.urlopen的参数介绍
#1.url      必传参数
#2.data     选传参数，数据必须是字节流类型的，如果数据是字典类型可以用urllib.parse.urlencode进行编码
#3.headers  选传参数，是一个字典  多用于修改请求头，伪装网页 
#4.origin_req_host  选传参数， 请求方的host名称或者ip地址
#5.unverifiable     选传参数， 默认为False，多用于修改抓取图像的权限
#6.method           选传参数， 用来指示请求的方法， 如GET, POST, PUT等
'''


#查看cookies
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)