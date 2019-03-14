import math
import datetime
import matplotlib.pyplot as plt
from autoformat import autoformat

def get_test_data():
    times = []
    data = []
    start_time = datetime.datetime.utcnow()
    for x in range(0,20):
        next_time = start_time + datetime.timedelta(hours=x)
        times.append(next_time)
        data.append(math.cos(x / 10.0))
    return times, data

def plot(filename):
    times, data = get_test_data()
    start = times[0]
    end = times[len(times)-1]
    autoformat.scale(start, end)
    plt.plot(times, data)
    plt.savefig(filename)
    plt.close()

plot("sample.png")
