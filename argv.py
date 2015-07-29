import sys
print(type(sys.argv))
print(len(sys.argv))
# print(sys.argv[0])
print("details of argv:")
for index,item in enumerate(sys.argv):
    print(index, item)