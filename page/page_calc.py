from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageCalc(Base):
    # 点击数字方法
    def page_click_num(self, nums):
        # 传递哪个数字,就点击哪个数字
        nums = str(nums)
        for i in nums:
            loc = By.CSS_SELECTOR, "#simple{}".format(i)
            # 执行单个点击按钮
            self.base_click(loc)

    # 通过 page.变量名 获取里面所有变量的值
    # 点击加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_click_equal(self):
        self.base_click(page.calc_equal)

    # 获取结果
    def page_get_res(self):
        return self.base_get_value(page.calc_result)

    # 清屏
    def page_clear(self):
        self.base_click(page.calc_clear)

    # 组合业务方法
    def page_calc(self,a,b):
        # 输入之前先进行清屏
        self.page_clear()
        self.page_click_num(a)
        self.page_click_add()
        self.page_click_num(b)
        self.page_click_equal()
        # 获取文本不要在这里写
        # 在业务层写,需要断言
        # self.page_get_res()
        # self.page_clear()
