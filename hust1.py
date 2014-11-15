#! usr/bin/python
# coding:utf-8
# Filename:hust.py

import urllib2
import re
class hust:
    def __init__(self,words):
        self.words = words
    def results(self):
        num = 0
        if self.words=='exit':
            print 'Ending'
        else:
            url = 'http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH='+self.words+'&SORT=D&image.x=0&image.y=0'
            html = urllib2.urlopen(url).read()
            r = re.compile(r'<!--{nohitmsg}-->.+?<a href=".+?">(.+?)</a>\n.+?\n.+?\n.+?\n(.*?)\n.+?\n.+?\n(.*?)<br />\n.+?\n.+?\n(.*?)<br />',re.DOTALL)
            all = re.search(r'(?<=\<i>).+?(?=\</i>)',html,re.DOTALL)
            print all.group()
            for x in r.findall(html):
                num = num+1
                print 'name:','\t',x[0]
                print 'author:','\t',x[1]
                print 'publishing:','\t',x[2]
                print 'description:','\t',x[3]
                print '-------------------第',num,'本--------------------------'
            while(1):            
                answer = raw_input('do you want more?y/n:')
                if answer == 'y':                
                    p = re.search(r'(?<=\<a href=").+?(?=">.+?</a>\n<!-- end page widgit -->)',html)
                    url1 = 'http://ftp.lib.hust.edu.cn'+p.group()
                    html1 = urllib2.urlopen(url1).read()
                    r1 = re.compile(r'<!--{nohitmsg}-->.+?<a href=".+?">(.+?)</a>\n.+?\n.+?\n.+?\n(.*?)\n.+?\n.+?\n(.*?)<br />\n.+?\n.+?\n(.*?)<br />',re.DOTALL)
                    for i in r1.findall(html1):
                        num = num+1
                        print 'name:','\t',i[0]
                        print 'authoe:','\t',i[1]
                        print 'publishing:','\t',i[2]
                        print 'description:','\t',i[3]
                        print '-------------------第',num,'本--------------------------'
                elif answer == 'n':
                    break
                else:
                    print 'Wrong!Please input again'




if __name__ == "__main__":
    while(1):
        s = hust(raw_input('word:'))
        s.results()

