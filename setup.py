from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = """# autoformat
Automatic, range-aware formatting of time-axis labels for timeseries data using matplotlib.

This package is supported for Python 3 only. This project works for time ranges on the order of milliseconds or millenia, and produces a decent-looking result with a few lines:

```python
from autoformat import autoformat

autoformat.scale(start_date, end_date)
# your matplotlib plotting code here

```

## Installation

```
pip install autoformat 
```

Project [github link](https://github.com/danielhogg/autoformat)

"""

setup(
    name='autoformat',
    version='1.0.0',
    description='Automatic, range-aware formatting of time-axis labels for timeseries data using matplotlib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/danielhogg/autoformat',
    author='Daniel Hogg',
    author_email='danielhogg@protonmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='matplotlib timeseries datetime',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.5, <4',
    install_requires=['numpy', 'matplotlib'],
)