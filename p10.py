#coding=utf-8
# class FileMgr:
#     def __init__(self,filename):
#         self.filename = filename
#         self.f = None
#
#     def __enter__(self):
#         self.f = open(self.filename)
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.f:
#             self.f.close()
#
#
# if __name__ == '__main__':
#     with FileMgr('p9.py') as f:
#         for line in f.readlines():
#             print(line)
# def delay_fun(x,y):
#     def cal():
#         return x + y
#     return cal
#
# if __name__ == '__main__':
#     num = delay_fun(2,3)
#     print(num())

class Calculate:
    def __init__(self,method,a,b):
        self.a = a
        self.b = b
        self.res = 0
        self.method = method
        self.fun = {}
        self.fun['mul'] = self.mul
        self.fun['add'] = self.add
        self.fun['sub'] = self.sub

    def cal(self):
        return self.fun[self.method]()
    def mul(self):
        return self.a * self.b

    def add(self):
        return  self.a + self.b

    def sub(self):
        return  self.a - self.b


if __name__ == '__main__':
    cal = Calculate('add',3,5)
    print cal.cal()