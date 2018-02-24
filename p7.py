#coding=utf-8
try:
    num = input('请输入整数')
    assert type(num) == int
except AssertionError:
    print 'error'
finally:
    pass
