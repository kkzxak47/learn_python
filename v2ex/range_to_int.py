#/usr/bin/env python3
# coding: utf-8
"""https://v2ex.com/t/298833
"""


import bisect

def main():
    arr = [1, 2, 3, 4]
    d = {1:1, 2:2, 3:5}
    idx = bisect.bisect_left(arr, 1.5)
    print(d[idx])
    idx = bisect.bisect_left(arr, 2.5)
    print(d[idx])
    idx = bisect.bisect_left(arr, 3.5)
    print(d[idx])


if __name__ == '__main__':
    main()
