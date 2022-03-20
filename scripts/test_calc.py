import unittest

from parameterized import parameterized

from base.get_logger import GetLogger
from base.read_txt import read_txt
from page.page_calc import PageCalc
from tool.get_log import get_logging

# 使用单例封装的 getlogger 日志方法
log = GetLogger().get_logger()


def get_data(filename):
    return read_txt(filename)


class TestCalc(unittest.TestCase):
    calc = None

    @classmethod
    def setUpClass(cls):
        try:
            # 获取page 对象,使用的都是page对象中的方法
            cls.calc = PageCalc()
        except Exception as e:
            # 将出错的信息放到日志文件中
            log.error(e)

    @classmethod
    def tearDownClass(cls):
        cls.calc.driver.quit()

    # 测试加法计算方法
    @parameterized.expand(get_data("calc.txt"))
    def test_calc_add(self, a, b, expect):
        # 调用组合业务计算方法
        self.calc.page_calc(a, b)
        msg = self.calc.page_get_res()
        print("{}+{}={}".format(a, b, msg))
        # try:
        # 传递的是int, 返回的是 string ,类型不相等
        # 获取在传递的期望数值加引号
        # 使用的读取.txt文件的方法,返回的是字符串,不用转
        # msg = int(msg)
        try:
            self.assertEqual(msg, expect)
        # except AssertionError:
        #     print("计算错误")
        except Exception as e:
            log.error(e)
