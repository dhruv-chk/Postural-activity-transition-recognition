# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:14:46 2018

@author: Dhruv
"""
count2=0
#tansition is checked using sliding window recursively
def transition(two, size, n):    
    global flag, flag2, count,count2,sit,win,sit2
    for i in range(n,len(two)):
       if count<size:
           if two[i]<30:
                    if flag==0:
                        flag=1
                        #print("Flag set 1")
                        #print(two[i])
                    else:
                        flag2=1
                        #print("Flag2 set 1")
                        #print(two[i])
                            
           if two[i]>=50 and two[i]<=70:
                 if flag==0:
                        flag=2
                        #print("Flag set 2")
                        #print(two[i])
                 else:
                        flag2=2         
                        #print("Flag2 set 2")
                        #print(two[i])
                           
           if two[i]>=90 and two[i]<=110:
                    if flag==0:
                        flag=3
                        #print("Flag set 3")
                        #print(two[i])
                    else:
                        flag2=3          
                        #print("Flag2 set 3")
                        #print(two[i])
                             
       else:
           count=0
          # print("Window change")
           
           if flag!=0:
                if flag==2 and flag2==1 and sit2==0:
                    print("Sitting to Standing")
                    flag=0 
                    flag2=0
                if flag==2 and flag2==1 and sit2==1:
                    print("Fall to Standing")
                    flag=0 
                    flag2=0 
                    sit2=0
                if flag==3 and flag2==1:
                    print("Fall to Standing")
                    flag=0
                    flag2=0
                    
                if flag==1 and flag2==2:
                    print("Standing to Sitting")
                    flag=0
                    flag2=0
                    sit=1
                    count2+=1
                if flag==3 and flag2==2:
                    print("Fall to Sitting")
                    flag=0
                    flag2=0
                    sit2=1
                if flag==1 and flag2==3:
                    print("Standing to Fall")
                    flag=0
                    flag2=0
                    
                if flag==2 and flag2==3 and sit==0:
                    print("Sitting to Fall")
                    flag=0
                    flag2=0
                   
                if flag==2 and flag2==3 and sit==1:
                    print("Standing to Fall")
                    flag=0
                    flag2=0
                    sit=0
           
                   
       count=count+1                    
                    

#Take window size as input
size=int(input("Enter the size of the window"))
flag=0
flag2=0
count=0
sit=0
sit2=0
win=0
#File is read
one=[]
f=open("D:\Activity transition\\standfall4.csv",'r')
for i in f:
    buffer=i.rstrip("\n").split(",")
    one.append(int(buffer[0]))
f.close()
two=[]
for i in range(0,len(one)):
    if one[i]<120:
      two.append(one[i])  
transition(two, size, 0) #transition checking function is called
print(count2)


