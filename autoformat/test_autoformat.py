import math
import datetime

import pytest
import matplotlib.pyplot as plt
import numpy as np

import autoformat


class SampleData:

    def __init__(self, start, end, n):
        # TODO: Make something better like a cosine plus noise

        self.data = np.random.random_sample(n)
        time_delta = end - start
        seconds = time_delta.total_seconds()
        increment = seconds / (n - 1)
        times_list = []

        for x in range(0, n):
            frac = (math.pi * float(x)) / float(n)
            self.data[x] = self.data[x]/10.0 + math.cos(frac) 

        for x in range(0, n):
            new_time = start + datetime.timedelta(seconds=int((increment * x)))
            times_list.append(new_time)

        self.times = np.array(times_list)

    def plot(self, filename):
        plt.plot(self.times, self.data)
        plt.savefig(filename)


def test_same_dates():
    start = datetime.datetime(2015,12,10,12)
    end = datetime.datetime(2015,12,10,12)

    autoformat.scale(start, end)

def test_wrong_order():
    start = datetime.datetime(2015,12,10,12)
    end = datetime.datetime(2015,11,10,12)

    autoformat.scale(start, end)

def test_time_period(time_span, filename):
    start = datetime.datetime(2015,12,10,12)
    end = start + time_span
    autoformat.scale(start, end)
    sample = SampleData(start, end, 100)
    sample.plot(filename)


def test_all():
    test_time_period(datetime.timedelta(seconds=60), "../tests/1min.png")
    test_time_period(datetime.timedelta(seconds=60*30), "../tests/30min.png")
    test_time_period(datetime.timedelta(seconds=60*60), "../tests/1hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*3), "../tests/3hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*6), "../tests/6hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*12), "../tests/12hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*24), "../tests/24hour.png")
    test_time_period(datetime.timedelta(days=3), "../tests/3day.png")
    test_time_period(datetime.timedelta(days=7), "../tests/7day.png")
    test_time_period(datetime.timedelta(days=14), "../tests/14day.png")
    test_time_period(datetime.timedelta(days=30), "../tests/30day.png")
    test_time_period(datetime.timedelta(days=30*3), "../tests/3month.png")
    test_time_period(datetime.timedelta(days=30*6), "../tests/6month.png")
    test_time_period(datetime.timedelta(days=365), "../tests/1year.png")
    test_time_period(datetime.timedelta(days=365*3), "../tests/3year.png")
    test_time_period(datetime.timedelta(days=365*5), "../tests/5year.png")
    test_time_period(datetime.timedelta(days=365*10), "../tests/10year.png")
    test_time_period(datetime.timedelta(days=365*25), "../tests/25year.png")
    test_time_period(datetime.timedelta(days=365*50), "../tests/50year.png")
    test_time_period(datetime.timedelta(days=365*100), "../tests/100year.png")
    test_time_period(datetime.timedelta(days=365*250), "../tests/250year.png")
    test_time_period(datetime.timedelta(days=365*500), "../tests/500year.png")
    test_time_period(datetime.timedelta(days=365*1000), "../tests/1000year.png")
    test_time_period(datetime.timedelta(days=365*3000), "../tests/3000year.png")

test_all()