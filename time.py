# coding=utf-8
import numpy as np
import os
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['KaiTi']
# plt.rcParams['font.serif'] = ['KaiTi']
plt.rcParams['font.family'] = 'Arial Unicode MS'
plt.rcParams['legend.fontsize'] = 8

# *************************以下为子功能函数*****************************


def percent_calcu(partial_time, total_time):  # 计算百分比函数  （额好像没用上
    return partial_time / total_time


def class_time_calcu(list_class):
    time = 0
    for item in list_class:
        start = item[1]
        finish = item[2]
        time += int(finish) - int(start) + (finish - int(finish) - start + int(start)) * 10 / 6  # 计算每一项的用时，单位为小时
    return time


def show(dict):
    # print (dict)
    labels = ['科研', '学习', '读书', '家务', '睡觉', '运动', '娱乐', '恋爱', '其他', '未知']
    # labels = []
    sizes = []
    colors = ['blue', 'lime', 'blueviolet', 'red', 'lightsalmon', 'deepskyblue','gray','hotpink', 'gold', 'gray']
    print("请输入今天的日期：")
    today = input()
    for key in dict:
        # labels.append(key)
        sizes.append(dict[key])

    plt.pie(sizes, labels=labels, colors=colors, \
            autopct='%1.1f%%', shadow=False, pctdistance=0.8, \
            startangle=90, textprops={'fontsize': 16, 'color': 'w'})

    plt.legend(loc='upper right')
    plt.title(today)
    plt.axis('equal')
    plt.show()


# *************************以下为主功能函数*****************************


def ask1():
    print("  记录【科研-看论文】时间请输入 0\n  记录【科研-研究/调研】时间请输入 1\n"
          "  记录【科研-干活】时间请输入 2\n  记录【学习-必修课】时间请输入 3\n  记录【学习-自学课】时间请输入 4\n"
          "  记录【看书-学科相关】时间请输入 5\n  记录【看书-课外书】时间请输入 6\n  记录【家务】时间请输入 7\n"
          "  记录【睡觉】时间请输入 8\n  记录【运动】时间请输入 9\n  记录【娱乐】时间请输入 10\n" 
          "  记录【恋爱】时间请输入 11\n 记录【其他类型】时间请输入 12\n")
    print("请输入要记录的类型编号：")
    type = input()
    print("请输入开始时间（示例各式--下午六点半为18.30）：")
    start = input()
    print("请输入结束时间（示例各式--下午六点半为18.30）：")
    finish = input()
    print("请输入关于本次时间记录要补充的内容，如果没有请输入 无 ：")
    tip = input()
    return [type, start, finish, tip]


def record_data(type, start, finish, tip):
    data = [type, " ", start, " ", finish, " ", tip, "\n"]
    with open("data.txt", "a+") as f:
        f.writelines(data)


def statistic():
    with open("data.txt", "r") as f:
        line = f.readline()
        line = line[:-1]
        data_list = []
        while line:
            data_list.append(line)
            line = f.readline()
            line = line[:-1]
    # print(data_list)
    data_split = []
    for item in data_list:
        data_split.append(item.split())
    # print(data_split)
    for l in data_split:
        for i in range(len(l) - 1):
            l[i] = float(l[i])
    # print(data_split)

    research = []
    study = []
    read = []
    housework = []
    sleep = []
    sport = []
    fun = []
    other = []

    data_dict = {'research': research, 'study': study, 'read': read, 'housework': housework, 'sleep': sleep,
                 'sport': sport, 'fun': fun, 'other': other}

    for item in data_split:
        if item[0] == 0 or item[0] == 1 or item[0] == 2:
            research.append(item)
        elif item[0] == 3 or item[0] == 4:
            study.append(item)
        elif item[0] == 5 or item[0] == 6:
            read.append(item)
        elif item[0] == 7:
            housework.append(item)
        elif item[0] == 8:
            sleep.append(item)
        elif item[0] == 9:
            sport.append(item)
        elif item[0] == 10:
            fun.append(item)
        else:
            other.append(item)

    time_dict = {}
    time_total = 0
    for key in data_dict:
        time_dict[key] = class_time_calcu(data_dict[key])
    for key in time_dict:
        time_total += time_dict[key]

    time_dict['unknown'] = 24 - time_total

    show(time_dict)
    # print ('time_dict', time_dict)


def rm_data():
    with open("data.txt", "r") as f:
        lines = f.readlines()
        cut = lines[:-1]
    with open("data.txt", "w") as f:
        f.writelines(cut)
        f.close()


# **********************************************以下为主程序部分**********************************************
switch = 1

while switch:
    print("Hi! 欢迎开启时光统计程序！\n  增加时间记录请输入 0\n  删除上一条时间记录请输入 1\n"
          "  查看统计结果请输入 2\n  开启新的一天请输入 3\n  退出程序请输入 4\n"
          "请选择你想使用的功能：\n")
    choice = input()

    if choice == "0":
        item = ask1()
        record_data(item[0], item[1], item[2], item[3])
    elif choice == "1":
        rm_data()
    elif choice == "2":
        statistic()
    elif choice == "3":
        print("请输入昨天的日期：")
        day = input()
        os.system("cp ~/mycodes/data.txt " + day + ".txt")
        os.system("rm ~/mycodes/data.txt")
    elif choice == "4":
        switch = 0
    else:
        print("请输入正确的功能编号")





# !【ok】代表已完成
# 日志：记得加入运动选项 【ok】
#       开启新一天时，记得保存前一天的饼状图，但是要研究一下怎么不让它显示出来
#       研究plot怎么显示中文 【ok】
