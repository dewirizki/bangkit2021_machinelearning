import tensorflow as tf
import pandas as pd
import os
import numpy as np
from pathlib import PurePosixPath, PureWindowsPath
from matplotlib import pyplot as plt

# Functions
def get_directory(path):
    if os.name == 'posix':
        return str(PurePosixPath(path))
    else:
        return str(PureWindowsPath(path))

# Constants
HARGAPANGAN_LOCATION = get_directory('./dataset/time-series')
WINDOW_SIZE = 128
TEST_ENV = False

class PriceForecast(object):
	def __init__(self, model, time_series):
		self._model = model
		self._time_series = time_series
	
