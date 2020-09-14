#===========================IMPORTAR LIBRERIAS==============================
import sys
sys.path.append('../')
import math
from numpy import *
from scipy.optimize import curve_fit
from pylab import *
from matplotlib import *
from matplotlib.pyplot import legend
#import Multiplot_P_BGO as BGO

#==============================FUNCIONES====================================

#-----------------------------Gaussiana-------------------------------------
def Gaussiana(x1,A,u,o):
    return A*(exp((-(((u - x1)/o)**2))/2))
#--------------------------Gaussiana y Recta--------------------------------
def func1(x1,A,u,o,c,d,e):
    return A*(exp((-(((u - x1)/o)**2))/2)) + c + d*(x1 - e)
#-------------------------2 Gaussianas y Recta-----------------------------
def func2(x1,A1,u1,o1,c,d,e,A2,u2,o2):
    return A1*(exp((-(((u1 - x1)/o1)**2))/2)) + c + d*(x1 - e) + A2*(exp((-(((u2 - x1)/o2)**2))/2))
#---------------------2 Gaussianas y Exponencial Neg------------------------
def func2F(x1,A1,u1,o1,c,d,e,j,A2,u2,o2):
    return A1*(exp((-(((u1 - x1)/o1)**2))/2)) + c/(exp((x1-e)/d)+1)+j  + A2*(exp((-(((u2 - x1)/o2)**2))/2))
#---------------------------------------------------------------------------
def canalenergia(x1,c,d,e):
    return  c + d*x1 + e*x1**2
#---------------------------------------------------------------------------
def Comvierte_A_Energia(a,b,x):
    return  a + b*x
#---------------------------------------------------------------------------
def DesComvierte_A_Energia(a,b,x):
    return  (x-a)/b
#---------------------------------------------------------------------------
def integralgaussiana(A,o):
    return sqrt(2*pi)*A*o

#==========================PARAMETROS DE ENTRADA============================

def Piniciales(a,c): #a es el archivo y c es el canal donde se encuentra el pico 
    x=a[:,0]
    return [a[c-30:c+30,1].max(),x[a[c-10:c+10,1].argmax() + c-10], 2.0, a[c-30,1], (a[c-30,1]-a[c+30-((c-3+1)/0.11),1])/(a[c-30,0]-a[c+30-((c-3+1)/0.11),0]),x[a[c-30:c+30,1].argmax() + c-30]] #Retorna una lista [] con los parametros iniciales
#--------------------------------------------------------------------------
def Piniciales2(a,c): #a es el archivo y c es el canal donde se encuentra el pico 
    x=a[:,0]
    return [a[int(c-30):int(c+30),1].max(),a[int(c-30):int(c+30),1].argmax()+c-30,30, a[int(c-30),1], (a[int(c-30),1]-a[int(c+30)-int(c-30+1),1])/(a[int(c-30),0]-a[int(c+30-((c-30+1))),0]),x[a[int(c-30):int(c+30),1].argmax() + c-30]]
#--------------------------------------------------------------------------
def Piniciales22(a,c): #a es el archivo y c es el canal donde se encuentra el pico 
    x=a[:,0]
    return [a[c-10:c+10,1].max(),c,10, a[c-10,1], (a[c-10,1]-a[c+10-(c-10+1),1])/(a[c-10,0]-a[c+10-((c-10+1)),0]),x[a[c-10:c+10,1].argmax() + c-10]]
#--------------------------------------------------------------------------
def Piniciales222(a,c): #a es el archivo y c es el canal donde se encuentra el pico 
    x=a[:,0]
    return [a[c-30:c+30,1].max(),c,30.0, 100.0,20.0,1600.0,1.0]

#===========================CALIBRACION DE PICOS============================

#--------------------------Un Pico en el Espectro---------------------------
def IntegralSencillo(C,archivo):

    XR = archivo[int((C-100.0)/1.0):int((C+100)/1.0),0] 
    YR = archivo[int((C-100.0)/1.0):int((C+100)/1.0),1]

    parametros = Piniciales2(archivo,C)

    # ylabel('Cuentas (min)', fontsize=18.5)
    # xlabel('Energia (keV)', fontsize=18.5)

    # xlim(C-100,C+100)                    
    # ylim(0,array(YR).max()*1.15)     
    # gcf().subplots_adjust(bottom=0.12)   #esto es para la grafica!
    # gcf().subplots_adjust(right=0.89)    #esto es para la grafica! 
    # gcf().subplots_adjust(left=0.14)     #esto es para la grafica!
    # gcf().subplots_adjust(top=0.96)      #esto es para la grafica!

    
    popt, pcov = curve_fit(func1,XR,YR,parametros) # Ajuste Gaussianas

    # plot(XR,YR,ls='steps-mid',lw=1, label='Espectro')    #Espectro
    # plot(XR,func1(XR,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]),ls='-',lw=1.5,color='r',label='Ajuste')
    # plot(XR,Gaussiana(XR,popt[0],popt[1],popt[2]),ls='-',lw=1.5, color='k',label='Gaussiana a 870 keV')
    # xticks(fontsize=18.5)
    # yticks(fontsize=18.5)
    #legend()
    #show()
    #print"Centroide-u = %f" % (popt[1])
    #print"Sigma-o = %f" % (popt[2])
    return popt[1]
