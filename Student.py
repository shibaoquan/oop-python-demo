

"""
子类重写父类方法demo
"""

class Company(object):

    companyName = None

    def __init__(self, companyName):
        self.companyName = companyName


class Person(Company):

    def __init__(self, companyName, name):
        # Company.__init__(self, companyName)    # python2 子类调用父类写法
        # super(Person, self).__init__("健易保")  # python2 子类调用父类写法
        super().__init__("健易保")                # python3 子类调用父类写法
        self.name = "史保权"

    def setName(self, name):
        self.name = name

if __name__ == '__main__':
    p = Person("健易保", "史保权")
    print(p.name)
    print(p.companyName)
    # p.name = "shibaoquan"
    p.setName("shibaoquan")
    print(p.name)

    p.companyName = "jianyibao"
    print(p.companyName)
