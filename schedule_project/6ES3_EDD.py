#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#EDD
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn import metrics
from numpy import linalg as LA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
import time
import sys

edd=np.zeros((2,10));
edd_result=np.zeros((3,11));
i=0;
j=0;
c=0;
d=0;
x=0;
t=0;
Lmax=0;
x=input("how many tasks do you have?(less than 10)")
x=int(x);
if x>10: 
    print("no more than 10 tasks, try again");
    sys.exit()

print("please input the task length and due date one by one");

for i in range(0,x):
    
    print("due date for D",i+1);
    c=input();
    edd[0,i]=int(c);
    print("task length for C",i+1);
    d=input();
    edd[1,i]=int(d);
    i=i+1;

print ("task list:");
print (edd);
    
edd=edd[:,edd[0,:].argsort()];


    
i=0;
for i in range(0,10):
    edd_result[0,i]=edd[0,i];
    edd_result[1,i]=edd[1,i];
    edd_result[2,i]=t;
    t=t+edd[1,i];
    i=i+1;
    edd_result[2,i]=t;


Lmax=t-edd[0,9];
if Lmax<=0:
    print("the schedule is feasible");
elif Lmax>0:
    print("the schedule is not feasible");

print("scheduled time table: ");
table=[
    "due date",
    "task length",
    "time line"
]

print ('\n'.join(table));
print(edd_result);


