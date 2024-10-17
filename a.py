import requests
import os
import sys

sys.path.append(".")

import threading
from queue import Queue
from time import sleep
import test

# from curl_cffi import requests

# 图片URL

A_queue = Queue()
shared_value = 0
lock = threading.Lock()
stop_threads = False


def download():

    while True:
        P, A = A_queue.get()  # 从队列中获取编号任务
        C = 0
        while True:
            C += 1
            path = ".\\PHOTO\\{:0>3d}\\{:0>3d}.webp".format(P, C)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # print(A, P, C)
            if os.path.exists(path):
                continue

            if P == -1:
                return
            url = "https://cdn-msp3.18comic.vip/media/photos/{}/{:0>5d}.webp".format(
                A, C
            )

            try:
                # 发送HTTP请求
                response = requests.get(url)
                # 如果图片太小，表示下载完成或资源不存在，获取下一个任务
                if len(response.content) < 10 or response.status_code.__eq__(403):
                    global shared_value
                    with lock:  # 确保对共享变量的安全访问
                        shared_value += 1
                        print(shared_value, P, A, C)
                    break

                with open(path, "wb") as file:
                    file.write(response.content)
                test.scramble_image(path, str(A))

                # print(f"下载完成：{path}")

            except requests.RequestException as e:
                print(f"下载错误：{e}")
                sleep(1)  # 出现错误时休息1秒重试
                continue

        A_queue.task_done()  # 标记任务完成


def producer():
    TTT = [
        335258,
        335259,
        335260,
        335261,
        335262,
        335263,
        335264,
        337032,
        339114,
        341043,
        343224,
        345411,
        390089,
        349573,
        351447,
        353954,
        355984,
        358351,
        360322,
        390053,
        364614,
        366606,
        368141,
        369665,
        372495,
        374821,
        377808,
        379816,
        381810,
        383833,
        385792,
        387690,
        389588,
        391960,
        394172,
        396580,
        398577,
        400342,
        401505,
        402957,
        404423,
        405548,
        407791,
        411304,
        414142,
        416478,
        418344,
        420489,
        423219,
        425621,
        427716,
        429371,
        431220,
        433086,
        435246,
        438080,
        439897,
        441934,
        443937,
        446097,
        447985,
        449903,
        452881,
        454901,
        457004,
        458898,
        461230,
        463282,
        465391,
        467412,
        469281,
        471491,
        473811,
        476034,
        478314,
        480867,
        483047,
        485363,
        487078,
        494724,
        498383,
        498377,
        500097,
        501654,
        503528,
        505767,
        507817,
        509502,
        511326,
        513168,
        515636,
        517964,
        520069,
        521854,
        524427,
        527857,
        530511,
        533491,
        535346,
        539470,
        541391,
        543319,
        545502,
        548184,
        550430,
        552304,
    ]
    # A_queue.put({1, TTT[0]})
    for i, A in enumerate(TTT, 1):
        A_queue.put((i, A))  # 向队列中加入新任务


if __name__ == "__main__":
    # 启动多个消费者线程，负责从队列中取出编号并下载图片
    num_workers = 10  # 定义工作线程数量
    workers = []
    for _ in range(num_workers):
        worker_thread = threading.Thread(target=download)
        worker_thread.start()
        workers.append(worker_thread)
    producer()
    for i in range(num_workers):
        A_queue.put(-1, -1)
    # stop_threads = True
    print("T  t", stop_threads)
