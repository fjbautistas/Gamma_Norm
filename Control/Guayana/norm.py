#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import ControlBGO as BGO
import ControlNaI2x2 as NaI2x2
import ControlNaI3x3 as NaI3x3
import ControlCsI as CsI
import ControlGe as Ge



################################Figura1#################################
f, ((ax1), (ax2)) = plt.subplots(2, sharex='col', sharey=False)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.14)   #esto es para la grafica!
plt.gcf().subplots_adjust(right=0.89)    #esto es para la grafica!
plt.gcf().subplots_adjust(left=0.14)     #esto es para la grafica! 
plt.gcf().subplots_adjust(top=0.86)      #esto es para la grafica!
#plt.ylabel(r"\textbf{Cuentas $/$ segundo}",fontsize=18)
#plt.xlabel(r"\textbf{Energ\'ia (keV)}",fontsize=18)
#plt.xticks(fontsize=16.5)
#plt.yticks(fontsize=16.5)

figura_ThGe1,=ax1.plot(Ge.SubSpectraList[1].cal_energy,
                       (Ge.SubSpectraList[1].counts*60/Ge.SubSpectraList[1].LifeTime),
                       ls="steps-mid",lw=2.0)
figura_UGe1,=ax1.plot(Ge.SubSpectraList[2].cal_energy,
                      (Ge.SubSpectraList[2].counts*60/Ge.SubSpectraList[2].LifeTime),
                      ls="steps-mid",lw=2.0)
figura_mBGO,=ax1.plot(BGO.SubSpectraList[3].cal_energy,
                      (BGO.SubSpectraList[3].counts*60/BGO.SubSpectraList[3].LifeTime)*10,
                      ls="steps-mid",lw=2.0)
figura_mCsI,=ax1.plot(CsI.SubSpectraList[3].cal_energy,
                      (CsI.SubSpectraList[3].counts*60/CsI.SubSpectraList[3].LifeTime)*10,
                      ls="steps-mid",lw=2.0)

figura_ThGe1,=ax2.plot(Ge.SubSpectraList[1].cal_energy,
                       (Ge.SubSpectraList[1].counts*60/Ge.SubSpectraList[1].LifeTime),
                       ls="steps-mid",lw=2.0)
figura_UGe1,=ax2.plot(Ge.SubSpectraList[2].cal_energy,
                      (Ge.SubSpectraList[2].counts*60/Ge.SubSpectraList[2].LifeTime),
                      ls="steps-mid",lw=2.0)
figura_mNaI2x2_3,=ax2.plot(NaI2x2.SubSpectraList[3].cal_energy,
                           (NaI2x2.SubSpectraList[3].counts*60/\
                            NaI2x2.SubSpectraList[3].LifeTime)*10,
                           ls="steps-mid",lw=2.0,color='maroon')
figura_mNaI3x3_3,=ax2.plot(NaI3x3.SubSpectraList[3].cal_energy,
                           (NaI3x3.SubSpectraList[3].counts*60/\
                            NaI3x3.SubSpectraList[3].LifeTime)*10,
                           ls="steps-mid",lw=2.0,color='navy')

ax1.legend([figura_ThGe1,figura_UGe1,figura_mBGO,figura_mCsI],
           [r"$^{232}$Th (Ge)",r"$^{238}$U (Ge)",r"Muestra BGO$\times{10}$",
            r"Muestra CsI$\times{10}$"],
           fontsize=16.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)
ax2.legend([figura_ThGe1,figura_UGe1,
            figura_mNaI2x2_3,figura_mNaI3x3_3],
           [r"$^{232}$Th (Ge)",r"$^{238}$U (Ge)",
            r"Muestra NaI($2\times2$)$\times{15}$",
            r"Muestra NaI($3\times3$)$\times{10}$"],
           fontsize=16.5, bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax2.get_xticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=18.5)

f.text(0.02, 0.5, r"\textbf{Cuentas $/$ min}", fontsize=19, ha='center', va='center', rotation='vertical')
f.text(0.5, 0.03, r"\textbf{Energ\'ia (keV)}", fontsize=19, ha='center', va='center')

xmin0=1600
xmax0=2712

ax1.set_xlim(xmin0,xmax0)
ax2.set_xlim(xmin0,xmax0)

ax1.set_ylim(0,8)
ax2.set_ylim(0,8)

space1y=50
space2y=10

# ax1.set_yticks(range(int(0)+space1y,int(280),50))
# ax2.set_yticks(range(int(0)+space1y,int(200),space1y))

space1x=210
space2x=65

#ax1.set_xticks([1361,1461,1561,1661])#range(int(xmin0),int(xmax0),space2x))
#ax2.set_xticks([550,583,609,650,700,750,800])
#ax2.set_xticks([1350,1461,1550,1650])
#ax4.set_xticks([550,583,609,650,700,750,800])


#ax4.set_xticks(range(int(xmin1),int(xmax1),space1x))
f.set_size_inches(14.5, 7.5, forward=True)
f.subplots_adjust(hspace=0)
f.savefig('Multiplot2.pdf')
f.show()
