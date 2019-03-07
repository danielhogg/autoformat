# autoformat
Automatic, range-aware formatting of time-axis labels for timeseries data using matplotlib.

This package is supported for Python 3 only. This project works for time ranges on the order of milliseconds or millenia, and produces a decent-looking result with two lines:

import autoformat
autoformat.scale(start_date, end_date)
