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

fig = plt.figure()
ax=fig.add_subplot(111)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.gcf().subplots_adjust(bottom=0.14)   #esto es para la grafica!
plt.gcf().subplots_adjust(right=0.89)    #esto es para la grafica!
plt.gcf().subplots_adjust(left=0.14)     #esto es para la grafica! 
plt.gcf().subplots_adjust(top=0.86)      #esto es para la grafica!
plt.ylabel(r"\textbf{cuentas $/$ segundo}",fontsize=21)
plt.xlabel(r"\textbf{E$_\gamma$ (keV)}",fontsize=21)
plt.xticks(fontsize=20.5)
plt.yticks(fontsize=20.5)
plt.xlim(100,800)
plt.ylim(0,120)

figura1,=ax.plot(BGO.rois_set[1].regions[0].spectrum.cal_energy,
                 BGO.rois_set[1].regions[0].spectrum.counts/\
                 (BGO.rois_set[1].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0)
figura2,=ax.plot(NaI2x2.rois_set[1].regions[0].spectrum.cal_energy,
                 NaI2x2.rois_set[1].regions[0].spectrum.counts/\
                 (NaI2x2.rois_set[1].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0)
figura3,=ax.plot(NaI3x3.rois_set[1].regions[0].spectrum.cal_energy,
                 NaI3x3.rois_set[1].regions[0].spectrum.counts/\
                 (NaI3x3.rois_set[1].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0)
figura4,=ax.plot(CsI.rois_set[1].regions[0].spectrum.cal_energy,
                 CsI.rois_set[1].regions[0].spectrum.counts/\
                 (CsI.rois_set[1].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0)
figura5,=ax.plot(Ge.rois_set[0].regions[0].spectrum.cal_energy[1400:],
                 Ge.rois_set[0].regions[0].spectrum.counts[1400:]*3/\
                 (Ge.rois_set[0].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0,color='orchid')
figura6,=ax.plot(Ge.rois_set[0].regions[0].spectrum.cal_energy[:1380],
                 Ge.rois_set[0].regions[0].spectrum.counts[:1380]*2.5/\
                 (Ge.rois_set[0].regions[0].spectrum.LifeTime),
                 ls="steps-mid",lw=2.0,color='orchid')

plt.annotate(r"Retrodispersi\'on",xy=(185,13.5),xytext=(120,35),arrowprops=dict(arrowstyle="fancy,tail_width=0.1",color='k'),fontsize=15, color='k')

plt.annotate(r"Borde Compton",xy=(470,7),xytext=(400,32),arrowprops=dict(arrowstyle="fancy,tail_width=0.1", color='k'),fontsize=15, color='k')

plt.annotate("Fotopico",xy=(660,100),xytext=(478,100),arrowprops=dict(arrowstyle="fancy,tail_width=0.1",color='k'),fontsize=15, color='k')

ax.legend([figura1,figura2,figura3,figura4,figura5],
          [r"BGO ($2''\times2''$)",r"NaI ($2''\times2''$)",
           r"NaI ($3''\times3''$)",r"CsI ($2''\times2''$)",r"Ge ($40\%$)$\times 3$"],
          fontsize=17.5,bbox_to_anchor=(0., 0.90, 1., .102),
          loc='upper left', ncol=1,fancybox=True,edgecolor='black',
          borderaxespad=0.90)
fig.subplots_adjust(hspace=0)
fig.savefig('Multiplot1.pdf')
plt.show()


################################Figura2#################################
