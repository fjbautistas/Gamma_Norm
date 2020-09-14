import numpy as np
import spectra as sp
from scipy.optimize import curve_fit
import quantities as pq

class roi_cal:
    def __init__(self,i,E_center,f, type='Gauss_Rect'):
        self.Initial=int(i)
        self.E_center=np.array(E_center)
        self.Final=int(f)
        self.center=int((self.Final-self.Initial)/2+(self.Initial))
        self.type=type
        self.fit={'Gauss_Rect':self.fit_GaussRect,
                  'Double_Gauss_Rect':self.fit_2GaussRect}
                  #'Gaus_Step':self.fit_GaussStep,
                  #'Double_Gauss_Step':self.fit_DGaussStep}
        
    def set_spectrum(self,spectrum):
        self.spectrum=spectrum
        self.fit[self.type]()
        
    def fit_GaussRect(self):

        m=float((self.spectrum.counts[self.Final]-self.spectrum.counts[self.Initial])
                /(self.spectrum.channels[self.Final]-self.spectrum.channels[self.Initial]))
        b=(self.spectrum.counts[self.Final]+self.spectrum.counts[self.Initial])/2
        s=len(self.spectrum.channels[self.Initial:self.Final])/6
        self.p0=np.array([self.spectrum.counts[self.center]-b, #amplitude
                          self.center,#mu
                          s, #sigma
                          float(b-m*self.center),#a_0
                          float(m)]) #a_1
                          #self.center])#x_0]
        
        #print('p0=',self.p0)
        try:
            self.popt, self.pcov = curve_fit(roi_cal.Gaussrect,
                                             self.spectrum.channels[self.Initial:self.Final],
                                             self.spectrum.counts[self.Initial:self.Final],
                                             self.p0)
        
        except RuntimeError:
            self.popt=self.p0
            print('Optimal parameters not found, p0=Optimal parameters')

        
        self.Amp, self.mu,self.sigma = self.popt[0],self.popt[1],self.popt[2]
        self.a_0, self.a_1,self.x_0 = self.popt[3],self.popt[4],self.mu

        self.OP=[self.popt]

#===============================En Construcción=============================================
         
    def fit_2GaussRect(self):
        
        s1=(self.center-self.Initial)*(1/3.0)
        mu1=(self.center+self.Initial)*(1/2.0) 
        s2=(self.Final-self.center)*(1/3.0)
        mu2=(self.center+self.Final)*(1/2.0)
        mu,Sigma=[mu1,mu2],[s1,s2]
        self.p0=np.array([max(self.spectrum.counts[int(self.Initial):int(self.center)]), #Amplitude_1
                          mu[0], #centroid_1
                          Sigma[0], #sigma_1
                          float(self.spectrum.counts[int(s1-mu[0])]), #a_0
                          float((self.spectrum.counts[self.Final]-self.spectrum.counts[self.Initial])
                                /(self.spectrum.channels[self.Final]-self.spectrum.channels[self.Initial])), #a_1
                          mu[0], #x_1
                          max(self.spectrum.counts[int(self.Initial):int(self.center)]), #Amplitude_2
                          mu[1], #centroid_2
                          Sigma[1] #sigma_2
                          ])
            
        self.popt, self.pcov = curve_fit(roi_cal.TwoGaussRect,
                                         self.spectrum.channels[self.Initial:self.Final],
                                         self.spectrum.counts[self.Initial:self.Final],
                                         self.p0)

        self.Amp, self.mu1,self.sigma1=self.popt[0],self.popt[1],self.popt[2]
        self.a_0, self.a_1,self.x_0=self.popt[3],self.popt[4],self.popt[5]
        self.Amp2, self.mu2,self.sigma2=self.popt[6],self.popt[7],self.popt[8]
        self.mu=[self.mu1,self.mu2]
        self.sigma=[self.sigma1,self.sigma2]
        self.OP=[self.mu+self.sigma]
        
#======================================================================================
    
    def Cal_Intensity(self):
        self.inten=self.Amp*self.sigma*np.sqrt(2*np.pi)/self.spectrum.LifeTime
        self.di=np.sqrt(self.inten)/self.spectrum.LifeTime
        self.intensity=pq.UncertainQuantity(self.inten,pq.m,self.di) #m=cuounts-energy
        #self.intensity=self.Amp*self.sigma*np.sqrt(2*np.pi)
        self.Cal_DIntensity()

    def rectIntegral(self):
        self.rectIntegral=self.a_1/2*(self.Final**2-self.Initial**2)+(self.a_0-self.x_0*self.a_1)*(self.Final-self.Initial)
        return self.rectIntegral
        
    def Cal_DIntensity(self):
        self.discreteTotalInt=np.sum(self.spectrum.counts[self.Initial:self.Final])
        self.discreteIntensity=(self.discreteTotalInt-self.rectIntegral())/self.spectrum.LifeTime
        self.discreteInteSigma=np.sqrt(np.sum(self.spectrum.sigma[self.Initial:self.Final]**2))/self.spectrum.LifeTime

#--------------------------------------------------------------------------------
        
    #def EFF

#--------------------------------------------------------------------------------
    
    @staticmethod
    def gauss(x,a,mu,sigma):
        return a*np.exp(-0.5*((x-mu)/sigma)**2)
    
    @staticmethod
    def rect(x,a_0,a_1,x_0):
        return a_0 + a_1*(x-x_0)
    
    @staticmethod
    def Gaussrect(x,g_a,g_mu,g_sigma,a_0,a_1):
        return roi_cal.gauss(x, g_a, g_mu, g_sigma)\
            + roi_cal.rect(x,a_0,a_1,g_mu)

    @staticmethod
    def TwoGaussRect(x,g_a,g_mu,g_sigma,a_0,a_1,x_0,G_a,G_mu,G_sigma):
        return roi_cal.gauss(x, g_a, g_mu, g_sigma)\
            +roi_cal.rect(x,a_0,a_1,x_0)\
            +roi_cal.gauss(x, G_a, G_mu, G_sigma)
    

class rois:
    def __init__(self, regions): #regions lista de roi_cal
        self.regions=regions

    def set_spectrum(self,spectrum):
        for region in self.regions:
            region.set_spectrum(spectrum)

    def get_intensity(self):
        I=[]
        for region in self.regions:
            I.append(region.intensity)
        return I
    def Cal_Intensity(self):
        for region in self.regions:
            region.Cal_Intensity()
        
     
class calibration:
    def __init__(self,rois_set): #rois_set lista de rois
        self.rois_set=rois_set
        self.p0=[]

    def cal(self):
        self.CalPoints=[]
        self.Energy=[]
        self.sigma=[]
        for rois in self.rois_set:
            for roi in rois.regions:
                self.CalPoints.append(roi.mu)
                self.sigma.append(roi.sigma)
                self.Energy.append(roi.E_center)
        self.set_p0()
        self.popt, self.pcov = curve_fit(calibration.rect,
                                         self.CalPoints,
                                         self.Energy,
                                         self.p0)#,
                                         #self.sigma)
        self.a_0=self.popt[0]
        self.a_1=self.popt[1]
        #self.a_2=self.popt[2]

    @staticmethod
    def rect(x,a_0,a_1):#,a_2=0):
        return a_0 + a_1*(x) #+ a_2*x*x

    def set_p0(self):
        #a2=-0.01
        a1=((max(self.CalPoints)-min(self.CalPoints))/(max(self.Energy)-min(self.Energy)))
        a0=-a1*(min(self.CalPoints))+min(self.Energy)
        self.p0=[a0,a1]#,a2]
        
        
