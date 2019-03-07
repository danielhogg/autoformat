import datetime

import matplotlib.pyplot as plt
import numpy as np


def scale(start_date, end_date):

    if start_date >= end_date:
        raise ValueError("start_date must be before end_date.")

    dynamic_range = end_date - start_date

    