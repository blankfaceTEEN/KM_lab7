import numpy as np

from calculates import calculate
from profile import letters


count = 200
l = letters.get('m') + letters.get('n') + letters.get('q')
values = np.random.exponential(l, size=count)
calculate(values)
