import sys
sys.path.append('../../')
import numpy as np
import matplotlib.pyplot as plt
import spectra as sp
import calibration as cl
import roi as Eroi

U_BGO2x2,Th_BGO2x2,K_BGO2x2=[],[],[]

m_RGU=(0.535,0.001)
m_RGTh=(0.536,0.001)
m_RGK=(0.556,0.001)

Na=6.022*(10**23)

#Co60_regions=[cl.roi_cal(720,1173.22,822),
Co60_regions=[cl.roi_cal(348,1173.2,383),
    #cl.roi_cal(346,[1173.22,1332.49],429,'Double_Gauss_Rect'),
    #cl.roi_cal(826,1332.49,935),
              cl.roi_cal(390,1332.49,430),
              cl.roi_cal(720,2505.71,820)]
    

Na22_regions=[cl.roi_cal(125,511,195),
              cl.roi_cal(350,1274.53,435),
              cl.roi_cal(500,1785.53,600)]

Cs137_regions=[cl.roi_cal(180,661.65,240)]

Cd109_regions=[cl.roi_cal(20,88.033,45)]

Co60_rois=cl.rois(Co60_regions)
Cs137_rois=cl.rois(Cs137_regions)
Na22_rois=cl.rois(Na22_regions)
Cd109_rois=cl.rois(Cd109_regions)
rois_set=[Co60_rois,Cs137_rois,Na22_rois,Cd109_rois]#conjunto de rois
#rois_set=[Co60_rois,Cs137_rois,Na22_rois]
#rois_set=[Co60_rois]
cal=cl.calibration(rois_set)

path='../../Data/BGO/CNF/'
Spre=['Cal_Co','Cal_Cs','Cal_Na','Cal_Cd']
#Spre=['Cal_Co','Cal_Cs','Cal_Na']
#Spre=['Cal_Co']
filenames_list,calrects=[],[]

for count in range(8):
#for count in range(2):
    l=[]
    for fn in Spre:
        l.append(fn+str(1+count)+'.CNF')
        #l.append(fn+str(8+count)+'.CNF')
        #print(fn+str(1+count)+'.CNF')
    filenames_list.append(l)
    del(l)

# fig=plt.figure()
# ax2=fig.add_subplot(111)

# fig=plt.figure()
# ax=fig.add_subplot(111)

# fig=plt.figure()
# ax5=fig.add_subplot(111)

for filenames in filenames_list:
    for index,filename in enumerate(filenames):
        s=sp.spectra(path+filename)
        cal.rois_set[index].set_spectrum(s)     

    cal.cal()
    calrects.append(cal.popt)
    
    # ax2.plot(range(1047),
    #         cal.rect(range(1047),
    #                  cal.popt[0],
    #                  cal.popt[1]),
    #          ls='-')
    # ax2.plot(cal.CalPoints,
    #          cal.Energy,
    #          'o')

    # ax2.errorbar(cal.CalPoints,
    #          cal.Energy,
    #          xerr=cal.sigma,
    #          marker='o',
    #          ls = 'none',
    #          color=(0,0,0),
    #          lw = 2)

    for index,Rois in enumerate(rois_set):
        # ax.plot(Rois.regions[0].spectrum.channels,
        #         Rois.regions[0].spectrum.counts,
        #         ls='steps-mid',
        #         label=filenames[index])
        Rois.regions[0].spectrum.set_cal(cal.a_0,cal.a_1)#,cal.a_2)
        # ax5.plot(Rois.regions[0].spectrum.cal_energy,
        #          Rois.regions[0].spectrum.counts,
        #          ls='steps-mid',
        #          label=filenames[index])
        
        for region in Rois.regions:
            x=np.arange(region.Initial,region.Final,0.1)
#             ax.plot(x,region.Gaussrect(x, region.popt[0],region.popt[1],region.popt[2],
#                                        region.popt[3],region.popt[4]))

#     ax.legend()
#     ax5.legend()
    
# fig.show()
#plt.show()

measure=['PatronK.CNF','PatronTh.CNF','PatronU.CNF','CHUCURI.CNF','Fondo9h.CNF']
CalMeasureIndex=[0,1,2,3,6]
measureFactors=[1,1,1,1,1]
calprom=[]

for i in range(len(calrects)-1):
    a0_p=(calrects[i+1][0]+calrects[i][0])/2.0
    a1_p=(calrects[i+1][1]+calrects[i][1])/2.0
    #a2_p=(calrects[i+1][2]+calrects[i][2])/2.0
    calprom.append([a0_p,a1_p])
