import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exponential_function(x, a, b, c):
    return a * np.exp(b * x) + c

#namerena data pro voltamperove charakteristiky
x_data = np.array([-6, -5, -4, -3, -2, -1, 0, 0.1, 0.2, 0.3, 0.4])
y_data = np.array([-88, -74, -58, -41, -27, -13, 0, 4, 20, 74, 233])

x_data1 = np.array([-6, -5, -4, -3, -2, -1, 0, 0.1, 0.2, 0.3, 0.4])
y_data1 = np.array([-106, -87, -71, -53, -36, -21, -5, 0, 16, 73, 233])

params, covariance = curve_fit(exponential_function, x_data, y_data)

params1, covariance = curve_fit(exponential_function, x_data1, y_data1)

a_fit, b_fit, c_fit = params

a_fit1, b_fit1, c_fit1 = params1

#data pro graficke urceni primky
x1, y1 = -2, 0
x2, y2 = 0, -200

m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1
x_values = np.linspace(-7, 0.5, 100)
y_values = m * x_values + b

x_fit = np.linspace(-7, 0.5, 1000)
y_fit = exponential_function(x_fit, a_fit, b_fit, c_fit)

x_fit1 = np.linspace(-7, 0.5, 1000)
y_fit1 = exponential_function(x_fit1, a_fit1, b_fit1, c_fit1)

#namerena experimentalni data
x_data2 = np.array([-1.45, -1.38, -1.36, -1.5, -1.6])
y_data2 = np.array([-50.4, -57.9, -59.4, -45.9, -34.3])
coefficients = np.polyfit(x_data2, y_data2, 1)
poly_function = np.poly1d(coefficients)

x_fit2 = np.linspace(-7, 0.5, 100)
y_fit2 = poly_function(x_fit2)

plt.scatter(x_data2, y_data2, label='Naměřené experimentální hodnoty', color='blue')
plt.plot(x_fit2, y_fit2, label='Experimentální zatěžovací přímka', color='blue')

plt.plot(x_values, y_values, label='Grafická zatěžovací přímka', color='black')
plt.scatter([x1, x2], [y1, y2], color='black')

plt.scatter(x_data, y_data, label='Naměřené hodnoty pro E = 0 ', color='red')
plt.plot(x_fit, y_fit, label='Nafitovaná funkce pro E = 0', color='red')

plt.scatter(x_data1, y_data1, label='Naměřené hodnoty pro E > 0', color='green')
plt.plot(x_fit1, y_fit1, label='Nafitovaná funkce pro E > 0', color='green')

plt.xlabel('U[V]')
plt.ylabel('I[μA]')
plt.legend()
plt.title('Voltampérové charakteristiky')
plt.grid(True)
plt.axvline(x=0, color='black', linestyle='-', label='x=0')  
plt.axhline(y=0, color='black', linestyle='-', label='y=0')  

plt.show()