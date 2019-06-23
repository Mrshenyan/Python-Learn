import socket
import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))##获取网页信息
# print(type(response))##获取输出相应类型
# print(response.status)##获取返回结果状态码
# print(response.getheaders())##
# print(response.getheader('Server'))##获取相应头部的Server值，说明服务器的搭建方式

##post测试
# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

#timeout参数
# timeoutRes = urllib.request.urlopen('http://httpbin..org/get',timeout=0.1)
# print(timeoutRes.read())#服务器响应时间超过设定，所以报错
# timeoutRes = urllib.request.urlopen('http://httpbin.org/get', timeout=0.11)
# print(timeoutRes.read())
# try:
#     timeoutRes = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time out')

##Request
# Reqrequest = urllib.request.Request('http://python.org')
# Reqrespone = urllib.request.urlopen(Reqrequest)##使用urlopen发送的是request对象
# print(Reqrespone.read().decode('utf-8'))
from urllib import parse, request

#使用 request.Request 可以构建request对象，参数一：请求的地址，参数二：数据本体；参数三：请求头部
#参数四：请求方式
url = 'http://httpbin.org/post'
headers = {
    'User_Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url, data = data, headers=headers, method='POST')
res = request.urlopen(req)
print(res.read().decode('utf-8'))