#-----------------------------------    
fig=plt.figure()
ax3=fig.add_subplot(111)
measureIndex=2    
filename=measure[measureIndex]
Mspectra=[]
SubSpectraList=[]

Eb=10.0
fondoSP=sp.spectra(path+'Fondo9h.CNF')
fondoSP.set_cal(calprom[6][0],
                calprom[6][1])
fondoSP.rebining(Eb)

for measureIndex,filename in enumerate(measure):
    measureSP=sp.spectra(path+filename)
        
    measureSP.set_cal(calprom[CalMeasureIndex[measureIndex]][0],
                      calprom[CalMeasureIndex[measureIndex]][1])
    measureSP.rebining(Eb)
    subSP=measureSP-fondoSP
    Mspectra.append(measureSP)
    SubSpectraList.append(subSP)
    ax3.plot(measureSP.cal_energy,
             (measureSP.counts/measureSP.LifeTime)*measureFactors[measureIndex],
             ls='steps-mid',
             label=filename)
    ax3.plot(subSP.cal_energy,
             (subSP.counts/subSP.LifeTime)*measureFactors[measureIndex],
             ls='steps-mid',
             label=filename+'-f4')
    ax3.legend()
SubSpectraList.pop(-1)
SubSpectraList.append(fondoSP)
fig.show()
plt.show()
#-------------------------------------
PU_regions=[Eroi.roi(1610,1764.49,1980)]
PTh_regions=[Eroi.roi(2454,2614.51,2815)]
PK_regions=[Eroi.roi(1311,1460.82,1620)]
Guayna_regions=[Eroi.roi(1610,1764.49,1980),
                Eroi.roi(2454,2614.51,2815),
                Eroi.roi(1311,1460.82,1620)]

fondo_regions=[Eroi.roi(1610,1764.49,1980),
               Eroi.roi(2454,2614.51,2815),
               Eroi.roi(1311,1460.82,1620)]

U_rois=cl.rois(PU_regions)
Th_rois=cl.rois(PTh_regions)
PK_rois=cl.rois(PK_regions)
Guayna_rois=cl.rois(Guayna_regions)
fondo_rois=cl.rois(fondo_regions)

#frois_set=[fondo_rois]

Mrois_set=[PK_rois,Th_rois,U_rois,Guayna_rois,fondo_rois]

fig=plt.figure()
ax4=fig.add_subplot(111)
intensity_values=[]
DiscreteIntensityValues=[]
intensity_fvalues=[]
DiscreteIntensityfValues=[]
Total_values=[]
Total_values_ConF=[]
for index,rois in enumerate(Mrois_set):
    #rois.set_spectrum(Mspectra[index])     
    rois.set_spectrum(SubSpectraList[index])#lista de espectros restados
    # ax4.plot(Mspectra[index].cal_energy,
    #         (Mspectra[index].counts)*measureFactors[index],
    #         ls='steps-mid',
    #         label=measure[index])
    ax4.plot(SubSpectraList[index].cal_energy,
             (SubSpectraList[index].counts/SubSpectraList[index].LifeTime)*measureFactors[index],
             ls='steps-mid',
             label=measure[index]+'-f4')
    values=[]
    dValues=[]
    value=[]
    for region in rois.regions:
        values.append([region.inten,region.di])
        dValues.append([region.discreteIntensity,region.discreteInteSigma])
        value.append([region.discreteTotalInt])
        x=np.arange(region.Initial,region.Final,0.1)
        ax4.plot(SubSpectraList[index].ch2Energy(x),
                 (region.Gaussrect(x,
                                   region.popt[0],
                                   region.popt[1],
                                   region.popt[2],
                                   region.popt[3],
                                   region.popt[4])/SubSpectraList[index].LifeTime)*measureFactors[index])
    Total_values.append(value)
    intensity_values.append(values)
    DiscreteIntensityValues.append(dValues)
    ax4.legend()
fig.show()
plt.show()
#cal.rois_set[index].set_spectrum(s)

def concentracion(conP,IntensidadM,IntensidadP):
    C=conP[0]*float(IntensidadM[0])/float(IntensidadP[0])
    a=(conP[1]/conP[0])
    c=(float(IntensidadM[1])/float(IntensidadM[0]))
    e=(float(IntensidadP[1])/float(IntensidadP[0]))
    #print('a c e',a,c,e)
    return (C,C*np.sqrt(a**2+c**2+e**2))

def Actividad(Concentracion, ProbDeca, masa, f):
    return float(Concentracion*ProbDeca*6.022*(10**23)*f/masa)

def eB(concentracionP,masaP,ProbDeca,masa,IP):
    return float((ProbDeca*concentracionP*Na*masaP)/(masa*IP))

