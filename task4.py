import numpy as np

from calculates import calculate
from profile import letters


count = 100
a = letters.get('m')
sigma = letters.get('n') + 1
values = np.random.normal(a, sigma, size=count)
calculate(values)
