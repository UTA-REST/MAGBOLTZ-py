import sys
import warnings
import time
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
from Magboltz import Magboltz
import numpy as np

CF4 = 1
He4 = 3
He3 = 4
Ne  = 5
Kr  = 6
Xe  = 7
CH4 = 8
ETHANE = 9
PROPANE = 10
ISOBUTANE = 11
CO2 = 12
H2 = 21
DEUTERIUM = 22
DME = 24

GASES = [np.nan, 'CF4', 'ARGON', 'HELIUM4', 'HELIUM3', 'NEON', 'KRYPTON', 'XENON', 'CH4', 'ETHANE', 'PROPANE'
         , 'ISOBUTANE', 'CO2', np.nan, 'H2O', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan
         , 'HYDROGEN', 'DEUTERIUM', np.nan, np.nan, 'DME']

Object = Magboltz()

import time
t1 =time.time()

# Set the number of gases
Object.NGAS =1
# Set the number of collisons 
Object.NMAX =1
# Set penning
Object.IPEN = 0
# Calculate the electron energy
Object.ITHRM=0
Object.EFINAL = 0.0
# Set the gas's with there given number
Object.NGASN=[4, 0, 0, 0, 0, 0]
# Set the gas fractions
Object.FRAC=[100, 0, 0, 0, 0, 0]
# Set the tempature
Object.TEMPC = float(23)
# Set the pressure
Object.TORR = 750.062
# Set the eletric field
Object.EFIELD =100
# Set the magnetic field and angle 
Object.BMAG = 90
Object.BTHETA =45

Object.Start()

t2 =time.time()

print("************************************************")
print("************************************************")
print("*****         Here are the outputs         *****")
print("************************************************ \n")
print("run time [s]= ",round(t2-t1,3))

print("Percentage of "+GASES[Xe]+" = ",  Object.FRAC[0])
#print("Gas1")
#print(str((Object.FRAC[0]))) #Gas1 Percentage
#print("Gas2")    
#print(str((Object.FRAC[1]))) #Gas2 Percentage

print("Tempature [C]         = ", Object.TEMPC)
print("Pressure [torr]       = ", Object.TORR)
print("Eletric field [V/cm]  = ", Object.EFIELD)
print("----------------------------------------------------")
print("Drift velocity [mm/mus]              = ", round((Object.WZ*1e-5),3))
print("----------------------------------------------------")
print("Drift velocity error [%]             = ", round(Object.DWZ,3))
print("----------------------------------------------------")
print("Transverse diffusion [cm**2/s]       = ", round(Object.DIFTR,3))
print("----------------------------------------------------")
print("Transverse diffusion error [%]       = ", round(Object.DFTER,3))
print("----------------------------------------------------")
print("Longitudinal diffusion [cm**2/s]     = ", round(Object.DIFLN,3))
print("----------------------------------------------------")
print("Longitudinal diffusion error [%]     = ", round(Object.DFLER,3))
print("----------------------------------------------------")
print("Transverse diffusion [mum/cm**0.5]   = ", round(Object.DTMN,3))
print("----------------------------------------------------")
print("Transverse diffusion error [%]       = ", round(Object.DFTER1,3))
print("----------------------------------------------------")
print("Longitudinal diffusion [mum/cm**0.5] = ", round(Object.DLMN,3))
print("----------------------------------------------------")
print("Longitudinal diffusion error [%]     = ", round(Object.DFLER1,3))
print("----------------------------------------------------")
print("Mean electron energy [eV]            = ", round(Object.AVE,3))
print("----------------------------------------------------")
print("Mean electron energy error [%]       = ", round(Object.DEN,3))
print("----------------------------------------------------")
print("************************************************")
print("************************************************")

