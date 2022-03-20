"""
1.python 字典对象转成JSON字符串
        import json
        json_str = json.dumps(python 字典对象)
2. JSON字符串转成python字典对象
        import json
        dict_str = json.loads(json 字符串)
        # 定义json 字符串
         # 键名只能是双引号
        # data="{'name':'cyj', 'age':18}"
        data='{"name":"cyj", "age":18}'

"""
import json
# dict to json
data={
    "name":"cyj",
    "age":18,
}
print("转换之前",type(data))
json_str= json.dumps(data)
print("转换之后",type(json_str))
print(json_str)

# 定义json 字符串
# data="{'name':'cyj', 'age':18}"
data='{"name":"cyj", "age":18}'
# 键名只能是双引号
# 转换 json to dict
print("转换之前",type(data))

dict_str = json.loads(data)
print("转换之后",type(dict_str))
