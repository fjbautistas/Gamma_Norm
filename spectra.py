import numpy as np
import matplotlib.pyplot as plt
import xylib_capi as xy
import mca_read as mca
import sys
from datetime import datetime, timedelta
import copy

class spectra:
    def __init__(self, File, val_PreCal=False):
        self.File=File
        self.val_PreCal=val_PreCal
        extension=self.File.split('.')[-1]
        if extension=='CNF':
            return self.read_file_CNF()
        elif extension=='mca':
            return self.read_file_mca()
        else:
            print('File:',File, 'type unkown, ext:','-',extension, '-','File type unkown')
        #self.info_time()
        
    def set_cal(self,a0,a1,a2=0):
        self.a0=a0
        self.a1=a1
        self.a2=a2
        self.cal_energy=self.ch2Energy(self.channels)
        
    def read_file_CNF(self):
        #if self.File.split('.')[1]=='CNF':
        self.dataset = xy.load_file(self.File.encode(), None, None)
        if not self.dataset:
            print("File not found:", self.File)
            sys.exit(1)
        self.block = xy.get_block(self.dataset, 0)
        self.ncol = xy.count_columns(self.block)
        self.rows = xy.count_rows(self.block, 2)
        channels,energy,counts=[],[],[]
        for i in range(self.rows):
            channels.append(xy.get_data(self.block, 0, i))
            energy.append(xy.get_data(self.block, 1, i))
            counts.append(xy.get_data(self.block, 2, i))
        self.LifeTime=float(xy.block_metadata(self.block,
                                              b'live time (s)'))
        self.RealTime=float(xy.block_metadata(self.block,
                                              b'real time (s)'))
        self.DataMeasure=xy.block_metadata(self.block,
                                           b'date and time')
        self.PreCal=[float(xy.block_metadata(self.block,
                                             b'energy calib 0')),\
                     float(xy.block_metadata(self.block,
                                             b'energy calib 1')),\
                     float(xy.block_metadata(self.block,
                                             b'energy calib 2'))]
        self.counts=np.array(counts,int)
        self.channels=np.array(channels,int)
        self.energy=np.array(energy,int)
        self.calc_sigma()
        if self.val_PreCal:
            self.set_cal(self.PreCal[0],self.PreCal[1])
        self.year = int(self.DataMeasure.split()[1][0:4])
        self.month = int(self.DataMeasure.split()[1][5:7])
        self.day = int(self.DataMeasure.split()[1][8:10])
        self.hour = int(self.DataMeasure.split()[2][0:2])
        self.minute = int(self.DataMeasure.split()[2][3:5])
        self.seconds = int(self.DataMeasure.split()[2][6:8])
        self.Measure=datetime(self.year,
                              self.month,
                              self.day,
                              self.hour,
                              self.minute,
                              self.seconds)
        
#----------------------------------------------------------------------
    def read_file_mca(self):
        #elif self.File.split('.')[1]=='mca':
        block=mca.read_mca_file(self.File,'latin-1')
        if not block:
            print("File not found:", self.File)
            sys.exit(1)
        block.read_file()
        energy,counts=[],[]
        for i in range(len(block.data)):
            counts.append(block.data[i])
        channels=np.arange(len(block.data))
        self.LifeTime=float(block.liveTime)
        self.RealTime=float(block.realTime)
        self.DataMeasure=block.date
        self.counts=np.array(counts,int)
        self.channels=np.array(channels,int)
        self.energy=np.array(energy,int)
        self.calc_sigma()
        self.year = int(self.DataMeasure.split()[0][6:10])
        self.month =  int(self.DataMeasure.split()[0][0:2])
        self.day =  int(self.DataMeasure.split()[0][3:5])
        self.hour = int(self.DataMeasure.split()[1][0:2])
        self.minute = int(self.DataMeasure.split()[1][3:5])
        self.seconds = int(self.DataMeasure.split()[1][6:8])
        self.Measure=datetime(self.year,
                              self.month,
                              self.day,
                              self.hour,
                              self.minute,
                              self.seconds)

    def ch2Energy(self,x):
        return self.a1*x+self.a0

    def rebining(self,Ebin):
        energyMin = self.ch2Energy(self.channels[0]-0.5)
        energyMax = self.ch2Energy(self.channels[-1]+0.5)

        rEnergyMin = np.floor(np.floor(energyMin)/Ebin)*Ebin
        rEnergyMax = np.ceil(np.ceil(energyMax)/Ebin)*Ebin

        rEnergy=np.arange(rEnergyMin+0.5*Ebin,rEnergyMax,Ebin)
        self.spectraout=np.zeros(len(rEnergy),dtype=[('energy','f4'), ('counts','i4')])
        self.spectraout['energy']=rEnergy

        for channel in self.channels:
            Econtinuous=np.random.uniform(self.ch2Energy(channel-0.5),
                                          self.ch2Energy(channel+0.5),
                                          self.counts[channel])
            indexes=np.floor((Econtinuous-rEnergyMin)/Ebin)
            for index in indexes:
                self.spectraout['counts'][int(index)]+=1
        EnergyFilter=rEnergy>0
        self.cal_energy=self.spectraout['energy'][EnergyFilter]
        self.counts=self.spectraout['counts'][EnergyFilter]
        self.calc_sigma()
        self.channels=np.arange(len(rEnergy[EnergyFilter]))
        #self.a0=rEnergyMin+0.5*Ebin
        self.a0=0.5*Ebin
        self.a1=Ebin

    def calc_sigma(self):
        self.sigma=np.sqrt(self.counts)
        
    def __sub__(self,other):
        oCopy=copy.deepcopy(self)
        length=min(len(oCopy.channels),len(other.channels))

        leftCountrate=(oCopy.counts[0:length]/oCopy.LifeTime)
        rightCountrate=(other.counts[0:length]/other.LifeTime)

        leftSigmarate=(oCopy.sigma[0:length]/oCopy.LifeTime)
        rightSigmatrate=(other.sigma[0:length]/other.LifeTime)
        
        oCopy.counts=(leftCountrate-rightCountrate)*oCopy.LifeTime
        oCopy.sigma=np.sqrt(leftSigmarate**2+rightSigmatrate**2)*oCopy.LifeTime
        return oCopy

if __name__ == '__main__':
    espectro1=spectra('Data/CsI/CNF/Cal_Cs4.CNF')
#    espectro2=spectra('Data/NaI2x2_old/mca/Cal_Co4.mca')
    espectro2=spectra('Data/NaI2X2/mca/Guayana8h.mca')
    print('dates:', 'cnf: ',espectro1.Measure, 'mca: ',espectro2.Measure)
    print("tiempo de medida", espectro2.LifeTime)
    print('channels:', len(espectro1.channels), len(espectro2.channels))
    print('counts:', max(espectro1.counts), max(espectro2.counts))
    fig = plt.figure()
    ax = fig.add_subplot(111)    
    plt.xlabel("Canales",fontsize=19)
    plt.ylabel("Cuentas",fontsize=19)

    # grafica, = plt.plot(espectro1.channels,
    #                     espectro1.counts,
    #                     ls='steps-mid',
    #                     lw=1.8,
    #                     color='b')
    grafica2, = plt.plot(espectro2.channels,
                         espectro2.counts,
                         ls='steps-mid',
                         lw=1.8,
                         color='b')
    plt.show()
