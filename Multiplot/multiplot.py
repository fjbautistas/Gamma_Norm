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

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey=False)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.12)
plt.gcf().subplots_adjust(right=0.95)
plt.gcf().subplots_adjust(left=0.07)
plt.gcf().subplots_adjust(top=0.96)
#----------------------------------------------------------
figura1_0, = ax1.plot(PatronKGe.cal_energy,
                      PatronKGe.counts*60/PatronKGe.LifeTime,#en min
                      ls="steps-mid",lw=2.0,color='chartreuse')
figura1_1, = ax1.plot(BGO.GuayanaRebinX2,
                      BGO.GuayanaDef*5,ls="steps-mid",#BGO x 5
                      lw=2.0,color="red")
figura1_2, = ax1.plot(CsI.GuayanaRebinX2,
                      CsI.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color="green")#CsI x 5

ax1.legend([figura1_0,figura1_1,figura1_2],
           [r"$^{40}$K (Ge)",
            r"Muestra BGO$\times 5$",
            r"Muestra CsI$\times 5$"],
           fontsize=17.3,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#---------------df-------------------------------------------
figura2_0, = ax2.plot(PatronThGe.cal_energy,
                      PatronThGe.counts*60/PatronThGe.LifeTime,#en min
                      ls="steps-mid",lw=2.0)
figura2_01, = ax2.plot(PatronUGe.cal_energy,
                       PatronUGe.counts*60/PatronUGe.LifeTime,#en min
                       lw=2.0)
figura2_1, = ax2.plot(BGO.GuayanaRebinX2,
                      BGO.GuayanaDef*5,ls="steps-mid",#BGO x 5
                      lw=2.0,color="red")
figura2_2, = ax2.plot(CsI.GuayanaRebinX2,
                      CsI.GuayanaDef*5,ls="steps-mid",lw=2.0)#CsI x 5

ax2.legend([figura2_0,figura2_01,figura2_1,figura2_2],
           [r"$^{238}$Th (Ge)",
            r"$^{238}$U (Ge)",
            r"Muestra BGO$\times5$",
            r"Muestra CsI$\times5"],
           fontsize=17.3,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=9, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#----------------------------------------------------------
figura3_0, = ax3.plot(PatronKGe.cal_energy,
                      PatronKGe.counts*60/PatronKGe.LifeTime,
                      ls="steps-mid",
                      lw=2.0,color='chartreuse')
figura3_1, = ax3.plot(NaI3.GuayanaRebinX2,
                      NaI3.GuayanaDef*3,ls="steps-mid",lw=2.0,
                      color='navy')#BGO x 5
figura3_2, = ax3.plot(NaI2.GuayanaRebinX2,
                      NaI2.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color='maroon')

ax3.legend([figura3_0,figura3_2,figura3_1],
           [r"$^{40}$K (Ge)",
            r"Muestra NaI($2''\times2''$)$\times 5$",
            r"Muestra NaI($3''\times3''$)$\times 3$"],
           fontsize=17.3,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#----------------------------------------------------------
figura4_0, = ax4.plot(PatronThGe.cal_energy,
                      PatronThGe.counts*60/PatronThGe.LifeTime,
                      ls="steps-mid",lw=2.0)
figura4_01, = ax4.plot(PatronUGe.cal_energy,
                       PatronUGe.counts*60/PatronUGe.LifeTime,
                       ls="steps-mid",lw=2.0)
figura4_1, = ax4.plot(NaI3.GuayanaRebinX2,
                      NaI3.GuayanaDef*3,ls="steps-mid",
                      lw=2.0,color='navy')#BGO x 5
figura4_2, = ax4.plot(NaI2.GuayanaRebinX2,
                      NaI2.GuayanaDef*5,ls="steps-mid",
                      lw=2.0,color='maroon')

ax4.legend([figura4_0,figura4_01,figura4_2,figura4_1],
           [r"$^{238}$Th (Ge)",
            r"$^{238}$U (Ge)",
            r"Muestra NaI($2''\times 2''$)$\times 5$",
            r"Muestra NaI($3''\times 3''$)$\times 3$"],
           fontsize=17.3,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=9, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

#----------------------------------------------------------

plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax2.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax3.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax3.get_yticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax4.get_xticklabels(), rotation='horizontal', fontsize=20.5)
plt.setp(ax4.get_yticklabels(), rotation='horizontal', fontsize=20.5)

f.text(0.02, 0.5, r"\textbf{cuentas $/$ min}", fontsize=21, ha='center', va='center', rotation='vertical')
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
ax3.set_xlim(xmin0,xmax0)
ax4.set_xlim(xmin1,xmax1)


ax1.set_ylim(0,60)
ax2.set_ylim(0,10)
ax3.set_ylim(0,50)
ax4.set_ylim(y1min,y2max)


space1y=10
space2y=1

ax1.set_yticks(range(int(y1min),int(y1max),space1y))
ax2.set_yticks(range(int(y1min),int(y2max),space2y))
ax3.set_yticks(range(int(y1min),int(y1max),space1y))
ax4.set_yticks(range(int(y1min),int(y2max),space2y))

space1x=200
space2x=65

ax1.set_xticks([1361,1461,1561,1661])#range(int(xmin0),int(xmax0),space2x))
#ax2.set_xticks([1768,1979,2190,2401,2612])
#ax3.set_xticks([1350,1461,1550,1650])
ax4.set_xticks([1764,1979,2190,2401,2614])


#ax4.set_xticks(range(int(xmin1),int(xmax1),space1x))
f.set_size_inches(13.5, 6.5, forward=True)
f.subplots_adjust(hspace=0)

f.show()
#f.legend()
f.savefig('figuras/MultiplotROI.pdf')
plt.show()
