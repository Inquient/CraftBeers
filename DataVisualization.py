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

beers.hist(column='abv', edgecolor='white')
pyplot.boxplot(abv, labels=["Содержание алкоголя, %"])
pyplot.boxplot(ibu, labels=["Индекс горечи"])
pyplot.show()

print(numpy.percentile(abv, q=0), numpy.percentile(ibu, q=0))

