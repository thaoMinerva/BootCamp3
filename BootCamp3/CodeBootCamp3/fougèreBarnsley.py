"""
construction de la fougère de Barnsley 
"""
#import
import random as rd
import matplotlib.pyplot as plt

#varaible global
x0=0
y0=0
N=500000
xL=[x0]
yL=[y0]

#def func
def f1(x,y):
	return 0, 0.16*y
	
def f2(x,y):
	return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
	
def f3(x,y):
	return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
	
def f4(x,y):
	return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
	
def rdMa(x,y):
	nbA=rd.randint(1,100)
	if nbA==1:
		x,y = f1(x,y)
	elif 2<= nbA <= 86:
		x,y = f2(x,y)
	elif 87<=nbA <= 93:
		x,y = f3(x,y)
	elif 94 <= nbA <=100:
		x,y =f4(x,y)
	else:
		print("Ses la merde")
	return x,y


x=x0
y=y0
for _ in range(N):
	x,y=rdMa(x,y)
	xL.append(x)
	yL.append(y)

#affichage

plt.figure()
plt.title("La fougère de Barnsley")
plt.scatter(xL,yL, s = 0.2, edgecolors="green")
plt.xlim(-4,4)
plt.ylim(0,11)
plt.show()
