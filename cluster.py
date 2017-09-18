from sklearn.cluster import MeanShift, estimate_bandwidth
from db import table
import numpy

data = numpy.array([
    [device['Power']['Active'],
     device['Power']['Reactive'],
     device['Power']['Appearent'],
     device['Line']['Current'],
     device['Line']['Voltage'],
     device['Peaks'][0],
     device['Peaks'][1],
     device['Peaks'][2]
     ] for device in table])

bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=200)
ms = MeanShift(bandwidth=bandwidth, cluster_all=False, bin_seeding=True)
labels = ms.fit_predict(data)
