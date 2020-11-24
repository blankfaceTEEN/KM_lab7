from calculates import calculate
from scipy.stats import binom
from profile import letters


count = 200
p = (5 * letters.get('m') + 5 * letters.get('n') + 10) / 100
n = 2 + letters.get('m') + letters.get('n')
values = binom.rvs(n, p, size=count)
calculate(values)

