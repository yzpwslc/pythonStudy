# a = input("input 2 num")
# b = [int(i) for i in a]
# c,d = zip(b)
# if b[0] > 60:
#     print 'PASSED'
# else:
#     if b[1] < 60:
#         print 'bu kao'
#     else:
#         print 'PASSED0'

a = input("input 10 numbers")
b = []
c = []
[b.append(int(i)) for i in a if i > 0]
[c.append(int(i)) for i in a if i < 0]
print(c)
