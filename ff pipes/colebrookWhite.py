import numpy as np
from scipy.optimize import root
from math import *
import pandas as pd
import matplotlib.pyplot as plt

excel_file = "lab3e.xlsx"

# Colebrook eq
def y(f):
    return (1 / (sqrt(f))) + 2 * log((eps/(3.7*D)) + (2.51 / (x * sqrt(f))), 10)

# Serghides eq
def ffS (Re):
    A = -2 * log10((eps/D) / 3.7 + (12 / Re))
    B = -2 * log10((eps/D) / 3.7 + ((2.51 * A) / Re))
    C = -2 * log10((eps/D) / 3.7 + ((2.51 * B) / Re))
    
    return (A - ((B - A)**2 / (A - (2 * B) + C)))**-2

# characteristics of 5 tube
c_tube = ["carbon steel 16.8mm", "acrylic pipe 12mm", "pvc 17mm", "carbon steel 22.4mm", "carbon steel 28.4mm"]
epss = [0.00004572, 0.000002, 0.0000015, 0.00004572, 0.00004572]
Diameter = [0.0168, 0.012, 0.017, 0.0224, 0.0284]
# row data
row = [2, 13, 25, 36, 47]

i = 0
for tube in c_tube:
    Re = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', skiprows=row[i], usecols='G', nrows=9))
    ff_exp = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', skiprows=row[i], usecols='H', nrows=9))
    ff = []
    D = Diameter[i]
    eps = epss[i]
    for x in Re:
        ff.append(getattr(root(y,0.002), 'x').item())
    plt.plot(Re, np.c_[ff, ff_exp], label=['colebrook ff', 'experimental ff'])
    plt.legend()
    plt.xlabel("Reynolds")
    plt.ylabel("friction factor")
    plt.title(tube)
    plt.show()

# compare friction factor of carbon steel 16.8mm by two methods
Re = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', skiprows=row[0], usecols='G', nrows=9))
ff_exp = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', skiprows=row[0], usecols='H', nrows=9))
ff = []
ffE = []
eps = epss[0]
D = Diameter[0]
for x in Re:
    ff.append(getattr(root(y,0.002), 'x').item())
    ffE.append(ffS(x))

plt.plot(Re, np.c_[ff, ffE, ff_exp], label=['Colebrook ff', 'Serghides ff', 'exp ff'])
plt.legend()
plt.xlabel("Reynolds")
plt.ylabel("friction factor")
plt.title(c_tube[0])
plt.show()



# Re = [9433.29, 14149.94, 18866.59, 23583.24, 28299.89, 35374.86, 42449.83, 47166.48, 58958.10]
# Re = [6603.31, 13206.61, 16508.27, 19809.92, 23111.58, 26413.23, 33016.54, 39619.84, 46223.15]
# Re = [9322.32, 13983.47, 18644.63, 23305.79, 27966.95, 34958.69, 46611.58, 58264.48, 65256.21]
# Re = [7074.97, 10612.46, 14149.94, 17687.43, 21224.92, 24762.40, 28299.89, 31837.38, 35374.86]
# Re = [8370.39, 11160.52, 13950.65, 20925.97, 23716.10, 27901.30, 30691.43, 34876.62, 41851.95]
