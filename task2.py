from calculates import calculate
from profile import letters

import numpy as np

count = 200
n = letters.get('m') + 4
x = [1, 2, 3, 4, 5]
p = [0.04 * letters.get('a'), 0.1 * letters.get('b'), 0.02 * letters.get('g') + 0.03 * letters.get('m'),
     0.01 * letters.get('n') + 0.04 * letters.get('q'),
     1 - (0.04 * letters.get('a')
          + 0.1 * letters.get('b')
          + 0.02 * letters.get('g')
          + 0.03 * letters.get('m')
          + 0.01 * letters.get('n')
          + 0.04 * letters.get('q'))]
print(p)
values = np.random.choice(x, count, p=p)
calculate(values)

