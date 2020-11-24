import numpy as np

from calculates import calculate
from profile import letters


count = 200
p = 0.08 * letters.get('m') + 0.02 * letters.get('n')
n = 30 + 1 + letters.get('n')
values = np.random.poisson(n * p, count)
calculate(values)

