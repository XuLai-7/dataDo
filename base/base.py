from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.get_logger import GetLogger
from tool.get_log import get_logging

# log = get_logging()
# 使用单例封装的 getlogger 日志方法
log = GetLogger().get_logger()
class Base:
    # 初始化方法,Base中没有driver,得初始化
    def __init__(self):
        self.driver = webdriver.Chrome()
        log.info("inint driver{}".format(self.driver))
        self.driver.maximize_window()
        log.info("max window{}".format(self.driver))
        self.driver.get('http://cal.apple886.com/')
        log.info("open url")

    # 标志程序运行的步骤,每一步都需要打日志

    # 查找元素
    def base_find(self, loc, timeout=30, poll=0.5):
        log.info("find element{}".format(loc))
        # 设置显示等待
        # *loc 解包 元组或者 列表
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素封装
    def base_click(self, loc):
        log.info("click element{}".format(loc))
        self.base_find(loc).click()

    # 获取文本框值
    def base_get_value(self, loc):
        # input 标签通过 value 属性 获取值
        log.info("get inputElement{} value".format(loc))
        return self.base_find(loc).get_attribute("value")
