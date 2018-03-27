# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:17:26 2018

@author: Dhruv
"""
#tansition is checked using sliding window recursively
def transition(two, size, n):    
    global flag, flag2
    for i in range(n,len(two)-size):
            for j in range(i,(i+size)-1):
                if two[j]<30:
                    if flag==0:
                        flag=1
                    else:
                        if flag!=1:
                            flag2=1                    
                            transition(two, size, j)
                            
                if two[j]>=50 and two[j]<=70:
                    if flag==0:
                        flag=2
                    else:
                        if flag!=2:
                            flag2=2                    
                            transition(two, size, j)
                if two[j]>=90 and two[j]<=100:
                    if flag==0:
                        flag=3
                    else:
                        if flag!=3:
                            flag2=3                    
                            transition(two, size, j)
                
            if flag!=0:
                if flag==2 and flag2==1:
                    print("Standing to sitting")
                if flag==3 and flag2==1:
                    print("Standing to fall")
                if flag==1 and flag2==2:
                    print("Sitting to Standing")
                if flag==3 and flag2==2:
                    print("Sitting to Fall")
                if flag==1 and flag2==3:
                    print("Fall to Standing")
                if flag==2 and flag2==3:
                    print("Fall to Sitting")
                
                
            
            



#Take window size as input
size=int(input("Enter the size of the window"))
flag=0
flag2=0
#File is read
one=[]
f=open("D:\Activity transition\\ashutosh-sit-stand.csv",'r')
for i in f:
    buffer=i.rstrip("\n").split(",")
    one.append(int(buffer[0]))
f.close()
two=[]
for i in range(0,len(one)):
    if one[i]<120:
      two.append(one[i])  
transition(two, size, 0) #transition checking function is called


    
                
            
     