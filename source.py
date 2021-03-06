import numpy as np
import quantities as pq
import sys
#import xylib as xy
from datetime import datetime, timedelta

 
year=timedelta(days=365).total_seconds()  #Objeto timedelta es una diferencia de fechas que se puede operar (+ , - , *, ...). 
day=timedelta(days=1).total_seconds()

class source:
        def __init__(self, serial, A0, dA, T, dT,E_B, t_cal):
                self.tau=pq.UncertainQuantity(T, pq.s, dT)/np.log(2)
                self.dA=A0*dA
                self.t_cal=t_cal                
                self.A0=pq.UncertainQuantity(A0, pq.Bq, dA)
                self.energy_branch()
        def activity(self,t_measure):
                self.delta=(t_measure-self.t_cal).total_seconds()
                Dt=pq.UncertainQuantity(self.delta,pq.s,0)
                return self.A0*np.exp(-Dt/self.tau)
        def energy_branch(self):
                self.EB=np.array(E_B)
       
Ba133=source('D-111-17', 31300, 0.05, 3848.7*day,1.2*day,([(53.1925,0.0006),(276.3989 , 0.001),(302.8508 , 0.0005),(356.0129 ,0.0007),(383.8485 , 0.0012)], [(0.0214, 0.0003),(0.0716, 0.0005),(0.1834,0.0013),(0.6205, 0.0019), (0.0894,0.0006)]),datetime(2006,6,8))
'''
Cd109=source(41F11-3,37000, 0.2, 461.4*day,1.2*day, ([(88.0336,0.0011)],[(0.03626,0.00020)]),datetime(2010,5,25))

Co57=source(39F15-9, 37000, 0.2, 271.80*day, 0.05*day,([(122.06065,0.00012),(136.47350,0.000029)], [(0.8551,0.0006),(0.1071,0.0015)]),datetime(2010,5,25))

Cs137=source(D-110-20, 41100, 0.05, 30.08*year, 0.009*year,( [(661.657,0.03)],[(0.8499, 0.0020)]),datetime(2006,5,18))

Mn54=source(D-110-21, 34600, 0.05, 312.29*day, 0.26*day,([(834.838,0.005)],[(0.999746,0.000011)]), datetime(2006,5,18))

Na22=source(D-112-1, 31900, 0.05, 950.57*day, 0,23*day, ([(1274.537,0.003)],[(0.9994),0.00014]),datetime(2006,7,10))

Co60=source(D-111-13, 34800, 0.05, 1925,23*day, 0.27*day, ([(1173.228,0.003),(1332.490,0.004)],[(0.8551,0.0006),(0.1071,0.0015)]),datetime(2006,6,8))

Eu152=source(1132, 7650, 0,05, 4941*day, 7*day, ([(344.2785,0.0012),(443.965,0.003),(778.9045,0.0024),(867.380,0.003),(964.072,0.018),(1112.076,0.003),(1212.948,0.011), (1299.142,0.008),(1408.013,0.003)],[(0.2658,0.0012),(0.03125,0.00014),(0.1296,0.0006),(0.04241,0.00023),(0.1462,0.0006),(0.1340,0.0006),(0.01415,0.00009),(0.01632,0.00009),(0.2085,0.0009)]), datetime (2006, 7,13))

Eu154=source(1132, 8450, 0.05, 3138.1*day, 1.4*day, ([(591.755, 0.003),(756.8020, 0.0023),(873.1834, 0.0023),(996.262, 0.006),(1004.725, 0.007),(1596.4804, 0.0028)],[(0.0495, 0.0005),(0.0453, 0.0005),(0.1217, 0.0012),(0.1050, 0.0010),(0.1785, 0.0017),(0.01783, 0.00017)]), datetime(2006, 7,13))

Eu155=source(1132, 12800, 0.05, 1736*day, 6*day, ([(45.2990, 0.0010),(60.0086, 0.0010),(105.3083, 0.0010)],[(0.0131, 0.0005),(0.0122, 0.0005),(0.211, 0.006)]), datetime(2006, 7,13))
'''
