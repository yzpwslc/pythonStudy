#coding=utf-8
while True:
    try:
        num = raw_input('input:').split(' ')
        a, b = [int(x) for x in num]
        print a + b
    except EOFError:
        break