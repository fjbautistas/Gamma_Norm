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
f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey=False)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.12)
plt.gcf().subplots_adjust(right=0.95)
plt.gcf().subplots_adjust(left=0.07)
plt.gcf().subplots_adjust(top=0.96)
#==========================================================
figura_mGe1,=ax1.plot(Ge.SubSpectraList[3].cal_energy,
                      (Ge.SubSpectraList[3].counts*60/\
                       Ge.SubSpectraList[3].LifeTime)*25,
                      ls="steps-mid",lw=2.0)
figura_mBGO1,=ax1.plot(BGO.SubSpectraList[3].cal_energy,
                       (BGO.SubSpectraList[3].counts*60/\
                        BGO.SubSpectraList[3].LifeTime)*10,
                       ls="steps-mid",lw=2.0)
figura_mCsI1,=ax1.plot(CsI.SubSpectraList[3].cal_energy,
                       (CsI.SubSpectraList[3].counts*60/\
                        CsI.SubSpectraList[3].LifeTime)*10,
                       ls="steps-mid",lw=2.0)
#===========================================================
figura_mGe2,=ax2.plot(Ge.SubSpectraList[3].cal_energy,
                      (Ge.SubSpectraList[3].counts*60/\
                       Ge.SubSpectraList[3].LifeTime)*25,
                      ls="steps-mid",lw=2.0)
figura_mBGO2,=ax2.plot(BGO.SubSpectraList[3].cal_energy,
                       (BGO.SubSpectraList[3].counts*60/\
                        BGO.SubSpectraList[3].LifeTime)*10,
                       ls="steps-mid",lw=2.0)
figura_mCsI2,=ax2.plot(CsI.SubSpectraList[3].cal_energy,
                       (CsI.SubSpectraList[3].counts*60/\
                        CsI.SubSpectraList[3].LifeTime)*10,
                       ls="steps-mid",lw=2.0)
#===========================================================
figura_mGe3,=ax3.plot(Ge.SubSpectraList[3].cal_energy,
                      (Ge.SubSpectraList[3].counts*60/\
                       Ge.SubSpectraList[3].LifeTime)*25,
                      ls="steps-mid",lw=2.0)
figura_mNaI2x2_3,=ax3.plot(NaI2x2.SubSpectraList[3].cal_energy,
                           (NaI2x2.SubSpectraList[3].counts*60/\
                            NaI2x2.SubSpectraList[3].LifeTime)*10,
                           ls="steps-mid",lw=2.0,color='maroon')
figura_mNaI3x3_3,=ax3.plot(NaI3x3.SubSpectraList[3].cal_energy,
                           (NaI3x3.SubSpectraList[3].counts*60/\
                            NaI3x3.SubSpectraList[3].LifeTime)*10,
                           ls="steps-mid",lw=2.0,color='navy')
#===========================================================
figura_mGe4,=ax4.plot(Ge.SubSpectraList[3].cal_energy,
                      (Ge.SubSpectraList[3].counts*60/\
                       Ge.SubSpectraList[3].LifeTime)*25,
                      ls="steps-mid",lw=2.0)
figura_mNaI2x2_4,=ax4.plot(NaI2x2.SubSpectraList[3].cal_energy,
                           (NaI2x2.SubSpectraList[3].counts*60/\
                            NaI2x2.SubSpectraList[3].LifeTime)*15,
                           ls="steps-mid",lw=2.0,color='maroon')
figura_mNaI3x3_4,=ax4.plot(NaI3x3.SubSpectraList[3].cal_energy,
                           (NaI3x3.SubSpectraList[3].counts*60/\
                            CsI.SubSpectraList[3].LifeTime)*10,
                           ls="steps-mid",lw=2.0,color='navy')


ax1.legend([figura_mGe1,figura_mBGO1,figura_mCsI1],
           [r"Ge$\times{20}$",r"BGO$\times{10}$",
            r"CsI$\times{10}$"],
           fontsize=17.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

ax2.legend([figura_mGe2,figura_mBGO2,figura_mCsI2],
           [r"Ge$\times{20}$",r"BGO$\times{10}$",
            r"CsI$\times{10}$"],
           fontsize=17.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)
ax3.legend([figura_mGe3,figura_mNaI2x2_3,figura_mNaI3x3_3],
           [r"Ge$\times{20}$",
            r"NaI($2''\times2''$)$\times{10}$ ",
            r"NaI($3''\times3''$)$\times{10}$"],
           fontsize=17.5,bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)
ax4.legend([figura_mGe4,figura_mNaI2x2_4,figura_mNaI3x3_4],
           [r"Ge$\times{20}$",
            r"NaI($2''\times2''$)$\times{15}$",
            r"NaI($3''\times3''$)$\times{10}$"],
           fontsize=17.5, bbox_to_anchor=(0., 0.89, 1., .102),
           loc=1, ncol=1,fancybox=True,edgecolor='black',
           borderaxespad=0.2)

plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax2.get_xticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax3.get_xticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax3.get_yticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax4.get_xticklabels(), rotation='horizontal', fontsize=20)
plt.setp(ax4.get_yticklabels(), rotation='horizontal', fontsize=20)

f.text(0.02, 0.55, r"\textbf{cuentas $/$ min}", fontsize=21, ha='center', va='center', rotation='vertical')
f.text(0.52, 0.03, r"\textbf{E$_\gamma$(keV)}", fontsize=21, ha='center', va='center')

xmin0=195
xmax0=1600

xmin1=530
xmax1=800

ax1.set_xlim(xmin0,xmax0)
ax2.set_xlim(xmin1,xmax1)
ax3.set_xlim(xmin0,xmax0)
ax4.set_xlim(xmin1,xmax1)


ax1.set_ylim(0,120)
ax2.set_ylim(0,50)
ax3.set_ylim(0,70)
ax4.set_ylim(0,25)


space1y=50
space2y=10

ax1.set_yticks(range(int(0)+space1y,int(280),50))
ax2.set_yticks(range(int(0)+space2y,int(100),20))
ax3.set_yticks(range(int(0),int(310)+space2y,50))
ax4.set_yticks(range(int(0),int(210),50))

space1x=210
space2x=65

#ax1.set_xticks([1361,1461,1561,1661])#range(int(xmin0),int(xmax0),space2x))
ax2.set_xticks([550,583,609,650,700,750,800])
#ax3.set_xticks([1350,1461,1550,1650])
ax4.set_xticks([550,583,609,650,700,750,800])


#ax4.set_xticks(range(int(xmin1),int(xmax1),space1x))
f.set_size_inches(14.5, 7.5, forward=True)
f.subplots_adjust(hspace=0)
f.savefig('Multiplot2_m.pdf')
f.show()
