#--------------------------Un Pico en el Espectro---------------------------
def IntegralSencilloCd(C,archivo):

    XR = archivo[int((C-10.0)/1.0):int((C+10)/1.0),0] 
    YR = archivo[int((C-10.0)/1.0):int((C+10)/1.0),1]

    parametros = Piniciales2(archivo,C)

    # ylabel('Cuentas (min)', fontsize=18.5)
    # xlabel('Energia (keV)', fontsize=18.5)

    # xlim(C-100,C+100)                    
    # ylim(0,array(YR).max()*1.15)     
    # gcf().subplots_adjust(bottom=0.12)   #esto es para la grafica!
    # gcf().subplots_adjust(right=0.89)    #esto es para la grafica! 
    # gcf().subplots_adjust(left=0.14)     #esto es para la grafica!
    # gcf().subplots_adjust(top=0.96)  
    #esto es para la grafica!

    popt, pcov = curve_fit(func1,XR,YR,parametros) # Ajuste Gaussianas
    # plot(XR,YR,ls='steps-mid',lw=1, label='Espectro')    #Espectro
    # plot(XR,func1(XR,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5]),ls='-',lw=1.5,color='r',label='Ajuste')
    # plot(XR,Gaussiana(XR,popt[0],popt[1],popt[2]),ls='-',lw=1.5, color='k',label='Gaussiana a 870 keV')
    # xticks(fontsize=18.5)
    # yticks(fontsize=18.5)
    #legend()
    #show()
    #print"Centroide-u = %f" % (popt[1])
    #print"Sigma-o = %f" % (popt[2])
    return popt[1]
#------------------------Picos Dobles Fondo lineal-----------------------------
def IntegralDoble2(C1,C2,archivo):    #con fondo lineal

    XR = archivo[int((C1-90.0)/1.0):int((C2+90)/1.0),0] 
    YR = archivo[int((C1-90.0)/1.0):int((C2+90)/1.0),1]

    parametros1 = Piniciales22(archivo,C1) 
    parametros2 = Piniciales22(archivo,C2)
    parametrosT = parametros1 + parametros2

    del parametrosT[9]    #Elimina parametros 'repetidos del fondo'
    del parametrosT[9]    #Elimina parametros 'repetidos del fondo'
    del parametrosT[9]    #Elimina parametros 'repetidos del fondo'

    # ylabel('Cuentas (min)', fontsize=18.5)
    # xlabel('Energy (keV)', fontsize=18.5)

    # xlim(C1-100,C2+100)
    # ylim(0,array(YR).max()*1.15)
    # gcf().subplots_adjust(bottom=0.12)   #esto es para la grafica!
    # gcf().subplots_adjust(right=0.89)    #esto es para la grafica!
    # gcf().subplots_adjust(left=0.14)     #esto es para la grafica! 
    # gcf().subplots_adjust(top=0.96)      #esto es para la grafica! 

    popt, pcov = curve_fit(func2,XR,YR,parametrosT) # Ajuste Gaussianas

    # plot(XR,YR,ls='steps-mid',lw=1.0, label='Espectro')    #Espectro
    # plot(XR,func2(XR,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6],popt[7],popt[8]),lw=1.5,color='r',label='Ajuste')
    # plot(XR,Gaussiana(XR,popt[0],popt[1],popt[2]),lw=2.5,color='k',label='Gaussiana a 1117 keV')
    # plot(XR,Gaussiana(XR,popt[6],popt[7],popt[8]),lw=2.5,color='c',label='Gaussiana a 1332 keV')

    # xticks(fontsize=18.5)
    # yticks(fontsize=18.5 )
    #legend()
    #show()
    #print"Centroide(G1,G2) = %f , %f" % (popt[1],popt[7])
    #print"Sigma(o1,o2) = %f , %f" % (popt[2],popt[8])

    return [popt[1],popt[7]]
#----------------------Picos dobles Fondo de Fermi-----------------------------
def IntegralDoble(C1,C2,archivo): #con fondo de Fermi

    XR = archivo[int((C1-90)/1):int((C2+90)/1),0] 
    YR = archivo[int((C1-90)/1):int((C2+90)/1),1]

    parametros1 = Piniciales222(archivo,C1)
    parametros2 = Piniciales222(archivo,C2)
    parametrosT = parametros1 + parametros2
    
    del parametrosT[9]     #Elimina parametros 'repetidos del fondo'
    del parametrosT[9]     #Elimina parametros 'repetidos del fondo'
    del parametrosT[9]     #Elimina parametros 'repetidos del fondo'
    del parametrosT[9]     #Elimina parametros 'repetidos del fondo'

    # ylabel('Cuentas (min)', fontsize=18.5)
    # xlabel('Energia (keV)', fontsize=18.5)

    # xlim(C1-90,C2+90)
    # ylim(0,array(YR).max()*1.15)         
    # gcf().subplots_adjust(bottom=0.12)    #esto es para la grafica  
    # gcf().subplots_adjust(right=0.89)     #esto es para la grafica
    # gcf().subplots_adjust(left=0.14)      #esto es para la grafica
    # gcf().subplots_adjust(top=0.96)  
    #esto es para la grafica

    popt, pcov = curve_fit(func2F,XR,YR,parametrosT) # Ajuste Gaussianas

    # plot(XR,YR,ls='steps-mid',lw=1.0)      #Espectro
    # plot(XR,func2F(XR,popt[0],popt[1],popt[2],popt[3],popt[4],popt[5],popt[6],popt[7],popt[8],popt[9]),lw=1.5,color='r',label='Ajuste')
    # plot(XR,Gaussiana(XR,popt[0],popt[1],popt[2]),lw=1.5,color='k',label='Gaussiana a 1117 keV')
    # plot(XR,Gaussiana(XR,popt[7],popt[8],popt[9]),lw=2.5,color='c',label='Gaussiana a 1332 keV')

    # xticks(fontsize=18.5)
    # yticks(fontsize=18.5)
    #legend ()
    #show()
    #print"Centroide(G1,G2) = %f, %f " % (popt[1],popt[8])
    #print"Sigma(o1,o2) = %f, %f " % (popt[2],popt[9])
    return [popt[1],popt[8]]

