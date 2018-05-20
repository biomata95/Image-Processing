import sys
import os
from math import sqrt
import numpy as np
import numpy.random as rnd
import glob
import cv2
import math
import colorsys
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
import warnings
import random
style.use('fivethirtyeight')

def leitura(arquivo): # leitura do arquivo de imagem
	img = cv2.imread(arquivo) 
	return img

def visualizarImagem(img): # visualiza imagem
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def KNN(data,predict,k):	
	if len(data) >= k:
		print('k eh menor do que o total de grupos')
	distances=[]
	for group in data:
		for features in data[group]:
			distancia_euclidiana=np.linalg.norm(np.array(features)-np.array(predict))
			distances.append([distancia_euclidiana,group])
	votos=[i[1] for i in sorted(distances)[:k]]
	print(Counter(votos).most_common(1))
	resultado_votos=Counter(votos).most_common(1)[0][0]
	return resultado_votos
	
def main():

	arquivo=sys.argv[1]; # nome do arquivo -> imagem
 	img=leitura(arquivo) #leitura do arquivo	
	dataset={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]],'s':[[11,5],[12,3],[10,1]]}
	new_features=[3,2]
	resultado=KNN(dataset,new_features,4)
	[[plt.scatter(ii[0],ii[1],s=200, color=i) for ii in dataset[i]] for i in dataset]
	plt.scatter(new_features[0],new_features[1],color=resultado)
	plt.show()
	print(resultado)
	#visualizarImagem(img) # visualiza a Imagem resultante
	

if __name__ == "__main__":
	main()

