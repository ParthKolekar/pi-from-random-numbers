#!/usr/bin/env python3

import random
import math
from sys import maxsize

TRIALS = 1000000

pi = math.sqrt(6 * TRIALS / sum([(math.gcd(random.randint(1, maxsize), random.randint(1, maxsize)) == 1) for _ in range(TRIALS)]))

print("Pi : {}".format(pi))
