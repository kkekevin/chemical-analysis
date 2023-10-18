import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

excel_file = "Untitled.xlsx"

volum = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', usecols='A', skiprows=1))
pH = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', usecols='B', skiprows=1))


print(pH, volum)

plt.plot(volum, pH, color = "#B00B69", label = "Tilpasset modell")
plt.scatter(volum, pH, color = "hotpink", label = "Datapunkter")
plt.xlabel("volum")
plt.ylabel("pH")
plt.grid()
plt.show()
print(volum[0])
d = []
for i in range(len(volum)-2):
    dery = pH[i+1] - pH[i]
    dert = volum[i+1] - volum[i]
    dydt = dery/dert
    d.append(dydt)

print(d)

def fmax(list):
    max = list[0]
    for x in list:
        if x > max:
            max = x
    return max
print('the biggest element in the derivative is', fmax(d))