def MDA(M,tb,B,eP): #B es una rata de conteo de fondo
    Ld=(1.645)**2+2*(1.645)*np.sqrt(2*B)
    return Ld/(M*tb)*eP

#===============================================================================    
#============================Potasio_===========================================
#===============================================================================    

ProbK, masaK, fK, dfK=np.log(2)/(31536000*1.248*(1000000000)), 0.040,0.0117,0.0001
dProbK=ProbK*np.sqrt((9*(31536000)/(31536000*1.248*(1000000000)))**2)
conPK=(448000*0.0117,3000*0.0117)
masaP=0.5#masa del patron en kg 
#conPK=(52.47, 0.3)
IntPK_Guayana=intensity_values[3][2]
dIntPK_Guayana=DiscreteIntensityValues[3][2]
cuentas_GK=dIntPK_Guayana[0]*SubSpectraList[3].LifeTime
cuentas_FondoK=DiscreteIntensityValues[4][2][0]
IntPK=intensity_values[0][0]
dIntPK=DiscreteIntensityValues[0][0]
#print('Potasio=====================================')
GuayanaPK_c=concentracion(conPK,IntPK_Guayana,IntPK)
#print(GuayanaPK_c)
#print('PPK:',conPK[1]/conPK[0]*100,'GPK:',GuayanaPK_c[1]/GuayanaPK_c[0]*100)
#print('discrete====================================')
dGuayanaPK_c=concentracion(conPK,dIntPK_Guayana,dIntPK)
#print(dGuayanaPK_c)
#print('PPK:',conPK[1]/conPK[0]*100,'GPK:',dGuayanaPK_c[1]/dGuayanaPK_c[0]*100)

ActividadK=Actividad(conPK[0],ProbK,masaK,fK)/1000000
ActividadMK=Actividad(dGuayanaPK_c[0],ProbK,masaK,fK)/1000000
dActividadMK=ActividadMK*np.sqrt((dGuayanaPK_c[1]/dGuayanaPK_c[0])**2+(dProbK/ProbK)**2+(dfK/fK)**2)
ddGuayanaPK_c=dGuayanaPK_c[0]*np.sqrt((dGuayanaPK_c[1]/dGuayanaPK_c[0])**2+(dIntPK_Guayana[1]/dIntPK_Guayana[0])**2+(m_RGK[1]/m_RGK[0])**2+(0.001/0.544)**2+(dIntPK[1]/dIntPK[0])**2)

# eBK=eB(conPK[0],masaP,ProbK,masaK,dIntPK[0])/1000000

# Lc_K=(1.645)*np.sqrt(2*cuentas_FondoK)#cuentas_Ver_Gilmore
# Ld_K=2.71+2*Lc_K#(cuenats)

# MDA_Ka=MDA(0.5,fondoSP.LifeTime,cuentas_FondoK,eBK)
# MDA_K=(1.645**2+2*1.645*np.sqrt(2*Ld_K)*eBK)/(0.5*fondoSP.LifeTime)

#C_MinK=concentracion(conPK,np.array(Ld_K)/fondoSP.LifeTime,dIntPK)

#Potasio=print('Actividad_Muestra= ',ActividadK,'dActividad= ',dActividadMK )

#===============================================================================    
#===============================Torio===========================================
#=============================================================================== 

ProbTh, masaTh, fTh, dfTh=np.log(2)/(31536000*1.248*(10000000000)),0.232,1,0
dProbTh=ProbTh*np.sqrt((9*(31536000)/(31536000*1.248*(1000000000)))**2)
conTh,masaP=(800,16),0.5
IntTh_Guayana=intensity_values[3][1]
dIntTh_Guayana=DiscreteIntensityValues[3][1]
cuentas_GTh=dIntTh_Guayana[0]*SubSpectraList[3].LifeTime
cuentas_FondoTh=intensity_values[4][1][0]*fondoSP.LifeTime
IntTh=intensity_values[1][0]
dIntTh=DiscreteIntensityValues[1][0]
#print('Torio========================================')
GuayanaTh_c=concentracion(conTh,IntTh_Guayana,IntTh)
#print(GuayanaTh_c)
#print('PTh:',conTh[1]/conTh[0]*100,'GTh:',GuayanaTh_c[1]/GuayanaTh_c[0]*100)       
#print('discrete====================================')
dGuayanaTh_c=concentracion(conTh,dIntTh_Guayana,dIntTh)
#print(dGuayanaTh_c)
#print('PTh:',conTh[1]/conTh[0]*100,'GTh:',dGuayanaTh_c[1]/dGuayanaTh_c[0]*100)

