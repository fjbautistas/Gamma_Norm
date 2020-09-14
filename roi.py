import calibration as cl
import spectra as sp


class roi(cl.roi_cal):
    def __init__(self,Ei,c,Ef,type='Gauss_Rect'):
        self.Ei=Ei
        self.c=c
        self.Ef=Ef
        self.type=type

    def set_spectrum(self,spectrum):
        def e2c(e):
            return int((e-spectrum.a0)/spectrum.a1)
        cl.roi_cal.__init__(self,e2c(self.Ei),self.c,e2c(self.Ef),self.type)
        cl.roi_cal.set_spectrum(self,spectrum)
        self.mu=self.mu*spectrum.a1
        self.sigmaE=self.sigma*spectrum.a1
        self.Cal_Intensity()
    '''
    def intensity(self):
        cl.roi_cal.intensity(self)*spectrum.a1

    '''
if __name__ == '__main__':
    espectro=sp.spectra('Data/CsI/CNF/Cal_Co2.CNF')
    a0,a1=0,1
    espectro.set_cal(a0,a1)
    testROI=roi(10,20,30)

