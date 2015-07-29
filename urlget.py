import urllib.request
url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url)
html = response.read()
# string = str(html)
# print(type(string))
# print(type('nihao'))
f = open('baidu.html','wb')
f.write(html)
# f.write(string)
f.close()