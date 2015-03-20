#!/usr/bin/env python
# -*- coding:utf8 -*-
import random
import string
import sys
from sys import argv
reload(sys)
sys.setdefaultencoding("utf8")

def random_number(*argv):
    pwlength=sys.argv[2]
    pwnumber=sys.argv[3]
    if int(argv[1])==0:
        pwcontent=string.digits+string.letters
    elif int(argv[1])==1:
        pwcontent=string.digits
    else :
        pwcontent=string.letters

    if  int(pwlength)<=10:
        for i in range(int(pwnumber)):
            number=string.join(random.sample(pwcontent,int(pwlength))).replace(' ','')
            print number
    else :
            print "目前只支持10位以下密码，请重试！！"
        #random_number()
if __name__=="__main__":
    random_number(*argv)