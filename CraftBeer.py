import numpy
import pandas
from matplotlib import pyplot
from matplotlib import rcParams

# Находит процент отсутствующих значений в выборке
def missing_values(array):
    values = array.dropna().values
    return 1-(len(values)/len(array))

# Вычисляет дисперсию выборки
def sample_var(array):
    mean = numpy.mean(array)

    sum_sqr = numpy.sum([(a - mean)**2 for a in array])

    N = len(array)
    var = sum_sqr / (N - 1)

    return var

# Вычисляет среднее квадратичное отклонение выборки
def sample_std(array):
    return numpy.sqrt(sample_var(array))


def std_percentages(x, x_mean, x_std):
    """ Computes the percentage of coverage at 1std, 2std and 3std from the
    mean value of a certain variable x.

    Arguments
    ---------
    x      : array, data we want to compute on.
    x_mean : float, mean value of x array.
    x_std  : float, standard deviation of x array.

    Returns
    -------

    per_std_1 : float, percentage of values within 1 standard deviation.
    per_std_2 : float, percentage of values within 2 standard deviations.
    per_std_3 : float, percentage of values within 3 standard deviations.
    """

    std_1 = x_std
    std_2 = 2 * x_std
    std_3 = 3 * x_std

    elem_std_1 = (((x_mean - std_1) < x) & (x < (x_mean + std_1))).sum()
    per_std_1 = elem_std_1 * 100 / len(x)

    elem_std_2 = (((x_mean - std_2) < x) & (x < (x_mean + std_2))).sum()
    per_std_2 = elem_std_2 * 100 / len(x)

    elem_std_3 = (((x_mean - std_3) < x) & (x < (x_mean + std_3))).sum()
    per_std_3 = elem_std_3 * 100 / len(x)

    return per_std_1, per_std_2, per_std_3

beers = pandas.read_csv("beers.csv")

abv = beers["abv"].dropna().values
ibu = beers["ibu"].dropna().values

print("Процент потерянных данных в массиве рейтингов пива {:.4f}".format(missing_values(beers["ibu"])))
print("Среднее квадратичное отклонение для процента алкоголя {:.4f} и рейтинга пива {:.4f}".format(sample_std(abv), sample_std(ibu)))


rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

abv_mean = numpy.mean(abv)
abv_std = sample_std(abv)
ibu_mean = numpy.mean(ibu)
ibu_std = sample_std(ibu)

abv_std1_per, abv_std2_per, abv_std3_per = std_percentages(abv, abv_mean, abv_std)
print('The percentage of coverage at 1 std of the abv_mean is : {:.2f} %'.format(abv_std1_per))
print('The percentage of coverage at 2 std of the abv_mean is : {:.2f} %'.format(abv_std2_per))
print('The percentage of coverage at 3 std of the abv_mean is : {:.2f} %'.format(abv_std3_per))

ibu_std1_per, ibu_std2_per, ibu_std3_per = std_percentages(ibu, ibu_mean, ibu_std)
print('The percentage of coverage at 1 std of the ibu_mean is : {:.2f} %'.format(ibu_std1_per))
print('The percentage of coverage at 2 std of the ibu_mean is : {:.2f} %'.format(ibu_std2_per))
print('The percentage of coverage at 3 std of the ibu_mean is : {:.2f} %'.format(ibu_std3_per))

# Строим график распределения содержания алкоголя в пиве
pyplot.figure(figsize=(10,5))
pyplot.axvline(abv_mean, 0, color='r', label='x mean')
pyplot.axvline(abv_mean + abv_std, 0, color='g', ls='--')
pyplot.axvline(abv_mean - abv_std, 0, color='g', ls='--')
pyplot.axvline(abv_mean + 2*abv_std, 0, color='g', ls='-.')
pyplot.axvline(abv_mean - 2*abv_std, 0, color='g', ls='-.')
pyplot.axvline(abv_mean + 3*abv_std, 0, color='g', ls=':')
pyplot.axvline(abv_mean - 3*abv_std, 0, color='g', ls=':')
pyplot.hist(abv, bins=20, color='#3498db', histtype='bar', edgecolor='white')
pyplot.title('abv \n')
pyplot.xlabel('Alcohol by Volume (abv) ')
pyplot.ylabel('Frequency')

# Строим график распределения рейтинга пива
pyplot.figure(figsize=(10,5))
pyplot.axvline(ibu_mean, 0, color='r')
pyplot.axvline(ibu_mean + ibu_std, 0, color='g', ls='--')
pyplot.axvline(ibu_mean - ibu_std, 0, color='g', ls='--')
pyplot.axvline(ibu_mean + 2*ibu_std, 0, color='g', ls='-.')
pyplot.axvline(ibu_mean - 2*ibu_std, 0, color='g', ls='-.')
pyplot.axvline(ibu_mean + 3*ibu_std, 0, color='g', ls=':')
pyplot.axvline(ibu_mean - 3*ibu_std, 0, color='g', ls=':')
pyplot.hist(ibu, bins=20, color='#e67e22', histtype='bar', edgecolor='white')
pyplot.title('ibu \n')
pyplot.xlabel('International Bittering Units (ibu)')
pyplot.ylabel('Frequency')
pyplot.show()