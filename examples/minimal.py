import math
import datetime
import matplotlib.pyplot as plt
from autoformat import autoformat

def get_test_data():
    times = []
    data = []
    data2 = []
    start_time = datetime.datetime.utcnow()
    for x in range(0,240):
        next_time = start_time + datetime.timedelta(hours=x*0.25)
        times.append(next_time)
        data.append(math.cos(x / 4.0) + math.sin(x / 1.5))
        data2.append(math.exp(-x / 150.0) * math.sin(x / 3.0))
    return times, data, data2

def plot(filename):
    times, data, data2 = get_test_data()
    start = times[0]
    end = times[len(times)-1]
    autoformat.scale(start, end)
    plt.title("Sample Timeseries Plot")
    plt.plot(times, data)
    plt.plot(times, data2)
    plt.savefig(filename)
    plt.close()

plot("sample.png")
