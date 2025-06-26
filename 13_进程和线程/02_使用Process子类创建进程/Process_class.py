from multiprocessing import Process
import os
import time


class Process_class(Process):
    # 重写__init__()方法
    def __init__(self, val, name=""):
        Process.__init__(self)
        self.val = val
        if name:
            self.name = name

    # 重写run()方法
    def run(self):
        print("子程序{}开始执行，父程序为{}".format(os.getpid(), os.getppid()))
        start = time.time()
        time.sleep(self.val)
        stop = time.time()
        print("子程序{}执行时间为{}秒".format(os.getpid(), stop - start))


def main():
    print("------主线程开始-----")

    p1 = Process_class(1, "p1")
    p2 = Process_class(2, "p2")

    # 对于没有target属性的Process类执行start()方法就会执行其中的run()方法
    p1.start()
    p2.start()

    print("p1的进程名：", p1.name)
    print("p1的进程号：", p1.pid)
    print("p1是否在执行：", p1.is_alive())
    print("p2的进程名：", p2.name)
    print("p2的进程号：", p2.pid)
    print("p2是否在执行：", p2.is_alive())

    print("-----等待子程序------")
    p1.join()
    p2.join()
    print("------主线程结束-----")


if __name__ == "__main__":
    main()
