__author__ = 'Qing'
#Create by 2015-03-19
# -*- coding: utf8 -*-
import urllib2
import threading
import sys
import os
from bs4 import BeautifulSoup
import time


reload(sys)
sys.setdefaultencoding('utf8')

class MSTX(threading.Thread):
    def __init__(self,number,process_number):
        threading.Thread.__init__(self)
        self.url='http://home.meishichina.com/recipe-'
        self.headers={ 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
        self.number=number
        self.process_number=process_number

    def menu(self,n):
        url=self.url+str(n)+'.html'
        response=urllib2.Request(url,headers=self.headers)
        res=urllib2.urlopen(response)
        soup=BeautifulSoup(res)
        title=soup.find(class_='recipe_De_title')
        material=soup.find_all(class_='category_s1')
        amount=soup.find_all(class_='category_s2')
        step=soup.find_all(class_='recipeStep_word')
        dir1='E:\\Qing\\program\\menu\\'
        dir=dir1+str(title.text).decode('utf-8')
        if os.path.isdir(dir1):
            f=open(dir,'w')
            for material in material:
                material_NU=material.text
                f.write(material_NU)
                f.write('\t')
            f.write('\n')
            for amount in amount:
                amount_NU=amount.text
                f.write(amount_NU)
                f.write('\t')
            f.write('\n')
            for step in step:
                step_NU=step.text
                f.write(step_NU)
                f.write('\n')
            f.close()
        else :
            os.makedirs(dir1)
            f=open(dir,'w')
            for material in material:
                material_NU=material.text
                f.write(material_NU)
                f.write('\t')
            f.write('\n')
            for amount in amount:
                amount_NU=amount.text
                f.write(amount_NU)
                f.write('\t')
            f.write('\n')
            for step in step:
                step_NU=step.text
                f.write(step_NU)
                f.write('\n')
            f.close()
        return url

    def process(self,n):
        url=self.url+str(n)+'.html'
        r=urllib2.Request(url,headers=self.headers)
        res=urllib2.urlopen(r).read()
        soup=BeautifulSoup(res)
        title_name=soup.find('title')
        r=title_name.text
        print r
        if r==u'您访问的页面不存在-美食天下':
            print "%s is NOT FOUND! %s " %(url,time.ctime())
        else :
            print "The process is %d , %s  %s" %(self.process_number,url,time.ctime())
            self.menu(n)

    def run(self):
            for i in range(self.number,self.number+10):
                self.process(i)

def test():

    t1=MSTX(1,1)
    t2=MSTX(100,2)
    t1.start()
    t2.start()
    return


if __name__=="__main__":
   test()