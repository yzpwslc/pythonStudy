#coding=utf-8
#模块

import math

def mSqrt(num):
    print str(num) + "的平方根是:" + str(math.sqrt(num))

def mAbs(num):
    print  str(num) + "de绝对值是:" + str(abs(num))

def isPrime(num):
    '''
    >>> isPrime(2)
    2是素数
    >>> isPrime(3)
    3是素数
    >>> isPrime(4)
    4不是素数
    '''
    res = 1
    if num > 1:
        if num > 2:
            for i in range(2,int(math.sqrt(num) + 1)):
                if num % i == 0:
                    res = 0
                    break
    else:
        print "error!"

    return res
    # str0 = "是素数" if res else "不是素数"
    # print  str(num) + str0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    num = input("请输入一个整数")
    mSqrt(num)
    mAbs(num)
    isPrime(num)
