import sys
import os
import numpy as np
import numpy.random as rnd
import glob
import cv2
import math
import colorsys
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


#Classificacao com Histogramas Exercicio 2


# FONTE da classificacao: https://mpatacchiola.github.io/blog/2016/11/12/the-simplest-classifier-histogram-intersection.html


#hist= cv2.calcHist([imagem],[0],None,[256],[0,256])
#correlation = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CORREL)
#quiQuadrado = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CHISQR)
#interse = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_INTERSECT)
#battha = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_BHATTACHARYYA)

def leituraArquivo(arqImagem):
	imagem = cv2.imread(arqImagem) 
	return imagem

def visualizarImagem(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def histograma(imagemTeste,listaFiguras):
	histTeste = cv2.calcHist([imagemTeste],[0],None,[256],[0,256])
	matrizValores = [[0.0 for i in range(0,4)]for j in range(0,len(listaFiguras))]
	correlation=0
	quiQuadrado=0
	interse=0
	battha=0
	for i in range(0,len(listaFiguras)):
		comparativa=cv2.imread(listaFiguras[i])
		histComparativa = cv2.calcHist([comparativa],[0],None,[256],[0,256])
		correlation = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CORREL)
		quiQuadrado = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_CHISQR)

		interse = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_INTERSECT)

		battha = cv2.compareHist(histTeste,histComparativa,cv2.cv.CV_COMP_BHATTACHARYYA)

		matrizValores[i][0]=correlation
		matrizValores[i][1]=quiQuadrado
		matrizValores[i][2]=interse
		matrizValores[i][3]=battha


	fig = plt.figure("Histograma Comparacoes")

	fig.suptitle("Histograma Comparacoes", fontsize = 20)
	plt.rcParams["figure.figsize"] = [15,7]
	fig, axes = plt.subplots(nrows=3,ncols=7)

	axes[0,3].imshow(imagemTeste)
	axes[0,3].axis('off')
	axes[0,3].set_title('Figura Teste')
	k=0
	contL=0
	for i in range(0,3):
		cont=0
		for j in range(0,math.trunc(len(listaFiguras)/2)):
			if(i==0):
				axes[i,j].axis('off')
			else:
				imag=cv2.imread(listaFiguras[k])
				axes[i,j].axis('off')

				coluna=matrizValores[k]			
				
				resultado=' '
				if(i==1):
					if(coluna[0]==1):
						resultado='(Parecido)'
					if(coluna[0]<1 and coluna[0]>=0.7):
						resultado='(Meio-parecido)'
					if(coluna[0]<0.7 and coluna[0]>=-1):
						resultado='(Diferente)'
					axes[i,j].set_title(resultado)
				if(i==2):		
					if(coluna[0]==1):
						resultado='(Parecido)'
					if(coluna[0]<1 and coluna[0]>=0.7):
						resultado='(Meio-parecido)'
					if(coluna[0]<0.7 and coluna[0]>=-1):
						resultado='(Diferente)'
					axes[i,j].set_title(resultado)
					cont=cont+0.14
				axes[i,j].imshow(imag)
				k=k+1
		contL=contL+0.07
	
	fig.show()
	plt.pause(100000000)
	
	



def main():

	arquivo=sys.argv[1]; # nome do arquivo -> imagem
	lista=glob.glob("Archive/*.png") # Varreduras dos arquivos .png do diretorio Archive/
	img=leituraArquivo(arquivo)
	histograma(img,lista)


if __name__ == "__main__":
	main()

