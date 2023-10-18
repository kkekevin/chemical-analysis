import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

excel_file = "Untitled.xlsx"
#df = pd.read_excel(excel_file, sheet_name='Sheet1', usecols='A:B', skiprows=1)

#print(df)
# Sample data 
x = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', usecols='A', skiprows=1)) #Vol
y = np.array(pd.read_excel(excel_file, sheet_name='Sheet1', usecols='B', skiprows=1)) #pH
plt.plot(x, y)
plt.show()

# Define a function that calculates the squared difference between the first derivative and 0
def squared_difference(params, x, y):
    a, b = params
    first_derivative = 2 * a * x + b # Replace with the actual derivative
    return np.sum((first_derivative - 0) ** 2)

# Initial guess for the parameters (slope and intercept)
initial_guess = [1, 1]

# Use an optimization method to find the parameters that minimize the squared difference
result = minimize(squared_difference, initial_guess, args=(x, y))

# The endpoint (x-coordinate) where the derivative is closest to 0
endpoint_x = -result.x[1] / (2 * result.x[0])


print(f"Endpoint x-coordinate: {endpoint_x:.2f}")

#first derivative
y1 = []
x1 = []
for i in range(len(x)):
    if(i != 0) :
        dery = y[i] - y[i-1]
        dert = x[i] - x[i-1]
        dydt = dery/dert
        x1.append(x[i] + x[i-1] / 2)
    else :
        dydt = y[1] - y[0] / x[1] - x[0]
        x1.append(x[1] + x[0] / 2)
    y1.append(dydt)
plt.plot(x1, y1)
plt.show()

def fmax(list):
    max = list[0]
    for i in range(len(y1)):
        if(list[i] > max):
            maxIndex = i
    return x[maxIndex - 1]
print('o ponto de inflexao se encontra no volume: ', fmax(y1))

#to calcul acid concentration
molMassAcid = 60.052
densityAcid = 1.05
volOfAcid = 3 + 40
cOfAcid = (0.1 * fmax(y1)) / volOfAcid #cAcid * volAcid = cNaOH * vNaOH
c = (cOfAcid * molMassAcid) * volOfAcid / 3 #cocentration in mass / L
print(c, "g por litro. a amostra apresenta ", c/10, "%")

#second derivative
y2 = []
x2 = []
for i in range(len(x1)):
    if(i != 0) :
        dery = y1[i] - y1[i-1]
        dert = x1[i] - x1[i-1]
        dydt = dery/dert
        x2.append(x1[i] + x1[i-1] / 2)
    else :
        dydt = y1[1] - y1[0] / x1[1] - x1[0]
        x2.append(x1[1] + x1[0] / 2)
    y2.append(dydt)
plt.plot(x2, y2)
plt.show()

