import numpy
import pandas
from matplotlib import pyplot

#Import rcParams to set font styles
from matplotlib import rcParams

#Set font style and size
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

# Load the beers data set using pandas, and assign it to a dataframe
beers = pandas.read_csv("beers.csv")

abv = beers["abv"].dropna().values
ibu = beers["ibu"].dropna().values

var_abv = numpy.var(abv, ddof=1)
std_abv = numpy.sqrt(var_abv)
# def_std_abv = numpy.std(abv, ddof=1)
# print(std_abv, def_std_abv)

var_ibu = numpy.var(ibu, ddof=1)
std_ibu = numpy.sqrt(var_ibu)
# def_std_ibu = numpy.std(ibu, ddof=1)
# print(std_ibu, def_std_ibu)

print("Значение медианы - {:.4f}; и Среднее значение{:.4f}".format(numpy.median(abv), numpy.mean(abv)))
print("Значение медианы - {:.4f}; и Среднее значение{:.4f}".format(numpy.median(ibu), numpy.mean(ibu)))

# beers.hist(column='abv', edgecolor='white')
# pyplot.show()

# pyplot.boxplot(abv, labels=["Содержание алкоголя, %"])
# pyplot.show()
#
# pyplot.boxplot(ibu, labels=["Индекс горечи"])
# pyplot.show()

print("Первый квартиль для abv {} и ibu {}".format(numpy.percentile(abv, q=25), numpy.percentile(ibu, q=25)))
print("Второй квартиль для abv {} и ibu {}".format(numpy.percentile(abv, q=50), numpy.percentile(ibu, q=50)))
print("Третий квартиль для abv {} и ibu {}".format(numpy.percentile(abv, q=75), numpy.percentile(ibu, q=75)))

# Визуализируем качественные данные

style_series = beers['style']
style_counts = style_series.value_counts() # Расчитывает количество повторов одного элемента в массиве
style_counts[0:20].plot.barh(figsize=(10,8), color='#008367', edgecolor='gray')
pyplot.show()

# Совместная визуализация различных данных

beers_clean = beers.dropna() # Очищаем данные от потерянных значений
abv = beers_clean['abv'].values
ibu = beers_clean['ibu'].values

pyplot.figure(figsize=(8,8))
pyplot.scatter(abv, ibu, color='#3498db')
pyplot.title('Scatter plot of alcohol-by-volume vs. IBU \n')
pyplot.xlabel('abv')
pyplot.ylabel('IBU')
pyplot.show()

