import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


def scale(start_date, end_date):

    if start_date >= end_date:
        raise ValueError("start_date must be before end_date.")

    dynamic_range = end_date - start_date
    total_seconds = dynamic_range.total_seconds()
    total_hours = total_seconds / 3600

    fig, ax = plt.subplots()

    majorLoc = mdates.AutoDateLocator()
    minorFormat = None
    minorLoc = None
    majorFormat = None
    xlabel = None

    
    if total_hours < 1:
        pass
    elif total_hours < 6:
        majorFormat = mdates.DateFormatter("%H:%M")
    elif total_hours < 12:
        majorFormat = mdates.DateFormatter("%Hh")
    elif total_hours <= 24 * 7:
        majorFormat = mdates.DateFormatter("%b %d")
        minorFormat = mdates.DateFormatter("%H")
        minorLoc = majorLoc
        majorLoc = mdates.DayLocator()
        fig.autofmt_xdate()
    elif total_hours < 24 * 7 * 4:
        majorFormat = mdates.DateFormatter("%b %d")
        majorLoc = mdates.DayLocator()
        fig.autofmt_xdate()
    else:
        pass
        # Currently out of scope


    if majorLoc is not None:
        ax.xaxis.set_major_locator(majorLoc)

    if majorFormat is not None:
        ax.xaxis.set_major_formatter(majorFormat)

    if minorLoc is not None:
        ax.xaxis.set_minor_locator(minorLoc)

    if minorFormat is not None:
        ax.xaxis.set_minor_formatter(minorFormat)

    if xlabel is not None:
        plt.xlabel(xlabel)

