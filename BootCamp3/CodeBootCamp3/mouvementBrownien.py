"""
Simulation/tracer, la trajectoire Brownienne d’une
bactérie, si on ignore les effets de son flagelle
"""

#import
import random as rd
import matplotlib.pyplot as plt

#variable global
x0=0
y0=0
N=1000000
dx=1
dy=1
xL=[x0]
yL=[y0]

#def focntion
def mouvBrownien(x,y):
	nbA=rd.randint(1,4)
	match nbA:
		case 1: x+=dx
		case 2: x-=dx
		case 3: y+=dy
		case 4: y-=dy
		case _: pass
	return x,y
	

#boucle Principal
x=x0
y=y0
for _ in range(N):
	x,y=mouvBrownien(x,y)
	xL.append(x)
	yL.append(y)

#affichage

plt.Figure()
plt.plot(xL,yL,"r")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Mouvement Bronien d'une bactérie")
plt.show()
