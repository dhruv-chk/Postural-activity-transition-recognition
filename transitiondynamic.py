# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:58:01 2018

@author: Dhruv
"""

#File is read
one=[]
f=open("....",'r')
for i in f:
    buffer=f.rstrip("\n").split(",")
    one.append(int(buffer[4]))
f.close()


#Identification of the range
flag=0
start=0
end=0
for i in range(0,len(one)):
    if one[i]<=70 and flag==0:
        flag=1
        start=i
    if one[i]>=120 and flag==0:
        flag=1
        start=i
    if one[i]<=70 and flag==1:
        flag=0
        end=i
    if one[i]>=120 and flag==1:
        flag=0
        end=i
    if start>0 and end>0:
        print(sum(one[start:end])/len(one[start:end]))
        print(one[start:end])
        start=0
        end=0

        