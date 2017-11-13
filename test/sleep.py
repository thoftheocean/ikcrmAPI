# coding:utf-8


import time, sched

# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间
schedule = sched.scheduler(time.time, time.sleep)

def perform_command(func, inc):
    # 安排inc秒后再次运行自己，即周期运行
    schedule.enter(inc, 0, perform_command, (func, inc))
    func()

def timming_exe(func, inc = 60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动,
    schedule.enter(inc, 0, perform_command, (func, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()

def spider():
    print 'hello'

if __name__ == '__main__':

        timming_exe(spider, 5) #间隔3天的时间

    # spider()单独运行爬虫