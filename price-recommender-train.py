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

# Variables (testing purposes)

def test_ts(model):
	# Get established time series
	_ORANGE = pd.read_excel(get_directory(HARGAPANGAN_LOCATION + '/Harga Pangan - Compiled.xlsx'), skiprows=1, sheet_name='jeruk').set_index('Tanggal')
	_ORANGE.index = pd.DatetimeIndex(pd.to_datetime(_ORANGE.index, format='%d/%m/%Y'))
	_ORANGE.loc[:, 'Harga Lokal'] = _ORANGE['Harga Lokal'].replace('-', np.NaN)
	for i in range(len(_ORANGE['Harga Lokal'].index)):
		if _ORANGE.loc[_ORANGE.index[i], 'Harga Lokal'] != _ORANGE.loc[_ORANGE.index[i], 'Harga Lokal']:   # check for NaN
			_temp = np.array([])
			for j in range(-2, 3):
				if _ORANGE.loc[_ORANGE.index[i+j], 'Harga Lokal'] == _ORANGE.loc[_ORANGE.index[i+j], 'Harga Lokal']:
					_temp = np.append(_temp, _ORANGE.loc[_ORANGE.index[i+j], 'Harga Lokal'])
			_ORANGE.loc[_ORANGE.index[i], 'Harga Lokal'] = sum(_temp) / len(_temp)

	#forecast_1y = _ORANGE.values.copy()
	results_1y = _ORANGE['Harga Lokal'].values.copy() / 35000

	# Value normalisation


	for i in range(128):
		print('\r'+'Forecasting '+str(i), end='')
		_temp = model.predict(
			results_1y[
				-1 * WINDOW_SIZE:
			][np.newaxis]
		)
		results_1y = np.append(results_1y, _temp[0, 0])
	
	# Re-normalisation
	results_1y = results_1y * 35000

	fig = plt.figure(figsize=(4,3))
	plt.suptitle('One year prediction')
	plt.plot(range(len(_ORANGE['Harga Lokal'].values)), _ORANGE['Harga Lokal'].values, 'b')
	plt.plot(range(WINDOW_SIZE, len(_ORANGE['Harga Lokal'])), results_1y[:len(_ORANGE['Harga Lokal']) - WINDOW_SIZE], 'p-')
	plt.plot(range(len(_ORANGE['Harga Lokal']), len(_ORANGE['Harga Lokal']) + 128), results_1y[-128:], 'g')
	plt.show()

def main(test = False):
	# Load model from weight
	model = tf.keras.models.load_model('./model/forecast-normalised')
	
	# Model loading
	model.summary()

	if test:
		test_ts(model)
	

if __name__ == '__main__':
	main(test_env)