ActividadTh=Actividad(conTh[0],ProbTh,masaTh,fTh)/1000000
ActividadMTh=Actividad(dGuayanaTh_c[0],ProbTh,masaTh,fTh)/1000000
# eBTh=eB(conTh[0],masaP,ProbTh,masaTh,dIntTh[0])/1000000
# MDA_Th=(1.645**2+2*1.645*np.sqrt(2*cuentas_FondoTh)*eBTh)/(0.5*fondoSP.LifeTime)
# MDA_Tha=MDA(0.5,fondoSP.LifeTime,cuentas_FondoTh,eBTh)
# Lc_Th=(1.645)*np.sqrt(2*cuentas_FondoTh)#cuentas_Ver_Gilmore
# Ld_Th=2.71+2*Lc_Th
dActividadMTh=ActividadMTh*np.sqrt((dGuayanaTh_c[1]/dGuayanaTh_c[0])**2+(dProbTh/ProbTh)**2+(dfTh/fTh)**2)
ddGuayanaTh_c=dGuayanaTh_c[0]*np.sqrt((dGuayanaTh_c[1]/dGuayanaTh_c[0])**2+(dIntTh_Guayana[1]/dIntTh_Guayana[0])**2+(m_RGK[1]/m_RGK[0])**2+(0.001/0.544)**2+(dIntTh[1]/dIntTh[0])**2)

#===============================================================================    
#===============================Uranio==========================================
#===============================================================================

ProbU, masaU, fU, dfU=np.log(2)/(31536000*4.468*(1000000000)),0.238,0.9925,  0.001
dProbU=ProbU*np.sqrt((9*(31536000)/(31536000*1.248*(1000000000)))**2)

conU=(400,2)
IntU_Guayana=intensity_values[3][0]
dIntU_Guayana=DiscreteIntensityValues[3][0]
cuentas_GU=dIntU_Guayana[0]*SubSpectraList[3].LifeTime
cuentas_FondoU=intensity_values[4][0][0]*fondoSP.LifeTime
IntU=intensity_values[2][0]
dIntU=DiscreteIntensityValues[2][0]
#print('Uranio========================================')
GuayanaU_c=concentracion(conU,IntU_Guayana,IntU)
#print(GuayanaU_c)
#print('PU:',conU[1]/conU[0]*100,'GU:',GuayanaU_c[1]/GuayanaU_c[0]*100)
#print('discrete====================================')
dGuayanaU_c=concentracion(conU,dIntU_Guayana,dIntU)#ppm
#print(dGuayanaU_c)
#print('PU:',conU[1]/conU[0]*100,'GU:',dGuayanaU_c[1]/dGuayanaU_c[0]*100)

ActividadU=Actividad(conU[0],ProbU,masaU,fU)/1000000#Bq/kg
ActividadMU=Actividad(dGuayanaU_c[0],ProbU,masaU,fU)/1000000#Bq/kg
# eBU=eB(conU[0],masaP,ProbU,masaU,dIntU[0])/1000000#Bq/kg
# MDA_U=(1.645**2+2*1.645*np.sqrt(2*cuentas_FondoU)*eBU)/(0.5*fondoSP.LifeTime)#Bq/kg
# MDA_Ua=MDA(0.5,fondoSP.LifeTime,cuentas_FondoU,eBU)
# Lc_U=(1.645)*np.sqrt(2*cuentas_FondoU)#cuentas_Ver_Gilmore
# Ld_U=2.71+2*Lc
dActividadMU=ActividadMU*np.sqrt((dGuayanaU_c[1]/dGuayanaU_c[0])**2+(dProbU/ProbU)**2+(dfU/fU)**2)
ddGuayanaU_c=dGuayanaU_c[0]*np.sqrt((dGuayanaU_c[1]/dGuayanaU_c[0])**2+(dIntU_Guayana[1]/dIntU_Guayana[0])**2+(m_RGK[1]/m_RGK[0])**2+(0.001/0.544)**2+(dIntU[1]/dIntU[0])**2)


################################RESULTADOS##############################
K_BGO2x2,Th_BGO2x2,U_BGO2x2=[],[],[]

K_BGO2x2.append([dGuayanaPK_c[0],ddGuayanaPK_c,ActividadMK,dActividadMK])
Th_BGO2x2.append([dGuayanaTh_c[0],ddGuayanaTh_c,ActividadMTh,dActividadMTh])
U_BGO2x2.append([dGuayanaU_c[0],ddGuayanaU_c,ActividadMU,dActividadMU])
