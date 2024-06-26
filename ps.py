# -*- coding: utf-8 -*-
"""ps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16LR65jmFoSIN_17el_OFGqrz7zyfYFrm
"""

import numpy as np
import matplotlib.pyplot as plt

def R(x,y,px,py):
  top=(-x*px)-(y*py)+np.sqrt((r*r)-((x*x)+(y*y)))
  bottom=np.sqrt((px*px)+(py*py)+1)*r
  return top/bottom

ps1=1
qs1=1
ps2=0
qs2=1
ps3=1
qs3=0
ps4=2
qs4=5
r=24

s=np.array([[-ps1/(np.sqrt(ps1*ps1 + qs1*qs1 + 1)), -qs1/(np.sqrt(ps1*ps1 + qs1*qs1 + 1)), 1/(np.sqrt(ps1*ps1 + qs1*qs1 + 1))],[-ps2/(np.sqrt(ps2*ps2 + qs2*qs2 + 1)), -qs2/(np.sqrt(ps2*ps2 + qs2*qs2 + 1)), 1/(np.sqrt(ps2*ps2 + qs2*qs2 + 1))],
            [-ps3/(np.sqrt(ps3*ps3 + qs3*qs3 + 1)), -qs3/(np.sqrt(ps3*ps3 + qs3*qs3 + 1)), 1/(np.sqrt(ps3*ps3 + qs3*qs3 + 1))],[-ps4/(np.sqrt(ps4*ps4 + qs4*qs4 + 1)), -qs4/(np.sqrt(ps4*ps4 + qs4*qs4 + 1)), 1/(np.sqrt(ps4*ps4 + qs4*qs4 + 1))]])

s

s_T=np.dot(np.transpose(s),s)
s_inv=np.linalg.inv(s_T)
s_TT=np.dot(s_inv,np.transpose(s))

for i in range (0,64):
  for j in range (0,64):
    E1[i,j]=R(i-32,j-32,ps1,qs1)
    E2[i,j]=R(i-32,j-32,ps2,qs2)
    E3[i,j]=R(i-32,j-32,ps3,qs3)
    E4[i,j]=R(i-32,j-32,ps4,qs4)

E1=np.ones((64,64),dtype=float)
E2=np.ones((64,64),dtype=float)
E3=np.ones((64,64),dtype=float)
E4=np.ones((64,64),dtype=float)

E1=np.nan_to_num(E1,nan=0)
E2=np.nan_to_num(E2,nan=0)
E3=np.nan_to_num(E3,nan=0)
E4=np.nan_to_num(E4,nan=0)

p_t=np.ones((64,64),dtype=float)
q_t=np.ones((64,64),dtype=float)
p=np.ones((64,64),dtype=float)
q=np.ones((64,64),dtype=float)
r=24
for i in range(0,64):
  for j in range(0,64):
    x=i-32
    y=j-32
    p_t[i,j]=((-1)*(x))/(np.sqrt((r*r)-(x*x + y*y)))
    q_t[i,j]=((-1)*(y))/(np.sqrt((r*r)-(x*x + y*y)))

for i in range(0,64):
  for j in range(0,64):
    E=np.ones((4,1),dtype=float)
    E[0,0]=E1[i,j]
    E[1,0]=E2[i,j]
    E[2,0]=E3[i,j]
    E[3,0]=E4[i,j]
    x=np.dot(s_TT,E)
    p[i,j]=-1*(x[0,0]/x[2,0])
    q[i,j]=-1*(x[1,0]/x[2,0])
    alb=np.linalg.norm(x)
    p[i,j]=p[i,j]/alb
    q[i,j]=q[i,j]/alb

p[30,30]

p_t[30,30]

