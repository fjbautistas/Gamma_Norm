#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
#-----Multiplots------

import Multiplot_P_NaI3 as NaI3

NaI_Thx=NaI3.PatronThRebinX2
NaI_Thy=NaI3.ThDef
NaI_Ux=NaI3.PatronURebinX2
NaI_Uy=NaI3.UDef
NaI_Kx=NaI3.PatronKRebinX2
NaI_Ky=NaI3.KDef

fig = plt.figure()
ax=fig.add_subplot(111)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#plt.rc('font', weight='bold')
#plt.rcParams['text.latex.preamble'] = [r'\usepackage{sfmath} \boldmath']
plt.gcf().subplots_adjust(bottom=0.11)   #esto es para la grafica!
plt.gcf().subplots_adjust(right=0.97)    #esto es para la grafica!
plt.gcf().subplots_adjust(left=0.09)     #esto es para la grafica! 
plt.gcf().subplots_adjust(top=0.94)      #esto es para la grafica!
plt.ylabel(r"\textbf{cuentas $/$ segundo}",fontsize=20)
plt.xlabel(r"\textbf{E$_\gamma$ (keV)}",fontsize=20)
plt.xticks(fontsize=16.5)
plt.yticks(fontsize=16.5)
#----------------------------------------------------------
figura1_0, = ax.plot(NaI_Thx,NaI_Thy*60/\
                     1775.61,#en min
                     ls="-",lw=2.0)
figura1_1, = ax.plot(NaI_Kx,NaI_Ky*60/\
                     1775.61,#en min
                     ls="-",lw=2.0)
figura1_2, = ax.plot(NaI_Ux,NaI_Uy*60/\
                     1775.31,#en min
                     ls="-",lw=2.0)

ax.fill_between(NaI_Thx[247:275],NaI_Thy[247:275]*60/1775.61)
ax.fill_between(NaI_Kx[135:155],NaI_Ky[135:155]*60/1775.61)
ax.fill_between(NaI_Ux[166:186],NaI_Uy[166:186]*60/1775.61)

ax.legend([figura1_0,figura1_1,figura1_2],
           [r"\textbf{$^{232}$Th}",r"\textbf{$^{40}$K}",r"\textbf{$^{238}$U}"],
           fontsize=18,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#---------------df-------------------------------------------
plt.axvline(x=1353,ymin=0, ymax = .45, linewidth=2, color='k')
plt.axvline(x=1540,ymin=0, ymax = .45, linewidth=2, color='k')
plt.axvline(x=1660,ymin=0, ymax = .25, linewidth=2, color='k')
plt.axvline(x=1852,ymin=0, ymax = .25, linewidth=2, color='k')
plt.axvline(x=2495,ymin=0, ymax = .2, linewidth=2, color='k')
plt.axvline(x=2720,ymin=0, ymax = .2, linewidth=2, color='k')
#plt.axvline(x=1461)

ax.text(1390,6.5 , r'\textbf{$^{40}$K}', fontsize=20)
ax.text(1711,3.7 , r'\textbf{$^{232}$U}', fontsize=20)
ax.text(2522,2.7 , r'\textbf{$^{232}$Th}', fontsize=20)

plt.setp(ax.get_xticklabels(), rotation='horizontal', fontsize=19.5)
plt.setp(ax.get_yticklabels(), rotation='horizontal', fontsize=19.5)

xmin0=50
xmax0=2900

ax.set_xlim(xmin0,xmax0)
ax.set_ylim(0,15)

space1y=10
space2y=1

ax.set_xticks([250,500,750,1000,1250,1461,1765,2000,2250,2614])

fig.set_size_inches(13.5, 6.5, forward=True)
fig.subplots_adjust(hspace=0)

fig.show()
#f.legend()
fig.savefig('figuras/MultiplotROIS.pdf')
plt.show()
