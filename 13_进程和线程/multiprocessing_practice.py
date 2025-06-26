# 创建两个子进程，并记录进程运行时间：
from multiprocessing import Process
import time
import os


def child1(val):
    print("子程序{}开始执行，父程序为：{}".format(os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(val)
    t_end = time.time()
    print("子程序{}执行时间为{}秒".format(os.getpid(), t_end - t_start))


def child2(val):
    print("子程序{}开始执行，父程序为：{}".format(os.getpid(), os.getppid()))
    t_start = time.time()
    time.sleep(val)
    t_end = time.time()
    print("子程序{}执行时间为{}秒".format(os.getpid(), t_end - t_start))


if __name__ == "__main__":
    p1 = Process(target=child1, args=(1,))
    p2 = Process(target=child2, args=(10,))
    p1.start()
    p2.start()

    print("p1的进程名：", p1.name)
    print("p1的进程号：", p1.pid)
    print("p1是否在执行：", p1.is_alive())
    print("p2的进程名：", p2.name)
    print("p2的进程号：", p2.pid)
    print("p2是否在执行：", p2.is_alive())

    # 等待两个子程序进程
    p1.join()
    p2.join()
    print("主程序结束")
