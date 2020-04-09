import math
import numpy as numpy
import simplekml

kml = simplekml.Kml()

R = 0.003333;
r = 0.000666;
a = 0.001333;
x1 = R + r - a;
y1 = 0;
pie = math.pi;
nReverse = 10;
for t in numpy.arange(0.0, pie*nReverse, 0.1):
	x2 = (R+r)*math.cos((r/R)*t) - a*math.cos((1+r/R)*t);
	y2 = (R+r)*math.sin((r/R)*t) - a*math.sin((1+r/R)*t);
	p1 = -118.285556;
	p2 = 34.020869;
	kml.newpoint(coords=[((x2+p1),(y2+p2))])

kml.save("spiro.kml")
	
    	