#================Archivos necesarios para las Gaussianas===============================
path='../Data/NaI3x3/mca/data/'
name='Cal_'
ext='.xy'
#----------------------------Archivos--Fondo------------------------------------------
Fondo = genfromtxt(path+'Fondo14h.xy') #con antes y despues se promedia u y o
#Antes:
Cd109F_a = genfromtxt(path+name+'Cd1'+ext)
Na22F_a = genfromtxt(path+name+'Na1'+ext)
Co60F_a = genfromtxt(path+name+'Co1'+ext)
Cs137F_a = genfromtxt(path+name+'Cs1'+ext)
#Despues:
Cd109F_d = genfromtxt(path+name+'Cd2'+ext)
Na22F_d =  genfromtxt(path+name+'Na2'+ext)
Co60F_d =  genfromtxt(path+name+'Co2'+ext)
Cs137F_d =  genfromtxt(path+name+'Cs2'+ext)

#----------------------------Archivos--PatronU------------------------------------------
PatronU = genfromtxt(path+'Patron_U.xy') #con antes y despues se promedia u y o
#Antes:
Cd109U_a = genfromtxt(path+name+'Cd2'+ext)
Na22U_a = genfromtxt(path+name+'Na2'+ext)
Co60U_a = genfromtxt(path+name+'Co2'+ext)
Cs137U_a = genfromtxt(path+name+'Cs2'+ext)
#Despues:
Cd109U_d = genfromtxt(path+name+'Cd3'+ext)
Na22U_d =  genfromtxt(path+name+'Na3'+ext)
Co60U_d =  genfromtxt(path+name+'Co3'+ext)
Cs137U_d =  genfromtxt(path+name+'Cs3'+ext)

#----------------------------Archivos--PatronTh------------------------------------------
PatronTh = genfromtxt(path +'Patron_Th.xy') #con antes y despues se promedia u y o
#Antes:
Cd109Th_a = genfromtxt(path+name+'Cd2'+ext)
Na22Th_a = genfromtxt(path+name+'Na2'+ext)
Co60Th_a = genfromtxt(path+name+'Co2'+ext)
Cs137Th_a = genfromtxt(path+name+'Cs2'+ext)
#Despues:
Cd109Th_d = genfromtxt(path+name+'Cd3'+ext)
Na22Th_d = genfromtxt(path+name+'Na3'+ext)
Co60Th_d = genfromtxt(path+name+'Co3'+ext)
Cs137Th_d = genfromtxt(path+name+'Cs3'+ext)

#----------------------------Archivos--PatronK------------------------------------------
PatronK = genfromtxt(path+'Patron_K.xy') #con antes y despues se promedia u y o
#Antes:
Cd109K_a = genfromtxt(path+name+'Cd2'+ext)
Na22K_a = genfromtxt(path+name+'Na2'+ext)
Co60K_a = genfromtxt(path+name+'Co2'+ext)
Cs137K_a = genfromtxt(path+name+'Cs2'+ext)
#Despues:
Cd109K_d = genfromtxt(path+name+'Cd3'+ext)
Na22K_d = genfromtxt(path+name+'Na3'+ext)
Co60K_d = genfromtxt(path+name+'Co3'+ext)
Cs137K_d = genfromtxt(path+name+'Cs3'+ext)

#----------------------------Archivos--Muestra------------------------------------------
Guayana=genfromtxt(path+'Guayana12h.xy') #con antes y despues se promedia u y o
#Antes:
Cd109G_a = genfromtxt(path+name+'Cd3'+ext)
Na22G_a = genfromtxt(path+name+'Na3'+ext)
Co60G_a = genfromtxt(path+name+'Co3'+ext)
Cs137G_a = genfromtxt(path+name+'Cs3'+ext)
#Despues:
Cd109G_d = genfromtxt(path+name+'Cd4'+ext)
Na22G_d = genfromtxt(path+name+'Na4'+ext)
Co60G_d = genfromtxt(path+name+'Co4'+ext)
Cs137G_d = genfromtxt(path+name+'Cs4'+ext)

#==============================Picos, Archivos=========================================

#-------------------------------FONDO-----------------------------------------------
# antes Fondo------------
CanalCdF_a = IntegralSencilloCd(73,Cd109F_a) #(canal,archivo)
CanalCsF_a = IntegralSencillo(445,Cs137F_a)  
CanalNa1F_a = IntegralSencillo(347,Na22F_a)  
CanalNa2F_a = IntegralSencillo(837,Na22F_a) 
Canal1CoF_a = IntegralDoble2(771,879,Co60F_a)[0]
Canal2CoF_a = IntegralDoble2(771,879,Co60F_a)[1]
SumaFNa_a = IntegralSencillo(1302,Na22U_a)
SumaFCo_a = IntegralSencillo(1822,Co60U_a)
# despues Fondo------------
CanalCdF_d = IntegralSencilloCd(71,Cd109F_d)  #(canaL,archivo)
CanalCsF_d = IntegralSencillo(442,Cs137F_d)  
CanalNa1F_d = IntegralSencillo(345,Na22F_d)  
CanalNa2F_d = IntegralSencillo(835,Na22F_d)
Canal1CoF_d = IntegralDoble2(772,873,Co60F_d)[0]
Canal2CoF_d = IntegralDoble2(772,873,Co60F_d)[1]
SumaFNa_d = IntegralSencillo(1295,Na22U_d)
SumaFCo_d = IntegralSencillo(1814,Co60U_d)

