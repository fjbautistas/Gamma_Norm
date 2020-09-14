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
f, ((ax1), (ax3)) = plt.subplots(2, sharex='col', sharey=False)


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.12)
plt.gcf().subplots_adjust(right=0.99)
plt.gcf().subplots_adjust(left=0.10)
plt.gcf().subplots_adjust(top=0.96)

figura_Ge,=ax1.plot(Ge.SubSpectraList[3].cal_energy,
                 (Ge.SubSpectraList[3].counts*60/Ge.SubSpectraList[3].LifeTime),
                 ls="steps-mid",lw=2.0)
figura_mBGO,=ax1.plot(BGO.SubSpectraList[3].cal_energy,
                      (BGO.SubSpectraList[3].counts*60/BGO.SubSpectraList[3].LifeTime),
                      ls="steps-mid",lw=2.0)
figura_mCsI,=ax1.plot(CsI.SubSpectraList[3].cal_energy,
                      (CsI.SubSpectraList[3].counts*60/CsI.SubSpectraList[3].LifeTime),
                      ls="steps-mid",lw=2.0)

figura1_Ge,=ax3.plot(Ge.SubSpectraList[3].cal_energy,
                 (Ge.SubSpectraList[3].counts*60/Ge.SubSpectraList[3].LifeTime),
                     ls="steps-mid",lw=2.0)

figura_mNaI2x2,=ax3.plot(NaI2x2.SubSpectraList[3].cal_energy,
                         (NaI2x2.SubSpectraList[3].counts*60/\
                          NaI2x2.SubSpectraList[3].LifeTime),
                         ls="steps-mid",lw=2.0,color='maroon')
figura_mNaI3x3,=ax3.plot(NaI3x3.SubSpectraList[3].cal_energy,
                         (NaI3x3.SubSpectraList[3].counts*60/\
                          NaI3x3.SubSpectraList[3].LifeTime),
                         ls="steps-mid",lw=2.0,color='navy')

ax1.legend([figura1_Ge,
            figura_mBGO,figura_mCsI],
           [r"Muestra (Ge)",r"Muestra (CsI)",r"Muestra (BGO)"],
           fontsize=16.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)
ax3.legend([figura1_Ge,figura_mNaI2x2,figura_mNaI3x3],
          [r"Muestra (Ge)",r"Muestra (NaI$2\times2$)",r"Muestra (NaI$3\times3$)"],
           fontsize=16.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax3.get_xticklabels(), rotation='horizontal', fontsize=18.5)
plt.setp(ax3.get_yticklabels(), rotation='horizontal', fontsize=18.5)

f.text(0.05, 0.5, r"\textbf{Cuentas $/$ min}", fontsize=19, ha='center', va='center', rotation='vertical')
f.text(0.5, 0.04, r"\textbf{Energ\'ia (keV)}", fontsize=19, ha='center', va='center')

xmin0=20
xmax0=2800
y1min=0
y1max=60
space1y=10

ax1.set_xlim(xmin0,xmax0)
ax3.set_xlim(xmin0,xmax0)
ax1.set_ylim(0,45)
ax3.set_ylim(0,60)

ax1.set_yticks(range(int(y1min),int(y1max),space1y))
ax3.set_yticks(range(int(y1min),int(y1max),space1y))

f.set_size_inches(13.5, 6.5, forward=True)
f.subplots_adjust(hspace=0)

plt.show()
