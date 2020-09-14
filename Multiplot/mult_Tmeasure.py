#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
#-----Multiplots------
import ControlGe as Ge
import Multiplot_P_BGO as BGO
import Multiplot_P_CsI as CsI
import Multiplot_P_NaI3 as NaI3
import Multiplot_P_NaI2 as NaI2

GuayanaGe=Ge.SubSpectraList[3]
PatronUGe=Ge.SubSpectraList[2]
PatronThGe=Ge.SubSpectraList[1]
PatronKGe=Ge.SubSpectraList[0]

f, ((ax1, ax2)) = plt.subplots(1, 2, sharex='col', sharey=False)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.12)
plt.gcf().subplots_adjust(right=0.95)
plt.gcf().subplots_adjust(left=0.07)
plt.gcf().subplots_adjust(top=0.96)
#----------------------------------------------------------
figura1_0, = ax1.plot(GuayanaGe.cal_energy,
                      GuayanaGe.counts*60*8/GuayanaGe.LifeTime,#en min
                      ls="steps-mid",lw=2.0,color='purple')
figura1_1, = ax1.plot(BGO.GuayanaRebinX2,
                      BGO.GuayanaDef*5,ls="steps-mid",#BGO x 5
                      lw=2.0,color="red")
figura1_2, = ax1.plot(CsI.GuayanaRebinX2,
                      CsI.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color="green")#CsI x 5
figura1_3, = ax1.plot(NaI3.GuayanaRebinX2,
                      NaI3.GuayanaDef*3,ls="steps-mid",lw=2.0,
                      color='navy')#BGO x 5
figura1_4, = ax1.plot(NaI2.GuayanaRebinX2,
                      NaI2.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color='maroon')

ax1.legend([figura1_0,figura1_1,figura1_2,figura1_4,figura1_3],
           [r"Ge$\times 8$",
            r"BGO$\times 5$",
            r"CsI$\times 5$",
            r"NaI($2''\times2''$)$\times 5$",
            r"NaI($3''\times3''$)$\times 3$"],
           fontsize=18.5,bbox_to_anchor=(0., 0.895, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#---------------df-------------------------------------------
figura2_0, = ax2.plot(GuayanaGe.cal_energy,
                      GuayanaGe.counts*60*15/GuayanaGe.LifeTime,#en min
                      ls="steps-mid",lw=2.0,color='purple')
figura2_1, = ax2.plot(BGO.GuayanaRebinX2,
                      BGO.GuayanaDef*5,ls="steps-mid",#BGO x 5
                      lw=2.0,color="red")
figura2_2, = ax2.plot(CsI.GuayanaRebinX2,
                      CsI.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color="green")#CsI x 5
figura2_3, = ax2.plot(NaI3.GuayanaRebinX2,
                      NaI3.GuayanaDef*3,ls="steps-mid",lw=2.0,
                      color='navy')#BGO x 5
figura2_4, = ax2.plot(NaI2.GuayanaRebinX2,
                      NaI2.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color='maroon')

ax2.legend([figura2_0,figura2_1,figura2_2,figura2_4,figura2_3],
           [r"Ge$\times 15$",
            r"BGO$\times 5$",
            r"CsI$\times 5$",
            r"NaI($2''\times2''$)$\times 5$",
            r"NaI($3''\times 3''$)$\times 3$"],
           fontsize=18.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=9, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#----------------------------------------------------------

plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax2.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=20.5)

f.text(0.02, 0.55, r"\textbf{cuentas $/$ min}", fontsize=21, ha='center', va='center', rotation='vertical')
f.text(0.5, 0.03, r"\textbf{E$_{\gamma}$ (keV)}", fontsize=21, ha='center', va='center')

xmin0=1350
xmax0=1680

xmin1=1670
xmax1=2770

y1min=0
y1max=60
y2max=7

ax1.set_xlim(xmin0,xmax0)
ax2.set_xlim(xmin1,xmax1)

ax1.set_ylim(0,60)
ax2.set_ylim(0,6)

space1y=10
space2y=1

ax1.set_yticks(range(int(y1min),int(y1max),space1y))
ax2.set_yticks(range(int(y1min),int(y2max),space2y))

space1x=200
space2x=65

ax1.set_xticks([1361,1461,1561,1661])#range(int(xmin0),int(xmax0),space2x))
ax2.set_xticks([1764,1979,2190,2401,2614])
#ax3.set_xticks([1350,1461,1550,1650])
#ax4.set_xticks([1764,1979,2190,2401,2614])


#ax4.set_xticks(range(int(xmin1),int(xmax1),space1x))
f.set_size_inches(13.5, 6.5, forward=True)
f.subplots_adjust(hspace=0)

f.show()
#f.legend()
f.savefig('figuras/MultiplotROI2.pdf')
plt.show()
