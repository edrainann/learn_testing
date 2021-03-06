# -*- coding: utf-8 -*-

#将要被测试的类
class Widget:
    #_init_()方法在类的一个对象被创建时，马上运行。
    # 这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self,size=(40,40)):
        self._size=size #变量传递

    #类具有封装性。如果要将一个方法声明为 private ，只要在方法名前面加上“ __ ”即可
    # 赋值函数（getXXX），取值函数（setXXX）
    def getSize(self):
        return self._size

    #self表示类本身
    def resize(self,width,height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
        self._size = (width,height)

    def dispose(self):
        pass
