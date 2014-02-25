import sys
import numpy.random

size = 100

try:
    size = int(sys.argv[1])
except IndexError:
    pass
except ValueError:
    sys.exit()

for i in numpy.random.randint(size, size=size):
    print i