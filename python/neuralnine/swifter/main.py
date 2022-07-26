# From https://www.youtube.com/watch?v=UpZf1uIo1M4
# cd <to here>
# conda create --name swifter python=3.7
# conda activate swifter
# pip install -r requirements.txt
# Activate the python kernel in your session

# Swifter should help optimize when/how to split jobs across threads for pandas dataframes
# It looks at Pandas apply, swifter apply, and dask apply to determine which is faster
# then, in the background it does that one. See swifter github for more info.
# https://github.com/jmcarpenter2/swifter

import pandas as pd
import pandas_datareader as web
import datetime as dt
import time

start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()

df = web.DataReader("GS", "yahoo", start, end)

def slow_function(row):
    time.sleep(0.001)
    return row

t1 = time.time()
df['Close'].iloc[:1000].apply(slow_function)
t2 = time.time()

print(f'Time to do the slow function without swifter {t2-t1}')

import swifter


t1 = time.time()
df['Close'].iloc[:1000].swifter.apply(slow_function)
t2 = time.time()

print(f'Time to do the slow function with swifter {t2-t1}')

from decimal import Decimal
import math

# Neuralnine showed the same with a factorial function, but I must
# have transcribed it wrong because mine throws errors.
# t1 = time.time()
# df['Close'].iloc[:1000].apply(lambda x: Decimal(math.factorial(int(x*50))))
# t2 = time.time()
# print(f'Time to do the factorial without swifter {t2-t1}')

# t1 = time.time()
# df['Close'].iloc[:1000].swifter.apply(lambda x: Decimal(math.factorial(int(x*50))))
# t2 = time.time()
# print(f'Time to do the factorial with swifter {t2-t1}')

t1 = time.time()
df['Close'].iloc[:1000].apply(lambda x: x**2)
t2 = time.time()
print(f'Time to do the square without swifter {t2-t1}')

t1 = time.time()
df['Close'].iloc[:1000].swifter.apply(lambda x: x**2)
t2 = time.time()
print(f'Time to do the square with swifter {t2-t1}')