"""
Title:多线程爬虫
Author:kingsley
Version:0.1
Question:多线程摸鱼，爬虫程序更加高效
Preparation:

"""
import time
import threading
from concurrent.futures import ThreadPoolExecutor


# 创建一个线程子类
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：'+ self.name)
        moyu_time(self.name, self.counter, 10)
        print('退出线程：'+ self.name)


def moyu_time(name, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s 开始摸鱼 %s' % (name, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        counter -= 1


if __name__ == '__main__':
    # moyu_time('kingsley', 1, 20)
    # 多个线程进行创建，销毁浪费资源，需要使用线程池，重复利用
    # thread1 = MyThread(1, '小明', 1)
    # thread2 = MyThread(2, '小红', 2)
    #
    # thread1.start()
    # thread2.start()
    #
    # thread1.join()
    # thread2.join()
    # print('退出主线程')

    # 可以使用ThreadPoolExecutor实现线程池，把许多线程塞入
    pool = ThreadPoolExecutor(20)
    for i in range(1, 5):
        pool.submit(moyu_time('kingsley'+ str(i), 1, 3))
