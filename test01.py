"""如何点击数字"""
from selenium.webdriver.common.by import By
# from base.base import Base
# num=By.CSS_SELECTOR,"#simple{}".format(1)
# print(num)
# base = Base()
# base.base_click(num)
# int 类型不能迭代
# nums 作为参数传递
nums = "12"
for i in nums:
    num=By.CSS_SELECTOR,"#simple{}".format(i)
    print(num)
    # base.base_click(num)
