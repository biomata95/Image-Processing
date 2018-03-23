import sys
import os
import numpy as np
import numpy.random as rnd
import glob
import cv2
import math
import colorsys
import matplotlib.pyplot as plt
from random import randint
import pdb

A=np.array([3,4,5,0])
B=np.array([2,1,0,0])
tamA=len(A)
tamB=len(B)
tamM=4

k=0
M=np.array([0,0,0,0])
for n in range(0,tamM):
	soma=0
	for k in range(0,n-k+2):
		soma=soma+A[k]*B[n-k]
	print('\n')
	M[n]=soma
print(M)



