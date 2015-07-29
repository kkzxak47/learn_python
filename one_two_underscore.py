# coding: utf-8
class MyClass():
    """ haha """
    def __init__(self):
        """ you see """
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"

mc = MyClass()

print mc._MyClass__superprivate, mc._semiprivate
print MyClass.__init__.__doc__
print mc.__dict__
print MyClass.__dict__