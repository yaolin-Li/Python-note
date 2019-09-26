#coding=utf-8
class AgeError(Exception):
    def __init__(self,errorInfo):
        super().__init__(self)
        self.errorInfo = errorInfo
    def __str__(self):
        return str(self.errorInfo)+"年龄错误,应该在1-150"

if __name__ == "__main__":
    age = int(input("输入一个年龄:"))
    if age<1 or age>150:
        raise AgeError(age)
    else:
        print("正常的年龄：",age)
