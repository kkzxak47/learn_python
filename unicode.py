# s = '你好'
# s2 = s.encode()
# # print(s.encode('utf8'))
# print('original s: ', s)
# print('encoded s2: ', s2)
# print('decoded s2: ', s2.decode())

f = open('baidu.html','rb')
html = f.read()
print(html)
f.close()