CanalF_a = [CanalCdF_a,CanalNa1F_a,CanalCsF_a,Canal1CoF_a,CanalNa2F_a,Canal2CoF_a,SumaFNa_a,SumaFCo_a]
EnergiaF_a = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

CanalF_d = [CanalCdF_d,CanalNa1F_d,CanalCsF_d,Canal1CoF_d,CanalNa2F_d,Canal2CoF_d,SumaFNa_d,SumaFCo_d]
EnergiaF_d = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

#---------------------------------URANIO-----------------------------------------------
# antes U---------------
CanalCdU_a = IntegralSencilloCd(70,Cd109U_a) #(canal,archivo)
CanalCsU_a = IntegralSencillo(485,Cs137U_a)   
CanalNa1U_a = IntegralSencillo(378,Na22U_a)  
CanalNa2U_a = IntegralSencillo(913,Na22U_a)
Canal1CoU_a = IntegralDoble2(846,958,Co60U_a)[0]
Canal2CoU_a = IntegralDoble2(846,958,Co60U_a)[1]
SumaUNa_a = IntegralSencillo(1294,Na22Th_a)
SumaUCo_a = IntegralSencillo(1812,Co60Th_a)
# despues U-------------
CanalCdU_d = IntegralSencilloCd(70,Cd109U_d) #(canal,archivo)
CanalCsU_d = IntegralSencillo(485,Cs137U_d)  
CanalNa1U_d = IntegralSencillo(376,Na22U_d) 
CanalNa2U_d = IntegralSencillo(914,Na22U_d) 
Canal1CoU_d = IntegralDoble2(845,959,Co60U_d)[0]
Canal2CoU_d = IntegralDoble2(845,959,Co60U_d)[1]
SumaUNa_d = IntegralSencillo(1298,Na22Th_d)
SumaUCo_d = IntegralSencillo(1818,Co60Th_d)

CanalU_a = [CanalCdU_a,CanalNa1U_a,CanalCsU_a,Canal1CoU_a,CanalNa2U_a,Canal2CoU_a,SumaUNa_a,SumaUCo_a]
EnergiaU_a = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

CanalU_d = [CanalCdU_d,CanalNa1U_d,CanalCsU_d,Canal1CoU_d,CanalNa2U_d,Canal2CoU_d,SumaUNa_d,SumaUCo_d]
EnergiaU_d = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

#---------------------------------THORIO-----------------------------------------------
# antes Th--------------
CanalCdTh_a = IntegralSencilloCd(70,Cd109Th_a) #(canal,archivo)
CanalCsTh_a = IntegralSencillo(485,Cs137Th_a)   
CanalNa1Th_a = IntegralSencillo(378,Na22Th_a)  
CanalNa2Th_a = IntegralSencillo(913,Na22Th_a)
Canal1CoTh_a = IntegralDoble2(846,958,Co60Th_a)[0]
Canal2CoTh_a = IntegralDoble2(846,958,Co60Th_a)[1]
SumaThNa_a = IntegralSencillo(1294,Na22Th_a)
SumaThCo_a = IntegralSencillo(1812,Co60Th_a)
# despues Th-------------
CanalCdTh_d = IntegralSencilloCd(70,Cd109Th_d) #(canal,archivo)
CanalCsTh_d = IntegralSencillo(485,Cs137Th_d)  
CanalNa1Th_d = IntegralSencillo(376,Na22Th_d) 
CanalNa2Th_d = IntegralSencillo(914,Na22Th_d) 
Canal1CoTh_d = IntegralDoble2(845,959,Co60Th_d)[0]
Canal2CoTh_d = IntegralDoble2(845,959,Co60Th_d)[1]
SumaThNa_d = IntegralSencillo(1298,Na22Th_d)
SumaThCo_d = IntegralSencillo(1818,Co60Th_d)

CanalTh_a = [CanalCdTh_a,CanalNa1Th_a,CanalCsTh_a,Canal1CoTh_a,CanalNa2Th_a,Canal2CoTh_a,SumaThNa_a,SumaThCo_a]
EnergiaTh_a = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

