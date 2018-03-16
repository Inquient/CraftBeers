import numpy
from matplotlib import pyplot
from matplotlib import rcParams
import math

def sum_product(x, y):
    sum_prod = 0
    for i in range(0, len(x)):
        sum_prod += x[i] * y[i]
    return sum_prod

def sum_square(x):
    sum_sqrt = 0
    for i in range(0, len(x)):
        sum_sqrt += x[i]*x[i]
    return sum_sqrt

def mean_value(array):
    sum = 0
    for value in array:
        sum += value
    return sum/len(array)

def coefficients(x, y, x_mean, y_mean):
    a_1 = numpy.sum(y * (x - x_mean)) / numpy.sum(x * (x - x_mean))
    a_0 = y_mean - a_1 * x_mean

    reg = a_0 + a_1 * x

    return reg

year, temp_anomaly = numpy.loadtxt("1880-2018.csv", delimiter=',', skiprows=5, unpack=True)

# rcParams['font.family'] = 'serif'
# rcParams['font.size'] = 16
#
# #You can set the size of the figure by doing:
# pyplot.figure(figsize=(10,5))
#
# #Plotting
# pyplot.plot(year, temp_anomaly, color='#2929a3', linestyle='-', linewidth=1)
# pyplot.title('Land global temperature anomalies. \n')
# pyplot.xlabel('Year')
# pyplot.ylabel('Land temperature anomaly [°C]')
# pyplot.grid()
# pyplot.show()


year_mean = mean_value(year)
temp_anomaly_mean = mean_value(temp_anomaly)

pyplot.figure(figsize=(10, 5))
pyplot.plot(year, temp_anomaly, color='#2929a3', linestyle='-', linewidth=1, alpha=0.5)
pyplot.plot(year, coefficients(year, temp_anomaly, year_mean, temp_anomaly_mean),
            'k--', linewidth=2, label='Linear regression')
pyplot.xlabel('Year')
pyplot.ylabel('Land temperature anomaly [°C]')
pyplot.legend(loc='best', fontsize=15)
pyplot.grid()
# pyplot.show()

A = (sum(year)*sum(temp_anomaly)-len(year)*sum_product(year,temp_anomaly))/(sum(year)*sum(year)-len(year)*sum_square(year))
B = (sum(temp_anomaly) - A*sum(year))/len(year)
print(A, B)

fx = [A*x+B for x in year]
# print(fx)
pyplot.figure(figsize=(10, 5))
pyplot.plot(year, temp_anomaly, color='#2929a3', linestyle='-', linewidth=1, alpha=0.5)
pyplot.plot(year, fx,
            'k--', linewidth=2, label='Linear regression')
pyplot.xlabel('Year')
pyplot.ylabel('Land temperature anomaly [°C]')
pyplot.legend(loc='best', fontsize=15)
pyplot.grid()
pyplot.show()

# Для анализа нелинейной зависимости

X1 = year[0]
X2 = year[len(year)-1]
Y1 = temp_anomaly[0]
Y2 = temp_anomaly[len(temp_anomaly)-1]

Xar = (X1+X2)/2
Xgeom = math.sqrt(abs(X1*X2))
Xgarm = (2*X1*X2)/(X1+X2)

Yar = (Y1+Y2)/2
Ygeom = math.sqrt(abs(Y1*Y2))
Ygarm = (2*Y1*Y2)/(Y1+Y2)

Yar_pr = A*Xar+B
Ygeom_pr = A*Xgeom+B
Ygarm_pr = A*Xgarm+B

# Вычислим пограшности, в зависимости от того, какая из них минимальна, выберем вид аналитической зависимости, наиболее
# точно описывающий выборку

e1 = abs(Yar_pr - Yar)      # погрешность относительно линейной зависимости
e2 = abs(Yar_pr - Ygeom)    # погрешность относительно показательной зависимости
e3 = abs(Yar_pr - Ygarm)    # погрешность относительно дробно-рациональной вида y = 1/(Ax+B)
e4 = abs(Ygeom_pr - Yar)    # погрешность относительно логарифмической
e5 = abs(Ygeom_pr - Ygeom)  # погрешность относительно смешанной
e6 = abs(Ygarm_pr - Yar)    # погрешность относительно гиперболической
e7 = abs(Ygarm_pr - Ygarm)  # погрешность относительно дробно-рациональной вида y = x/(Ax+B)

e = [e1,e2,e3,e4,e5,e6,e7]
print(e, min(e))