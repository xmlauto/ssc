#coding:utf-8

import re
import os
import time

qr = []
hr = []

fp = open("data.txt", "r")
for i in fp:
    ret = re.findall("\d{3}(\d\s\d\s)\d\s(\d\s\d)", i)
    for j in ret:
        qr.append(j[0])
        hr.append(j[1])
fp.close()

qr_list = []
for i in qr:
    if (qr.count(i) > 1) and (i not in qr_list):
        qr_list.append(i)
print "*" * 30 + "qian er" + "*" * 30
for i in range(len(qr_list)):
    qr_list[i] =  "".join(qr_list[i].split())
print qr_list
print len(qr_list)
print "*" * 30 + "qian er" + "*" * 30


hr_list = []
for i in hr:
    if (hr.count(i) > 1) and (i not in hr_list):
        hr_list.append(i)
print "*" * 30 + "hou er" + "*" * 30
for i in range(len(hr_list)):
    hr_list[i] =  "".join(hr_list[i].split())
print hr_list
print len(hr_list)
print "*" * 30 + "hou er" + "*" * 30
#raw_input()

if os.path.exists("qian.txt"):
	os.remove("qian.txt")
if os.path.exists("hou.txt"):
	os.remove("hou.txt")
#raw_input()
time.sleep(1)
print "+" * 60
fp = open("source.txt", "r")
for i in fp:
    x = i.split()
    for j in qr_list:
        if j in x:
            x.remove(j)
    y = " ".join(x)
    fp1 = open("qian.txt", "a")
    fp1.write(y)
    fp1.write("\n")
    fp1.close()
fp.close()
fp1 = open("qian.txt", "a")
fp1.write("\n\n\n")
fp1.write(" ".join(qr_list))
fp1.close()

print "+" * 60
fp = open("source.txt", "r")
for i in fp:
    x = i.split()
    for j in hr_list:
        if j in x:
            x.remove(j)
    y = " ".join(x)
    fp1 = open("hou.txt", "a")
    fp1.write(y)
    fp1.write("\n")
    fp1.close()
fp.close()
fp1 = open("hou.txt", "a")
fp1.write("\n\n\n")
fp1.write(" ".join(hr_list))
fp1.close()


