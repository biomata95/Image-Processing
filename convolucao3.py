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

'''
M=np.zeros(tamM) # aloca posicoes do vetor resultante com 0's
for n in range(0,tamM):
	soma=0 # soma
	for k in range(0,n-k+2): 
		soma=soma+A[k]*B[n-k]
	M[n]=soma
'''


'''matriz = np.matrix('5,8,3,4,6,2,3,7;3,2,1,1,9,5,1,0;0,9,5,3,0,4,8,3;4,2,7,2,1,9,0,6;9,7,9,8,0,4,2,4;5,2,1,8,4,1,0,9;1,8,5,4,9,2,3,8;3,7,1,2,3,4,4,6')

filtro=np.matrix('2,1,0;1,1,-1;0,-1,-2')

'''

matriz = np.matrix('1,2,3;4,5,6;7,8,9')

linhas,colunas=np.shape(matriz)

filtro=np.matrix('-1,-2,-1;0,0,0;1,2,1')

linhasF,colunasF=np.shape(filtro)


matriz2=np.zeros((linhas,colunas))
k=0
l=0
for i in range(0,linhas-1):
	for j in range(colunas-1):
	soma=0
		for k  in range(0,linhasF-1):
			if(i==k and j==l):
				soma=soma+matriz[i,j]*filtro[k,l]				
	matriz2[i,j]=soma
print(matriz2)



