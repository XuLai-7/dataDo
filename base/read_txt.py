# 读取文本文件中的数据
def read_txt(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        datas = f.readlines()
        # 读出的数据是一个列表
        arrs = []
        for data in datas:
            # strip() 可以去除字符串的前后特殊字符
            # split() 将字符串按符号分隔组成列表
            # 如果需要元组,就用 tuple() 强转成元组
            # print(data.strip().split(","))
            arrs.append(tuple(data.strip().split(",")))
        #     截取字符串,去掉表头
        return arrs[1:]


# if __name__=='__main__':
#     print(read_txt())
#     print("--------")
#     # strip() 可以去除字符串的前后特殊字符
#     # split() 将字符串按符号分隔组成列表
#     # 如果需要元组,就用 tuple() 强转成元组
#     arrs = []
#     for data in read_txt():
#         # print(data.strip().split(","))
#         arrs.append(tuple(data.strip().split(",")))
#
#     print(arrs)
if __name__ == '__main__':
    print(read_txt("calc.txt"))
