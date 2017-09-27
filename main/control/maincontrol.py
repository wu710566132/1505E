#-*- coding:utf-8 -*-
from util import firefoxutil

# 定义一个类继承 object
class MainControl(object):


    def __init__(self,frefox):

        # 实例化对象
        self.frefox = frefox

        pass


    #查找控件,输入内容
    def mainSeatch(self,message,inputs,buttom):

        # 查找输入框
        self.frefox.FindId(inputs).send_keys(message)
        # 点击一下
        self.frefox.ClickClass(buttom)

        pass

    # 进行断言
        # 断言title的方法

    def MainTtitle(self, self1, expects):
        title = self.frefox.getTitle()

        self1.assertEqual(title, expects)

        pass

    #断言列表的数量
    def MainAssertCount(self,self1,cls,number):

        # 通过class 查询
        gl_items = self.frefox.FindClasses(cls)

        self1.assertEqual(len(gl_items), number)

        pass

    # 浮动
    def ActionChain(self,cls):

        self.frefox.ActionMove(cls)

        pass

    # 断言点击的内容是不是一直
    def MainAssertText(self,cls,position,self1):


        # 获取列表的内容
        address = self.frefox.FindXpath("//*[@id='ttbar-mycity']/div[2]/div[2]/div/div/div[2]/a")

        # 通过class 查询
        gl_items = self.frefox.FindClasses(cls)

        # 点击第二个
        gl_items[position].click()

        # 获断取当前显示的位置进行断言
        ui_areamini_text = self.frefox.FindClass("ui-areamini-text")
        # 获取显示的内容
        msg = ui_areamini_text.text


        self1.assertEqual(msg, address.text)

        pass


