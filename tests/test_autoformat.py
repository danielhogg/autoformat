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
        plt.close()


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
    test_time_period(datetime.timedelta(seconds=60), "../tests/0_1min.png")
    test_time_period(datetime.timedelta(seconds=60*30), "../tests/1_30min.png")
    test_time_period(datetime.timedelta(seconds=60*60), "../tests/2_1hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*3), "../tests/3_3hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*6), "../tests/4_6hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*12), "../tests/5_12hour.png")
    test_time_period(datetime.timedelta(seconds=60*60*24), "../tests/6_24hour.png")
    test_time_period(datetime.timedelta(days=3), "../tests/7_3day.png")
    test_time_period(datetime.timedelta(days=7), "../tests/8_7day.png")
    test_time_period(datetime.timedelta(days=14), "../tests/9_14day.png")
    test_time_period(datetime.timedelta(days=30), "../tests/10_30day.png")
    test_time_period(datetime.timedelta(days=30*3), "../tests/11_3month.png")
    test_time_period(datetime.timedelta(days=30*6), "../tests/12_6month.png")
    test_time_period(datetime.timedelta(days=365), "../tests/13_1year.png")
    test_time_period(datetime.timedelta(days=365*3), "../tests/14_3year.png")
    test_time_period(datetime.timedelta(days=365*5), "../tests/15_5year.png")
    test_time_period(datetime.timedelta(days=365*10), "../tests/16_10year.png")
    test_time_period(datetime.timedelta(days=365*25), "../tests/17_25year.png")
    test_time_period(datetime.timedelta(days=365*50), "../tests/18_50year.png")
    test_time_period(datetime.timedelta(days=365*100), "../tests/19_100year.png")
    test_time_period(datetime.timedelta(days=365*250), "../tests/20_250year.png")
    test_time_period(datetime.timedelta(days=365*500), "../tests/21_500year.png")
    test_time_period(datetime.timedelta(days=365*1000), "../tests/22_1000year.png")
    test_time_period(datetime.timedelta(days=365*3000), "../tests/23_3000year.png")

test_all()