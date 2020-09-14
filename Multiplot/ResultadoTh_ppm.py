#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import  ScalarFormatter

fig = plt.figure()
ax = fig.add_subplot(111)
plt.gcf().subplots_adjust(bottom=0.40)
plt.gcf().subplots_adjust(right=0.99)
plt.gcf().subplots_adjust(left=0.16)
plt.gcf().subplots_adjust(top=0.98)

#------------------------------------
#ax2 = ax.twinx()
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
data=np.genfromtxt("totalData.dat")
ax.set_xlabel(r"Detector",fontsize=25)
ax.set_ylabel(r"$C$($^{232}$Th) [ppm]",fontsize=25)
#ax2.set_ylabel(r"$^{40}$K concentrations [ppm]",fontsize=25)

#-----------------------------------------------------------------------------------------
test, =ax.plot(data[:,0][0], data[:,3][0], marker='D', markersize=10, color = 'blue')
ax.errorbar(data[:,0][0], data[:,3][0], yerr=data[:,4][0], marker='D',markersize=10,ls = '-', color="blue" ,lw = 2, capsize=10)
            
test1, =ax.plot(data[:,0][1], data[:,3][1], marker='D', markersize=10, color = 'green')
ax.errorbar(data[:,0][1], data[:,3][1], yerr=data[:,4][1], marker='D',markersize=10,ls = '-', color="green" ,lw = 2, capsize=10)

test2, =ax.plot(data[:,0][4], data[:,3][4], marker='D', markersize=10, color = 'orangered')
ax.errorbar(data[:,0][4], data[:,3][4], yerr=data[:,4][4], marker='D',markersize=10,ls = '-', color="navy" ,lw = 2, capsize=10)

test3, =ax.plot(data[:,0][3], data[:,3][3], marker='D', markersize=10, color = 'navy')
ax.errorbar(data[:,0][3], data[:,3][3], yerr=data[:,4][3], marker='D',markersize=10,ls = '-', color="orangered" ,lw = 2, capsize=10)

test4, =ax.plot(data[:,0][2], data[:,3][2], marker='D', markersize=10, color = 'red')
ax.errorbar(data[:,0][2], data[:,3][2], yerr=data[:,4][2], marker='D',markersize=10,ls = '-', color="red" ,lw = 2, capsize=10)            


#-----------------------------------------------------------------------------------------

plt.setp(ax.get_xticklabels(), rotation='vertical', fontsize=20.5)
plt.setp(ax.get_yticklabels(), rotation='horizontal', fontsize=25.5)
#plt.legend(loc="upper left",fontsize=18,bbox_to_anchor=(0.2,0.9),ncol=2)
#ax.legend([test,test1,test2,test3,test4],[r"HPGe", r"CsI","BGO",r"NaI($2\times 2$)",r"NaI($3\times 3$)"],fontsize=24, bbox_to_anchor=(0., 1.02, 1., .102), loc=2, ncol=3,mode="expand", borderaxespad=0.)

xmin=1.2
xmax=3.8

ax.set_xlim(xmin,xmax)

ax.set_xticks([data[:,0][0],data[:,0][1],data[:,0][4],data[:,0][2],data[:,0][3]])
labels = ax.get_xticks().tolist()
labels[0] = r'HPGe'
labels[1] = r'CsI'
labels[2] = r'NaI($3^{\prime\prime}\times 3^{\prime\prime})$'
labels[3] = r'BGO'
labels[4] = r'NaI($2^{\prime\prime}\times 2^{\prime\prime})$'
#labels[4] = r'NaI($3\times 3)$'
ax.set_xticklabels(labels)

ymin=41000
ymax=49000
#ax2.set_ylim(ymin,ymax)
#labelsy = (ax2.get_yticks()/10000).tolist()
#labelsy[-1] = r'$\times{10^{4}}$'
#ax2.set_yticklabels(labelsy,fontsize=23)
#ax2.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
#plt.tight_layout()
fig.savefig('figuras/Th_ppm.pdf')
plt.show()
