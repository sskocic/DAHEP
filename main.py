from ClassDef import Boson
from ClassDef import Higgs

foton=Boson("Foton",1,100)
H=Higgs("Higgs",0,100,125)
foton.PrintInfo()
H.PrintInfo()
print("Higgs energy: "+str(H.Energy()))