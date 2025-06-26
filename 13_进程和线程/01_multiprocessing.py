from multiprocessing import Process

# Process(group=None, target=None, name=None, args=(), kwargs={})
# group：进程组，基本不用
# target：执行的目标任务名
# name：进程名
# args：以元组方式给执行任务传参
# kwargs：以字典方式给执行任务传参


# 执行子程序
def test(val):
    print(f"我是子程序！{val}")


def main():
    print("我是主程序！")
    p = Process(target=test, args=("1",))
    p.start()
    # 实例P处理start方法外还有：
    # p.join(timeout=2) 主进程等待子进程执行结束后，主进程才继续执行,timeout：超时时间
    # p.name 进程名
    # p.pid 进程号
    # p.is_alive() 进程是否还在执行
    # p.terminate() 终止进程
    print(p.name)
    print("主程序结束")


if __name__ == "__main__":
    main()
