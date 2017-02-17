#!/user/bin/env python
# -*-  coding:utf-8 -*-

import time

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fibs(10)
    fobj = open('//Users//yh//Desktop//untitled22.py','w+')
    for i,num in enumerate(result):
        print u"第%d 个数是：%d" % (i,num)
        fobj.write("这是斐波拉契数列：%d\n"%num)
        time.sleep(1)
        
if __name__ == '__main__':
    main()