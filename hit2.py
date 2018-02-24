import re

def delDouble(string):
    length0 = len(string)
    string = re.sub(r'[A]{2,}|[B]{2,}|[C]{2,}',"",string,0,re.I)
    lengthNew = len(string)
    if length0 - lengthNew > 0:
        string = delDouble(string)
    return string

def match1(string):
    delLength = 2
    if len(string) == 0:
        delLength = 1
    else:
        res = re.search(r'a.a|b.b|c.c',string,re.I)
        if res:
            delLength = 4
    return delLength

try:
    num = input('input numbers of string:')
    length = 0
    delta = 0
    while num > 0:
        try:
            string = raw_input('input str:')
            length0 = len(string)
            string = delDouble(string)
            length = len(string)
            deltaLen = length0 - length
            delta = deltaLen + match1(string)
            print delta
            num -= 1
        except EOFError:
            break
except EOFError:
    print 'error!'