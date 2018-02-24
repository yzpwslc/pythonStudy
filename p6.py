#coding=utf-8
# class DemoPro:
#     className = "Demo"
#
#     def __init__(self,x = 0):
#         self.x = x
#
#     def class_info(self):
#         print '类变量值: ',DemoPro.className
#
#     def changeCn(self,name):
#         DemoPro.className = name
#
# dpa = DemoPro()
# dpb = DemoPro()
#
# print('init...')
#
# dpa.class_info()
# dpb.class_info()
#
# dpa.changeCn('dpa')
#
# dpb.class_info()
import unittest
class Geinus:
    def __init__(self,en = 0):
        self.en = en
        self.weight = 1
        self.height = 9
        self.color = '#fff'

    def run(self):
        print 'running...'
        self.en = self.en - 1
        print 'en:' + str(self.en)

    def jump(self):
        print 'jumping...'
        self.en = self.en - 1
        print  'en:' + str(self.en)

    def eatting(self):
        print 'eatting...'
        self.en = self.en + 1
        return 'en:' + str(self.en)


# gen = Geinus(10)
# gen.run()
# gen.jump()
# gen.eatting()

class mytest(unittest.TestCase):
    def setUp(self):
        self.tclass = Geinus(10)
    def tearDown(self):
        pass
    def testeatting(self):
        self.assertEqual(self.tclass.eatting(),'en:11')

if __name__ == 'main':
    unittest.main()