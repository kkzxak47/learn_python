# coding: utf-8


def main():
    array = range(10)
    array.remove(5)
    full_array = range(10)
    x = 0
    for i in array:
        x ^= i
    for i in full_array:
        x ^= i
    print x

if __name__ == '__main__':
    main()
