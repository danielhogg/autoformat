import datetime

import pytest
import matplotlib.pyplot as pyplot
import numpy as np

import autoformat


class SampleData:

    def __init__(self, start, end, n):
        # TODO: Make something better like a cosine plus noise

        self.data = np.random.random_sample(n)
        time_delta = end - start
        seconds = time_delta.seconds
        increment = seconds / n
        times_list = []
        for x in range(0, n):
            new_time = start + datetime.timedelta(seconds=increment*x)
            times_list.append(times_list)

        self.times = np.array(times_list)

    def plot(self):

        plt.plot(self.times, self.data)
        plt.show()

def test_same_dates():
    start = datetime.datetime(2015,12,10,12)
    end = datetime.datetime(2015,12,10,12)

    autoformat.scale(start, end)

def test_wrong_order():
    start = datetime.datetime(2015,12,10,12)
    end = datetime.datetime(2015,11,10,12)

    autoformat.scale(start, end)

def test_3_days():
    start = datetime.datetime(2015,12,10,12)
    end = datetime.datetime(2015,12,13,12)

    autoformat.scale(start, end)
    sample = SampleData(start, end, 100)
    sample.plot()


test_same_dates()