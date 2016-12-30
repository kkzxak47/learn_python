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
    # 获取锁，确保只有一个线程操作这个数
    muxlock.acquire()
    global balance
    balance = balance + n
    balance = balance - n
    # 释放锁，给其他被阻塞的线程继续操作
    muxlock.release()


def run_thread(n):
    # 最后的数字是0
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
