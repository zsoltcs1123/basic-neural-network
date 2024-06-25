import os

import matplotlib.pyplot
import numpy

os.makedirs("output", exist_ok=True)

a = numpy.zeros([3, 2])

a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12

matplotlib.pyplot.imshow(a, interpolation="nearest")
matplotlib.pyplot.savefig("output/samplePlot.png")