CanalTh_d = [CanalCdTh_d,CanalNa1Th_d,CanalCsTh_d,Canal1CoTh_d,CanalNa2Th_d,Canal2CoTh_d,SumaThNa_d,SumaThCo_d]
EnergiaTh_d = [88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

#---------------------------------POTASIO-----------------------------------------------
# antes K------------
CanalCdK_a = IntegralSencilloCd(70,Cd109K_a) #(canal,archivo)
CanalCsK_a = IntegralSencillo(485,Cs137K_a)   
CanalNa1K_a = IntegralSencillo(378,Na22K_a)  
CanalNa2K_a = IntegralSencillo(913,Na22K_a)
Canal1CoK_a = IntegralDoble2(846,958,Co60K_a)[0]
Canal2CoK_a = IntegralDoble2(846,958,Co60K_a)[1]
SumaKNa_a = IntegralSencillo(1294,Na22K_a)
SumaKCo_a = IntegralSencillo(1812,Co60K_a)
# despues K-------------
CanalCdK_d = IntegralSencilloCd(70,Cd109K_d) #(canal,archivo)
CanalCsK_d = IntegralSencillo(485,Cs137K_d)  
CanalNa1K_d = IntegralSencillo(376,Na22K_d) 
CanalNa2K_d = IntegralSencillo(914,Na22K_d) 
Canal1CoK_d = IntegralDoble2(845,959,Co60K_d)[0]
Canal2CoK_d = IntegralDoble2(845,959,Co60K_d)[1]
SumaKNa_d = IntegralSencillo(1298,Na22K_d)
SumaKCo_d = IntegralSencillo(1818,Co60K_d)


CanalK_a=[CanalCdK_a,CanalNa1K_a,CanalCsK_a,Canal1CoK_a,CanalNa2K_a,Canal2CoK_a,SumaKNa_a,SumaKCo_a]
EnergiaK_a=[88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

CanalK_d=[CanalCdK_d,CanalNa1K_d,CanalCsK_d,Canal1CoK_d,CanalNa2K_d,Canal2CoK_d,SumaKNa_d,SumaKCo_d]
EnergiaK_d=[88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]

#--------------------------------GUAYANA-----------------------------------------------
# antes Guayana-------------

CanalCdG_a = IntegralSencilloCd(70,Cd109G_d) #(canal,archivo)
CanalCsG_a = IntegralSencillo(485,Cs137G_d)  
CanalNa1G_a = IntegralSencillo(376,Na22G_d) 
CanalNa2G_a = IntegralSencillo(914,Na22G_d) 
Canal1CoG_a = IntegralDoble2(845,959,Co60G_d)[0]
Canal2CoG_a = IntegralDoble2(845,959,Co60G_d)[1]
SumaGNa_a = IntegralSencillo(1298,Na22G_d)
SumaGCo_a = IntegralSencillo(1818,Co60G_d)
# despues Guayana------------
CanalCdG_d = IntegralSencilloCd(71,Cd109G_d) #(canal,archivo)
CanalCsG_d = IntegralSencillo(485,Cs137G_d)  
CanalNa1G_d = IntegralSencillo(376,Na22G_d)  
CanalNa2G_d = IntegralSencillo(914,Na22G_d) 
Canal1CoG_d = IntegralDoble2(846,957,Co60G_d)[0]
Canal2CoG_d = IntegralDoble2(846,957,Co60G_d)[1]
SumaGNa_d = IntegralSencillo(1297,Na22F_d)
SumaGCo_d = IntegralSencillo(1815,Co60F_d)
#1460.82
CanalG_a=[CanalCdG_a,CanalNa1G_a,CanalCsG_a,Canal1CoG_a,CanalNa2G_a,Canal2CoG_a,SumaGNa_a,SumaGCo_a]
#del CanalG_a[0]
EnergiaG_a=[88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]
#del EnergiaG_a[0]

CanalG_d=[CanalCdG_d,CanalNa1G_d,CanalCsG_d,Canal1CoG_d,CanalNa2G_d,Canal2CoG_d,SumaGNa_d,SumaGCo_d]
#del CanalG_d[0]
EnergiaG_d=[88.033,511.0,661.657,1173.228,1274.537,1332.490,1785.573,2505.718]
#del EnergiaG_d[0]

#==============================Calibracion=============================================(esta funcion promedia de una vez antes y despues, vea 'ejeX')

def Calibracion(archivo,canal_a,energia_a,canal_d,energia_d):

    X= archivo[:,0]
    picoscal = len(canal_a)
    pce_a = [0.0,fabs(energia_a[1]-energia_a[picoscal-1])/fabs(canal_a[1]-canal_a[picoscal-1]),1.0]#parametros Iniciales de ajuste canal energia
    pce_d = [0.0,fabs(energia_d[1]-energia_d[picoscal-1])/fabs(canal_d[1]-canal_d[picoscal-1]),1.0]#parametros Finales de ajuste canal energia

    #pce_a =[0.0,1.0]
    #pce_d =[0.0,1.0]
    
    popt_a, pcov_a = curve_fit(canalenergia,canal_a,energia_a,pce_a)
    popt_d, pcov_d = curve_fit(canalenergia,canal_d,energia_d,pce_d)

    ejeX = canalenergia(X,(popt_a[0]+popt_d[0])/2.0,(popt_a[1]+popt_d[1])/2.0,(popt_a[2]+popt_d[2])/2.0)

    return [ejeX,(popt_a[0]+popt_d[0])/2.0,(popt_a[1]+popt_d[1])/2.0,(popt_a[2]+popt_d[2])/2.0]
    #return ejeX

def CalibracionA(archivo,canal_a,energia_a,canal_d,energia_d):

    X= archivo[:,0]
    picoscal = len(canal_a)
    pce_a = [0.0,fabs(energia_a[1]-energia_a[picoscal-1])/fabs(canal_a[1]-canal_a[picoscal-1]),1.0]#parametros Iniciales de ajuste canal energia
    pce_d = [0.0,fabs(energia_d[1]-energia_d[picoscal-1])/fabs(canal_d[1]-canal_d[picoscal-1]),1.0]#parametros Finales de ajuste canal energia

    #pce_a =[0.0,1.0]
    #pce_d =[0.0,1.0]
    
    popt_a, pcov_a = curve_fit(canalenergia,canal_a,energia_a,pce_a)
    popt_d, pcov_d = curve_fit(canalenergia,canal_d,energia_d,pce_d)

    ejeX = canalenergia(X,popt_a[0],popt_a[1],popt_a[2])
    
    return [ejeX,popt_a[0],popt_a[1],popt_a[2]]

def CalibracionD(archivo,canal_a,energia_a,canal_d,energia_d):

    X= archivo[:,0]
    picoscal = len(canal_a)
    pce_a = [0.0,fabs(energia_a[1]-energia_a[picoscal-1])/fabs(canal_a[1]-canal_a[picoscal-1]),1.0]#parametros Iniciales de ajuste canal energia
    pce_d = [0.0,fabs(energia_d[1]-energia_d[picoscal-1])/fabs(canal_d[1]-canal_d[picoscal-1]),1.0]#parametros Finales de ajuste canal energia

    #pce_a =[0.0,1.0]
    #pce_d =[0.0,1.0]
    
    popt_a, pcov_a = curve_fit(canalenergia,canal_a,energia_a,pce_a)
    popt_d, pcov_d = curve_fit(canalenergia,canal_d,energia_d,pce_d)

    ejeX = canalenergia(X,popt_d[0],popt_d[1],popt_d[2])
    
    return [ejeX,popt_d[0],popt_d[1],popt_d[2]]
    

#================Grafica Archivo Con Calibracion Promedio===========================

#------U--------

ejeXCPatronU = Calibracion(PatronU,CanalU_a,EnergiaU_a,CanalU_d,EnergiaU_d)[0]
cortePatronU = Calibracion(PatronU,CanalU_a,EnergiaU_a,CanalU_d,EnergiaU_d)[1]
pendientePatronU = Calibracion(Fondo,CanalU_a,EnergiaU_a,CanalU_d,EnergiaU_d)[2]

#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.plot(ejeXCPatronU,PatronU[:,1],ls='steps-mid',lw=1.0)
#fig.show()

#------Th-------

ejeXCPatronTh = Calibracion(PatronTh,CanalTh_a,EnergiaTh_a,CanalTh_d,EnergiaTh_d)[0]
cortePatronTh = Calibracion(PatronTh,CanalTh_a,EnergiaTh_a,CanalTh_d,EnergiaTh_d)[1]
pendientePatronTh = Calibracion(Fondo,CanalTh_a,EnergiaTh_a,CanalTh_d,EnergiaTh_d)[2]

#fig2=plt.figure()
#ax2=fig2.add_subplot(111)
#ax2.plot(ejeXCPatronTh,PatronTh[:,1],ls='steps-mid',lw=1.0)
#fig2.show()

#-------K--------

ejeXCPatronK = Calibracion(PatronK,CanalK_a,EnergiaK_a,CanalK_d,EnergiaK_d)[0]
cortePatronK = Calibracion(PatronK,CanalK_a,EnergiaK_a,CanalK_d,EnergiaK_d)[1]
pendientePatronK = Calibracion(Fondo,CanalK_a,EnergiaK_a,CanalK_d,EnergiaK_d)[2]

#fig3=plt.figure()
#ax3=fig3.add_subplot(111)
#ax3.plot(ejeXCPatronK,PatronK[:,1],ls='steps-mid',lw=1.0)
#fig3.show()

#----Guayana-----


corteGuayana = Calibracion(Guayana,CanalG_a,EnergiaG_a,CanalG_d,EnergiaG_d)[1]
pendienteGuayana = Calibracion(Fondo,CanalG_a,EnergiaG_a,CanalG_d,EnergiaG_d)[2]

#fig4=plt.figure()
#ax4=fig4.add_subplot(111)
#ax4.plot(ejeXCGuayana,Guayana[:,1],ls='steps-mid',lw=1.0)
#fig4.show()

#-----Fondo------

ejeXCFondo = Calibracion(Fondo,CanalF_a,EnergiaF_a,CanalF_d,EnergiaF_d)[0]
corteFondo = Calibracion(Fondo,CanalF_a,EnergiaF_a,CanalF_d,EnergiaF_d)[1]
pendienteFondo = Calibracion(Fondo,CanalF_a,EnergiaF_a,CanalF_d,EnergiaF_d)[2]

#fig5=plt.figure()
#ax5=fig5.add_subplot(111)
#ax5.plot(ejeXCFondo,Fondo[:,1],ls='steps-mid',lw=1.0)
#fig5.show()

#============================"REBIENADO"========================================

def Rebin(archivo,corte,pendiente):
    y=archivo[:,1]
    data=[]
    for n in range(0,len(archivo[:,0]),1):# observe el doble ciclo: primero se recorren todos los canales
        for m in range(0,int(y[n]),1): # para cada canal se recorren cada una de las cuentas
            data.append(archivo[n,0]*pendiente+corte+uniform(-1, 1)*pendiente) # data guarda todas las cuentas No un histograma, el histograma se arma despues
                                                       # a cada cuenta le da la opcion de caer tambien en los canales vecinos
                                                       # al multiplicar por (*a) fluctua menos el espectro
    binwidth=10.0  #KeV                                    
    cuentas, bins, patches = plt.hist(data, bins=np.arange(0, 3000, binwidth), facecolor='green', alpha=0.5)
    return bins, cuentas

#-----------------Ejes "Rebineados"-----------

FondoRebinX, FondoRebinY = Rebin(Fondo,corteFondo,pendienteFondo)
FondoRebinX2 = delete(FondoRebinX,len(FondoRebinX)-1)

GuayanaRebinX, GuayanaRebinY = Rebin(Guayana,corteGuayana,pendienteGuayana)
GuayanaRebinX2 = delete(GuayanaRebinX,len(GuayanaRebinX)-1)

PatronURebinX, PatronURebinY = Rebin(PatronU,cortePatronU,pendientePatronU)
PatronURebinX2 = delete(PatronURebinX,len(PatronURebinX)-1)

PatronThRebinX, PatronThRebinY = Rebin(PatronTh,cortePatronTh,pendientePatronTh)
PatronThRebinX2 = delete(PatronThRebinX,len(PatronThRebinX)-1)

PatronKRebinX, PatronKRebinY = Rebin(PatronK,cortePatronK,pendientePatronK)
PatronKRebinX2 = delete(PatronKRebinX,len(PatronKRebinX)-1)

#fig8=plt.figure()
#ax8=fig8.add_subplot(111)
#ax8.plot(PatronURebinX2,PatronURebinY,ls='steps-mid',lw=1.0)
#ax8.plot(PatronKRebinX2,PatronKRebinY,ls='steps-mid',lw=1.0)
#ax8.plot(PatronThRebinX2,PatronThRebinY,ls='steps-mid',lw=1.0)
#ax8.plot(GuayanaRebinX2,GuayanaRebinY,ls='steps-mid',lw=1.0)
#ax8.plot(FondoRebinX2,FondoRebinY,ls='steps-mid',lw=1.0)
#fig8.show()

#---------------Normalizado----------------

GuayanaNormaY = (GuayanaRebinY/(8.0*60))
FondoNormaY = FondoRebinY/(18.0*60)
UNormaY = PatronURebinY/(0.5*60)
ThNormaY = PatronThRebinY/(0.5*60)
KNormaY = PatronKRebinY/(0.5*60)

GuayanaDef = GuayanaNormaY-FondoNormaY
ThDef = ThNormaY-FondoNormaY
UDef = UNormaY-FondoNormaY
KDef = KNormaY-FondoNormaY

#fig9=plt.figure()
#ax9=fig9.add_subplot(111)
#ax9.plot(GuayanaRebinX2,GuayanaNormaY,ls='steps-mid',lw=1.0)
#ax9.plot(FondoRebinX2,FondoNormaY,ls='steps-mid',lw=1.0)
#ax9.plot(GuayanaRebinX2,GuayanaDef,ls='steps-mid',lw=1.0)
#fig9.show()

#=========================LECTURA GERMANIO=========================================
# way='../Data/Ge/CNF/data/'
# GuayanaGe = genfromtxt(way+'Guayana.xy') # esta en cuentas por hora
# PatronUGe = genfromtxt(way+'PatronU.xy')
# PatronThGe = genfromtxt(way+'PatronTh.xy')
# PatronKGe = genfromtxt(way+'PatronK.xy')

#=========================LECTURA BGO=========================================
# way2='../Data/BGO/CNF/data/'
# GuayanaBGO = genfromtxt(way2+'Guayana15h.xy') # esta en cuentas por hora
# PatronUBGO = genfromtxt(way2+'PatronU.xy')
# PatronThBGO = genfromtxt(way2+'PatronTh.xy')
# PatronKBGO = genfromtxt(way2+'PatronK.xy')

#=============================MULTIPLOTS===========================================

#GuayanaNaI = genfromtxt(path+'G6H.xy')    #realmente es CsI

#------Grafica 1------                
# f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey=False)
# #f, (ax1, ax3) = plt.subplots(2, sharex=True, sharey=False)
# #f.set_size_inches(10.5, 6.5, forward=True)


# gcf().subplots_adjust(bottom=0.12)
# gcf().subplots_adjust(right=0.99)
# gcf().subplots_adjust(left=0.10)
# gcf().subplots_adjust(top=0.96)



# GuayanaGeFigura, = ax4.plot((0.386001695767*(GuayanaGe[:,0])-26.0031922218),GuayanaGe[:,1]/100,lw=2.0,ls='steps-mid')
# GuayanaNaIFigura, = ax4.plot(GuayanaRebinX2,GuayanaDef*3.5,lw=2.0,ls='steps-mid')

# GuayanaGeFigura, = ax3.plot((0.386001695767*(GuayanaGe[:,0])-26.0031922218),GuayanaGe[:,1]/100,lw=2.0,ls='steps-mid')
# GuayanaNaIFigura, = ax3.plot(GuayanaRebinX2,GuayanaDef*5,lw=2.0,ls='steps-mid')

# '''
# GuayanaGeFigura2, = ax2.plot((0.386001695767*(GuayanaGe[:,0])-26.0031922218),GuayanaGe[:,1],lw=2.0,ls='steps-mid',color='g')
# PatronUGeFigura, =  ax2.plot((0.386001695767*PatronUGe[:,0]-26.0031922218),PatronUGe[:,1],lw=2.0,ls='steps-mid',color='c')
# PatronThGeFigura, =  ax2.plot((0.386001695767*PatronThGe[:,0]-26.0031922218),PatronThGe[:,1],lw=2.0,ls='steps-mid',color='r')
# PatronKGeFigura, =  ax2.plot((0.386001695767*PatronKGe[:,0]-26.0031922218),PatronKGe[:,1],lw=2.0,ls='steps-mid',color='#000000')
# '''

# GuayanaNaIFigura2, = ax2.plot(GuayanaRebinX2,GuayanaDef*15,lw=2.0,ls='steps-mid',color='b')

# #GuayanaBGOFigura2, = ax2.plot(BGO.GuayanaRebinX2,BGO.GuayanaDef*15,lw=2.0,ls='steps-mid', color='k')

# PatronUGeFigura1, =  ax2.plot((0.386001695767*(PatronUGe[:,0])-26.0031922218),PatronUGe[:,1]/100,lw=2.0,ls='steps-mid',color='c')
# PatronThGeFigura1, =  ax2.plot((0.386001695767*PatronThGe[:,0]-26.0031922218),PatronThGe[:,1]/100,lw=2.0,ls='steps-mid',color='r')
# PatronKGeFigura1, =  ax2.plot((0.386001695767*PatronKGe[:,0]-26.0031922218),PatronKGe[:,1]/100,lw=2.0,ls='steps-mid',color='#000000')

# GuayanaNaIFigura2, = ax1.plot(GuayanaRebinX2,GuayanaDef*2,lw=2.0,ls='steps-mid',color='b')
# PatronUGeFigura1, =  ax1.plot((0.386001695767*(PatronUGe[:,0])-26.0031922218),PatronUGe[:,1]/100,lw=2.0,ls='steps-mid',color='c')
# PatronThGeFigura1, =  ax1.plot((0.386001695767*PatronThGe[:,0]-26.0031922218),PatronThGe[:,1]/100,lw=2.0,ls='steps-mid',color='r')
# PatronKGeFigura1, =  ax1.plot((0.386001695767*PatronKGe[:,0]-26.0031922218),PatronKGe[:,1]/100,lw=2.0,ls='steps-mid',color='#000000')

# #----------etiqueta--------

# ax1.legend([GuayanaNaIFigura2,PatronUGeFigura1,PatronThGeFigura1,PatronKGeFigura1], ["Sample-CsI$\\times{10}$","$^{238}$U (Ge)$/100$","$^{232}$Th (Ge)$/100$","$^{40}$K (Ge)$/100$"], fontsize=17.5, bbox_to_anchor=(0.50, 0.85, 1., .102), loc=2, ncol=1, borderaxespad=0.)

# ax2.legend([GuayanaNaIFigura2,PatronUGeFigura1,PatronThGeFigura1,PatronKGeFigura1], ["Sample-CsI$\\times{15}$","$^{238}$U (Ge)$/100$","$^{232}$Th (Ge)$/100$","$^{40}$K (Ge)$/100$"], fontsize=17.5, bbox_to_anchor=(0.30, 0.85, 1., .102), loc=2, ncol=1, borderaxespad=0.)

# ax3.legend([GuayanaGeFigura,GuayanaNaIFigura], ["Sample-Ge$/100$","Sample-CsI$\\times{5}$"], fontsize=17.5, bbox_to_anchor=(0.50, 0.85, 1., .102), loc=2, ncol=1, borderaxespad=0.)

# ax4.legend([GuayanaGeFigura,GuayanaNaIFigura], ["Sample-Ge$/100$","Sample-CsI$\\times{3.5}$"], fontsize=17.5, bbox_to_anchor=(0.30, 0.85, 1., .102), loc=2, ncol=1, borderaxespad=0.)

# #------------------------

# plt.setp(ax1.get_xticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax1.get_yticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax2.get_xticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax2.get_yticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax3.get_xticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax3.get_yticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax4.get_xticklabels(), rotation='horizontal', fontsize=18.5)
# plt.setp(ax4.get_yticklabels(), rotation='horizontal', fontsize=18.5)

# #plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

# f.text(0.5, 0.04, 'Energy (keV)', fontsize=19, ha='center', va='center')
# f.text(0.05, 0.5, 'Counts/min', fontsize=19, ha='center', va='center', rotation='vertical')

# xmin0=1350
# xmax0=1680

# xmin1=1680
# xmax1=2770

# y1min=0
# y1max=50
# y2max=4

# ax1.set_xlim(xmin0,xmax0)
# ax2.set_xlim(xmin1,xmax1)
# ax3.set_xlim(xmin0,xmax0)
# ax4.set_xlim(xmin1,xmax1)


# ax1.set_ylim(0,45)
# ax2.set_ylim(0,45)
# ax3.set_ylim(0,60)
# ax4.set_ylim(y1min,y2max)


# space1y=15
# space2y=1

# ax1.set_yticks(range(int(y1min)+space1y,int(y1max),space1y))
# ax2.set_yticks(range(int(y1min)+space1y,int(y1max),space1y))
# ax3.set_yticks(range(int(y1min)+space1y,int(y1max),space1y))
# ax4.set_yticks(range(int(y1min)+space2y,int(y2max),space2y))

# space1x=200
# space2x=65

# ax1.set_xticks([1361,1461,1561,1661])#range(int(xmin0),int(xmax0),space2x))
# #ax2.set_xticks([1768,1979,2190,2401,2612])
# ax3.set_xticks([1350,1461,1550,1650])
# ax4.set_xticks([1768,1979,2190,2401,2612])


# #ax4.set_xticks(range(int(xmin1),int(xmax1),space1x))
# f.set_size_inches(13.5, 6.5, forward=True)
# f.subplots_adjust(hspace=0)

# f.show()
# #f.legend()
# f.savefig('figuras/mult_BGO_K.pdf')
# plt.show()


# #--------------------------------------------------------------------------
# #sdfsd fsdf
