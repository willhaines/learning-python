# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

x = array([0,1,2,3,4,5,6,7,8,9])
y = 2*x;

plt.figure(1)
plt.ylabel("two times x")
plt.plot(x,y)
plt.show()
