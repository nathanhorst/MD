"""
Created on Mon Jul 11 15:04:51 2016

@author: waltmann
"""


import numpy as np

def normal_distribution(arr):
    std=np.std(arr)
    mean=np.mean(arr)
    dist=np.array([[0.0,0.0]])
    d=1/np.sqrt(2*std*std*np.pi)
    for i in range(0,60): 
        x=(mean-3*std)+i*(std/10.0)
        a=np.exp(-1*((x-mean)**2)/(2*std**2))*d
        dist=np.append(dist,[[x,a]],axis=0)
    return dist    
    
#print(len(inter_angle('2np.xml',0)))  
    
def histogram(arr,boxes):    
    arr=np.sort(arr,axis=0,kind='mergesort')
    #print arr
    hist=np.array([[0.0,0.0]])
    step= (arr[len(arr)-1]-arr[0])/boxes
    for i in range(0,boxes):
        min=arr[0]+i*step
        max=arr[0]+(i+1)*step
        hit=0
        for x in range(0,len(arr)):
            if (arr[x]>=min and arr[x]<max):
                hit+=1
        hist=np.append(hist,[[(min+max)/2,hit]],axis=0)
    #print hist
    return hist
    
def vector_length(x,y,z):
    c=np.sqrt(x**2+y**2+z**2)
    return c
    
def length(vector):
    return vector_length(vector[0],vector[1],vector[2])    

def part_distance(part1,part2,lx,ly,lz):
    
    x=abs(float(part1[0])-float(part2[0]))
    if(x>(lx/2)-1):
        x=lx-x
    y=abs(float(part1[1])-float(part2[1]))
    if(y>(ly/2)-1):
        y=ly-y
    z=abs(float(part1[2])-float(part2[2]))
    if(z>(lz/2)-1):
        z=lz-z
    return vector_length(x,y,z)


def part_distance(part1,part2,inputfile):
    fin1= open(inputfile,'r')
    f1data=fin1.read()
    data1=f1data.splitlines()
    #print data1[3]
    s=data1[3].split()
    #print s
    lx=0
    ly=0
    lz=0
    for i in range(len(s)):
        if s[i][:2]=='lx':
            count=0
            while(s[i][count]!='"'):
                count+=1
            b=1
            while(s[i][count+b]!='"'):
                b+=1
            lx=float(s[i][count+1:b+count-len(s[i])])
        elif s[i][:2]=='ly':
            count=0
            while(s[i][count]!='"'):
                count+=1
            b=1
            while(s[i][count+b]!='"'):
                b+=1
            ly=float(s[i][count+1:b+count-len(s[i])])
        elif s[i][:2]=='lz':
            count=0
            while(s[i][count]!='"'):
                count+=1
            b=1
            while(s[i][count+b]!='"'):
                b+=1
            lz=float(s[i][count+1:b+count-len(s[i])])
    #print lx
    #print ly
    #print lz
    #print part1
    #print part2[0]
    x=abs(float(part1[0])-float(part2[0]))
    if(x>(lx/2)-1):
        x=lx-x
    y=abs(float(part1[1])-float(part2[1]))
    #print y
    if(y>(ly/2)-1):
        y=ly-y
    z=abs(float(part1[2])-float(part2[2]))
    if(z>(lz/2)-1):
        z=lz-z
    #print x
    #print y 
    #print z
    return vector_length(x,y,z)
def write_array(arr, outputfile):
    fid=open(outputfile,'w')
    for i in range(1,arr.shape[0]):
        for x in range(0,arr.shape[1]):
            fid.write(str(arr[i][x]))
            if(x!=arr.shape[1]-1):
                fid.write(" ")
            else:
                fid.write('\n')