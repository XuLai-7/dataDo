"""
    写入json
    json 写入
        param: 字典数据
        f: 文件流
        json.dump(param,f)
"""
import json

# data = {"name": "cyj", "age": 18}
data = {"name": "程裕江", "age": 18}
with open("../data/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
    # 不使用 ASCII 码写入