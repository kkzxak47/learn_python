#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.jianshu.com/p/af3aaf5f9291
"""
import threading

# 假定这是你的银行存款:
balance = 0
muxlock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    # 循环次数一旦多起来，最后的数字就变成非0
    for _ in range(100000):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t3 = threading.Thread(target=run_thread, args=(9,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print balance
