"""
    重点: 读取json文件

"""
import json

# 获取文件流,并调用 load 方法

with open("../data/login.json","r",encoding="utf-8") as f:
    print(json.load(f))