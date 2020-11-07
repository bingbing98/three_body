import matplotlib.pyplot as plt
import numpy as np
import math

#=======================================
# a simple test for three-body problem
# by Wang Bingwen 2020-09-03
# parameter t can not be too large
#=======================================



#------------------------
# mass , initial position , initial velocity

mass1 = 15
mass2 = 15
mass3 = 15

posi1 = np.array([200,60])
posi2 = np.array([-120,-200])
posi3 = np.array([-110,150])

v1 = np.array([0.1,0.1])
v2 = np.array([0.1,0.2])
v3 = np.array([0.1,0])

#------------------------


def gravity(mm1,mm2):
	# F = G*(M1 * M2)/ R^2
	#G = 6.67e-11
	G = 1
	R = np.linalg.norm(mm1.p - mm2.p,2)
	#print(R)
	F = G*(mm1.m*mm2.m)/(R**2)
	vector_f = (mm2.p - mm1.p)/np.linalg.norm(mm2.p - mm1.p,2)*F
	#print(vector_f)
	return vector_f

def vel(v1,v2):
	return v1+v2

def new_v(mm1,mm2,mm3):  
	# for m1
	
	v1_1 = gravity(mm1,mm2)/mm1.m*t
	v1_2 = gravity(mm1,mm3)/mm1.m*t
	
	v = vel(v1_1,v1_2)
	#print(v1_1,v1_2,v)
	return vel(mm1.v,v)

class body():
	def __init__(self):
		self.m = 0
		self.v = np.array([0,0])
		self.p = np.array([0,0])

m1 = body()
m1.m = mass1
m1.v = v1
m1.p = posi1

m2 = body()
m2.m = mass2
m2.v = v2
m2.p = posi2

m3 = body()
m3.m = mass3
m3.v = v3
m3.p = posi3

t = 0.05 # assume delta_time = 0.1

p1x,p2x,p3x = [],[],[]
p1y,p2y,p3y = [],[],[]
plt.figure()
plt.ion()
for i in range(200000):
	p1x.append(m1.p[0])
	p1y.append(m1.p[1])

	p2x.append(m2.p[0])
	p2y.append(m2.p[1])

	p3x.append(m3.p[0])
	p3y.append(m3.p[1])


	# for m1
	m1.v = new_v(m1,m2,m3)
	
	# for m2
	m2.v = new_v(m2,m1,m3)
	
	# for m3
	m3.v = new_v(m3,m1,m2)
	#print(m1.v,m2.v,m3.v)

	m1.p = m1.v * t + m1.p
	m2.p = m2.v * t + m2.p
	m3.p = m3.v * t + m3.p
	if len(p1x) == 10000:
		p1x.pop(0)
		p1y.pop(0)
		p2x.pop(0)
		p2y.pop(0)
		p3x.pop(0)
		p3y.pop(0)

	if i%100 == 0:
		plt.clf()	
		plt.plot(p1x,p1y,color='r')
		plt.plot(p2x,p2y,color='g')
		plt.plot(p3x,p3y,color='b')
		plt.plot(p1x[-1],p1y[-1],'or',markersize=m1.m)
		plt.plot(p2x[-1],p2y[-1],'og',markersize=m2.m)
		plt.plot(p3x[-1],p3y[-1],'ob',markersize=m3.m)
		plt.pause(0.000001)
	
	
plt.ioff()
