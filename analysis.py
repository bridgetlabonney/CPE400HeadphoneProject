# Bridget LaBonney
# Project Analysis Code
# CPE 400

import numpy
import matplotlib.pyplot as plt

file data = open("data.txt", "r")

# Data is cleaned and turned into a text file formatted as:
# PORT SIZE PURPOSE
#on each line
d = data.readlines() #gets count no matter 
p, s, pr;
for i in d:
	 p = d[i].readline().strip().split(' ');
	 s = d[i].readline().strip().split(' ');
	 pr = d[i].readline().strip().split(' ');

# graph delay/size of packets/etc