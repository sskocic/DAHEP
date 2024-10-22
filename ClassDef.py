import math as m
import numpy as np


class Boson:

        isfermion=False

        def __init__(self,name,spin,momentum):
                self.name=name
                self.spin=spin
                self.momentum=momentum

        def PrintInfo(self):
                print("Name: " + self.name+", Spin: "+str(self.spin) +", Momentum: "+str(self.momentum)+", Fermion:"+str(self.isfermion))

class Higgs(Boson):
        MassSigma=1
        def __init__(self, name, spin, momentum, MeanMass):
            super().__init__(name,spin,momentum)
            self.MeanMass = MeanMass

        def Energy(self):
                return m.sqrt((self.momentum)**2 + (self.MeanMass)**2)
        
        def generate_mass(self):
                return np.random.normal(self.MeanMass, self.MassSigma)


