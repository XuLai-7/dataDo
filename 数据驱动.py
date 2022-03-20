"""
    数据驱动:
        是以数据来驱动整个测试用例的执行, 也就是测试数据决定测试结果
        一种模式
        在 page 不变的情况下,主要对 测试数据的构建和维护
        依赖 参数化 的技术
    数据存放文件类型: json,excel,xml ,txt,csv,数据库(不常用) 等格式文件
    数据驱动 = 数据存储文件+读取数据技术工具+参数化技术

    JSON:
        是 JavaScript对象表示法, 基于文本的轻量级数据交换格式
        键值对形式 : ,
        语法规则:
            大括号保存对象
            中括号保存数组
            对象数组可以相互嵌套
            数据采用键值对表示
            用逗号分隔
        数字,字符串,布尔值,数组,对象,null
        例如:
        {
            "name":"tom",
            "address":{
                "country":"China",
                "city":"suzhou"
            },
            "numbers":[2,3,4],
            "links":[
                {
                    "name":"yjcms",
                    "url":"http://yjcms.top:7001"
                },
                {
                    "name":"baidu",
                    "url":"http://www.baidu.com"
                }
            ]

        }

    1.python 字典对象转成JSON字符串
        import json
        json_str = json.dumps(python 字典对象)
    2.JSON字符串转成 python字段对象
        import json
        dict_str = json.loads(json 字符串)
        # 定义json 字符串
         # 键名只能是双引号
        # data="{'name':'cyj', 'age':18}"
        data='{"name":"cyj", "age":18}'

    json 读取
        load()
        # 获取文件流,并调用 load 方法
        with open("../data/login.json","r",encoding="utf-8") as f:
            print(json.load(f))

    json 写入
        param: 数据
        f: 文件流
        json.dump(param,f)
        data = {"name": "程裕江", "age": 18}
        with open("../data/data.json", "w", encoding="utf-8") as f:
             json.dump(data, f, ensure_ascii=False)
             # 不使用 ASCII 码写入

    应用
        json 数据文件编写
            每组数据单独键名: 用例编号
            {
             "tpshop_login_001": {
                "username": "151212712885",
                "password": "cyj282535",
                "verify_code": "8888",
                "expect": "账号格式不匹配!"
                 },
                 ...
            }
    # { "键名1": 字典数据中的数据键值对,"键名2":字典数据中的数据键值对 }
        读取工具类编写
            打开文件获取文件流, 并调用 json.load()
            with open 文件动态参数
                函数内部 固定路径+传入的json文件名称
                return json.load(f)

        测试执行
        if __name__ == '__main__':
             print(read_json("login.json"))

    转换格式, 提供参数驱动
    预期: [(),()] 或 [[],[]]
    实际: {"":{}, "":{}}
    思路方法:
        def get_data():
        # 模拟数据驱动
        arrs = []

        # 通过键名获取值
        # 列表嵌套元组
        # 遍历获取 json 串 value值
        values() 方法一次获取所有的字典的值,值还是json
        append((data.get("键名"), ...))
        for data in read_json("login.json").values():
            # print(data)
            arrs.append((data.get("username"),
                         data.get("password"),
                         data.get("verify_code"),
                         data.get("expect"),
                         ))
        return arrs

        列表嵌套列表
         for data in read_json("login.json").values():
             # print(data)
             arrs.append([data.get("username"),
                          data.get("password"),
                          data.get("verify_code"),
                          data.get("expect"),
                          ])
       return arrs


       实战需求:
        测试网页计算器的加法
            1+1=2
            10+0=10
            11123123+1=11123124
        使用PO+数据驱动

        # 获取文本框值
        def base_get_value(self, loc):
            # input 标签通过 value 属性 获取值
            return self.base_find(loc).get_attribute("value")

        page 层点击数字
             # 点击数字方法
            def page_click_num(self, nums):
                # 传递哪个数字,就点击哪个数字
                # int 类型不能迭代
                # nums 作为参数传递
                nums = str(nums)
                for i in nums:
                    loc = By.CSS_SELECTOR, "#simple{}".format(i)
                    # 执行单个点击按钮
                    self.base_click(loc)
        script 层
            # 获取page 对象,使用的都是page对象中的方法
             cls.calc = PageCalc()
             调用业务方法
             断言

    # 读取文本文件中的数据
        1.读取
        2.转换格式
    def read_txt():
        with open("../data/calc.txt","r",encoding="utf-8") as f:
                readlines() 读取所有行
                readline() 读取单行
                read() 读取所有数据
            datas = f.readlines()
            # 读出的数据是一个列表
            arrs = []
            遍历单行数据,去除前后特殊字符,分隔字符串成列表,用元组强转,
            空列表追加,返回列表
            for data in datas:
                # strip() 可以去除字符串的前后特殊字符
                # split() 将字符串按符号分隔组成列表
                # 如果需要元组,就用 tuple() 强转成元组
                # print(data.strip().split(","))
                arrs.append(tuple(data.strip().split(",")))
               #截取字符串,去掉表头
              return arrs[1:]





"""