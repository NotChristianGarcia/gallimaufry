"""
Flop test for Abaco. Reads in a string message of "'std_deviation' 'size'" from
Abaco. Does some cool multi-threaded math and outputs total time to completion.
"""
import os
import time

#threads, std_dev, size = map(int, os.environ.get('MSG').split())
threads, std_dev, size = map(int, "0 1000 8000".split())

if threads:
    os.environ["OMP_NUM_THREADS"] = str(threads)

import numpy
whole_start = time.time()
A = numpy.random.normal(0, std_dev, (size, size))
B = numpy.random.normal(0, std_dev, (size, size))

calc_start = time.time()
C = numpy.dot(A, B)

end = time.time()

print(end - whole_start, end - calc_start)