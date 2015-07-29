import os

dirname = 'e:/mp3temp/'
filename = 'mp3list.txt'
abspath = os.path.abspath(os.path.join(dirname, filename))
print(abspath)
print(abspath.split('\\'))
togetheragain = ''
for item in abspath.split('\\'):
    togetheragain = os.path.abspath(os.path.join(togetheragain, item))
print('togetheragain: ' + togetheragain)
with open(abspath) as f:
    print(f.readlines())