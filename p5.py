# coding=utf-8
import pdb
def mysum(a,b):
    return a + b
x = (1,2)
print(mysum(*x))

def mysort(lst,asc = True):
    lst = sorted(lst,reverse = asc)
    print(lst)
str = "sdad as_ d"
alist = [1,4,6,8,9,3]
print(list(filter(lambda x:x % 2,alist)))

pdb.runcall(mysort,(alist,True))

print(list(str))

strList = list(str)
oList = len(strList)
fList = filter(lambda x:x != " ",strList)
print(oList - len(fList))

html = '''
<head>

    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
	<meta content="always" name="referrer">
    <meta name="theme-color" content="#2932e1">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="search" type="application/opensearchdescription+xml" href="/content-search.xml" title="百度搜索" />
    <link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg">


	<link rel="dns-prefetch" href="//s1.bdstatic.com"/>
	<link rel="dns-prefetch" href="//t1.baidu.com"/>
	<link rel="dns-prefetch" href="//t2.baidu.com"/>
	<link rel="dns-prefetch" href="//t3.baidu.com"/>
	<link rel="dns-prefetch" href="//t10.baidu.com"/>
	<link rel="dns-prefetch" href="//t11.baidu.com"/>
	<link rel="dns-prefetch" href="//t12.baidu.com"/>
	<link rel="dns-prefetch" href="//b1.bdstatic.com"/>

    <title>百度一下，你就知道</title>


'''

linkCount = html.count('rel')
print(linkCount)