#-*- coding:utf-8 -*-
# 倒包
import unittest

# 导入浏览器包
from util import firefoxutil,urlutil
from main.control import maincontrol


# 声明类继承单元测试
class Main(unittest.TestCase):



    @classmethod
    def setUpClass(self):

        # 实例化浏览器对象
        self.firfox = firefoxutil.startFirfox2()
        # 实例化url类
        self.URL = urlutil.URL()
        # 实例化对象
        self.mainControl = maincontrol.MainControl(self.firfox)

        pass


    def setUp(self):

        # 打开浏览器
        self.firfox.startFirFox1(self.URL.JD_MAIN)

        pass


    def tearDown(self):

        # 关闭浏览器
        self.firfox.closeFirFox()

        pass



    # # 查找物品的单元测试
    # def test_main_search(self):
    #
    #     # 输入袜子
    #     self.mainControl.mainSeatch(u"袜子","key","button")
    #
    #     # 添加天涯
    #     self.mainControl.MainTtitle(self,u"袜子 - 商品搜索 - 京东")
    #
    #     # 添加第二个断言
    #     self.mainControl.MainAssertCount(self,"gl-item",30)
    #
    #     pass
    #
    # # 断言地址的用例与数据库一致不一致
    # def test_main_address(self):
    #
    #     # 浮动上去
    #     self.mainControl.ActionChain("dorpdown")
    #     # 进行断言
    #     self.mainControl.MainAssertCount(self,"item",35)
    #
    #     pass

    # 浮动到地址上面,切换地址
    def test_mian_address_switch(self):

        # 浮动上去
        self.mainControl.ActionChain("dorpdown")

        # 断言
        self.mainControl.MainAssertText("item",1,self)

        pass