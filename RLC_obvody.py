import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Sample x and y coordinates (replace these with your own data)
x_data =[0, 0.8, 1.6, 2.4, 3.2, 5.6, 7.2, 8.8, 9.6, 10.6, 11.2, 12.8, 15.2, 18]
y_data = [-3.5, -2.6, -0.3, 0.8, 1.7, 3, 3.5, 3.8, 2.8, 0.8, -0.3, -1.7, -2.8, -3.5]

coefficients = np.polyfit(x_data, y_data, 5)
poly_function = np.poly1d(coefficients)

x_fit = np.linspace(0, 20, 40)
y_fit = poly_function(x_fit)

#plt.scatter(x_data, y_data, label='Naměřené experimentální hodnoty', color='green')
#plt.plot(x_fit, y_fit, label='1 perioda nafitované funkce', color='blue')

x_data1 =[0, 0.8, 1.6, 2.4, 3.2, 5.6, 7.2, 8.8, 9.6, 10.6, 11.2, 12.8, 15.2, 18]
y_data1 = [0.0, 1.9, 3.9, 5.8, 7.7, 13.2, 16.9, 20.4, 22.2, 24.4, 25.7, 29.1, 34.1, 39.8]

coefficients = np.polyfit(x_data1, y_data1, 5)
poly_function1 = np.poly1d(coefficients)

x_fit1 = np.linspace(0, 20, 40)
y_fit1 = poly_function1(x_fit1)

plt.scatter(x_data1, y_data1, label='Vypočtené hodnoty', color='green')
plt.plot(x_fit1, y_fit1, label='Nafitované funkce', color='blue')

plt.xlabel('t[μs]')
plt.ylabel('I[mA]')
plt.legend()
plt.title('Analytické řešení')
plt.grid(True)
plt.axvline(x=0, color='black', linestyle='-', label='x=0')  
plt.axhline(y=0, color='black', linestyle='-', label='y=0')  

plt.show()




