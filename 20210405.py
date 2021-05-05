#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: Zhen YANG
# created at:4/5/2021 9:09 PM
# contact: zhyang8-c@my.cityu.edu.hk

import numpy as np

# a = np.array([[1,2,3,4], [2,3,4,5]])
# b = np.array([[2,3,4,5],[5,6,7,8]])
# print("a: ", a.shape, a)
# print("b: ", b.shape, b)
# c = np.stack((a,b), axis=0)
# print("c: ", c.shape, c)

# a = np.array([[1,2,3,4], [2,3,4,5], [3,4,5,6]])
# b = np.array([[2,3,4,5],[5,6,7,8]])
# print("a: ", a.shape, a)
# print("b: ", b.shape, b)
# c = np.vstack((a,b))
# print("c: ", c.shape, c)

a = np.array([[1,2], [2,3], [3,4]])
b = np.array([[2,3,4,5],[5,6,7,8], [5,6,7,8]])
print("a: ", a.shape, a)
print("b: ", b.shape, b)
c = np.hstack((a,b))
print("c: ", c.shape, c)


