import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x_data =[0, 4, 6, 9, 15, 23, 33, 39, 48, 60]
y_data = [8.9, 8.6, 8.4, 8.2, 8, 7.8, 7.75, 7.7, 7.65, 7.6]

coefficients = np.polyfit(x_data, y_data, 5)
poly_function = np.poly1d(coefficients)

x_fit = np.linspace(0, 60, 120)
y_fit = poly_function(x_fit)

plt.scatter(x_data, y_data, label='Naměřené experimentální hodnoty', color='green')
#plt.plot(x_fit, y_fit, label='1 perioda nafitované funkce', color='blue')

x_data1 =[]
y_data1 = []

E=9
R=47000
C=0.00022
Rv=200000
Dt=3
t=0
Q=C*E

while t<=60:
    I1=(-Q/C+E)/R
    I2=Q/C/Rv
    Dq = (I1-I2)*Dt
    UV = Rv*I2
    x_data1.append(t)
    y_data1.append(UV)
    t=t+Dt
    Q=Q+Dq

coefficients = np.polyfit(x_data1, y_data1, 5)
poly_function1 = np.poly1d(coefficients)

x_fit1 = np.linspace(0, 20, 40)
y_fit1 = poly_function1(x_fit1)

plt.scatter(x_data1, y_data1, label='Vypočtené hodnoty', color='blue')
#plt.plot(x_fit1, y_fit1, label='Nafitované funkce', color='blue')

plt.xlabel('t[s]')
plt.ylabel('U[V]')
plt.legend()
plt.title('Analytické řešení')
plt.grid(True)
plt.axvline(x=0, color='black', linestyle='-', label='x=0')  
plt.axhline(y=0, color='black', linestyle='-', label='y=0')  

plt.show()