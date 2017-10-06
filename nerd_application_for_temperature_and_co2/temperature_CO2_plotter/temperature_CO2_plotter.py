#!/usr/bin/env python3

"""
.. 	module:: temperature_CO2_plotter
	:platform: OS X
	:synopsis: Solution to 6.1, 6.4, 6.6

.. moduleauthor:: Jon Vegard Sparre

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class TemperatureCO2Plotter(object):
	'''Methods:

	- plot_temperature(ylim=None, month='January', years=None)
	- plot_CO2(ylim=None, years=None)
	- plot_CO2_by_country(threshold_l=0., threshold_u=1000., year='2012')
	- predict_future(endyear=2021, month='July')

	Usage:

	>>> from temperature_CO2_plotter import TemperatureCO2Plotter
	>>> plot = TemperatureCO2Plotter()

	Now you can use the different methods, see below.
	
	'''
	def __init__(self):
		"""Fetching path
		"""
		self.path = os.getcwd()

	def plot_CO2(self, years=None, ylim=None):
		'''

		Plot CO2 levels over time with data from data/co2.csv

		Kwargs:
			ylim 	(list):	Set limits on y-axis as a tuple (ymin,ymax)
			year	(list):	Set time interval as a list [startyear, endyear]

		Returns:
			0

		Usage:

		>>> plot = TemperatureCO2Plotter()
		>>> plot.plot_CO2()

		Then you'll get a plot over all CO2 emissions from the start of measurements until 2012.
		
		'''

		path = self.path

		df_co2  = pd.read_csv(path+'/data/co2.csv')

		if years == None:							# Setting default time period if none is given
			years = [df_co2['Year'].iloc[0], df_co2['Year'].iloc[-1]]

		df_co2.plot(x=0)
		if ylim != None:							# If limits are given we use them
			plt.ylim(ylim[0],ylim[1])
		plt.xlim(years[0],years[1])
		plt.xlabel('Year')
		plt.ylabel('CO2 level')
		plt.title('CO2 levels over time, from {} to {}'.format(int(years[0]), int(years[1])))

		return 0

	def plot_temperature(self, month='January', years=None, ylim=None):
		'''

		Plot temperature over time with data from temperature.csv
		You can choose which time interval to plot and the limits on the y-axis.

		Kwargs:
			ylim	(list):	Set limits on y-axis as a list [ymin,ymax]
			month	(str):	Set which month to plot temperatures form, default: January
			years	(list):	Set years to plot over as a list [start year, end year]
		Returns:
			0

		Usage:

		>>> plot = TemperatureCO2Plotter()
		>>> plot.plot_temperature()

		This gives a plot over temperatures in January from start of measurements until 2012
		
		'''

		path = self.path

		df_temp = pd.read_csv(path + '/data/temperature.csv')
		
		if years == None:							# Setting default time period if none is given
			years = [df_temp['Year'].iloc[0], df_temp['Year'].iloc[-1]]

		if ylim == None:							# Setting limits on y-axis if none is given
			ylim = [min(df_temp[month])-1,max(df_temp[month])+1]

		df_temp.plot(x=0,y=month)
		plt.ylim(ylim[0],ylim[1])
		plt.xlim(years[0],years[1])
		plt.title('Temperatures from {}, {} to {}'.format(month, int(years[0]), int(years[1])))
		plt.xlabel('Year')
		plt.ylabel('Temperature')

		return 0

	def plot_CO2_by_country(self, threshold_l=0., threshold_u=1000., year='2012'):
		'''

		Make a plot over emissions by each country for a given year.

		Kwargs:
			threshold_l	(float):	lower threshold value of emissions
			threshold_u	(float):	upper threshold value of emissions
			year	(str):	year to plot

		Usage:

		>>> plot = TemperatureCO2Plotter()
		>>> plot.plot_CO2_by_country()

		This gives a bar plot over emissions from all countries in 2012.

		.. 	note::
			
			The default plot will not be so very readable, we recommend setting some threshold values.
		
		'''
		path = self.path

		df = pd.read_csv(path + '/data/CO2_by_country.csv')

		# Using pandas to find all countries with emissions between chosen thresholds
		# threshold and then plotting the result
		temp = df.loc[df[year].gt(threshold_l)]
		temp.loc[df[year].lt(threshold_u)].plot(x=0, y=year, kind='bar')

		plt.title('Emissions by country between {} and {} metric tons per capita in {}'.format(threshold_l, threshold_u, year))
		plt.xlabel('Country')
		plt.ylabel('Emissions')

		return 0

	def predict_future(self, endyear=2021, month='July'):
		"""

		Predict the future by extrapolating from current dataset.

		Kwargs:
			endyear	(int):	how far into the future do you want to extrapolate?
			month(str):	for which month do you want to extrapolate?

		Returns:
			0

		Usage:

		>>> plot = TemperatureCO2Plotter()
		>>> plot.predict_future(endyear=2030, month='June')

		This gives a plot of temperature over all years with measurements
		and an extrapolation of the data into 2030.

		"""

		# Using a module from scipy to do the interpolation
		from scipy.interpolate import UnivariateSpline
		path = self.path

		temp_data 	= pd.read_csv(path + '/data/temperature.csv')
		CO2_data 	= pd.read_csv(path + '/data/CO2.csv')
		
		# No of previous 	years to take into account
		no = 10
		# Read out data from 2002-2012:
		last_years 	= temp_data.tail(no)['Year']
		last_year 	= last_years.iloc[-1]
		# Temperatures last ten years for chosen month
		temp_month	= temp_data.tail(no)[month]
		# CO2 levels last ten years
		CO2_levels	= CO2_data.tail(no)['Carbon']
		# Constant future rate of increasing CO2 emission based on the diff last two years
		CO2_diff 	= CO2_levels.iloc[-1] - CO2_levels.iloc[-2]

		# Array for extrapolating and no of years into the future
		no_years	= endyear - last_year + 1
		future		= np.linspace(last_year, endyear, no_years)
		future_CO2	= np.linspace(CO2_levels.iloc[-1], CO2_levels.iloc[-1] + (no_years-1)*CO2_diff, no_years)
		# spline order for interpolating, choosing 1 to get a linear extrapolation
		order 		= 1
		# interpolate and then using future_CO2 array to extrapolate
		s = UnivariateSpline(CO2_levels, temp_month, k=order)
		y = s(future_CO2)

		# plotting past temperatures and future temperatures (in different styles)
		temp_data.plot(x=0,y=month)
		plt.hold('on')
		plt.plot(future, y, 'r')
		plt.xlabel('Year')
		plt.ylabel('Temperature')
		plt.title('Future temperatures into {}'.format(endyear))
		plt.xlim(temp_data.head(1)['Year'].iloc[0], future[-1])

		return 0

if __name__ == '__main__':
	# Run all methods and save plot from each
	plot = TemperatureCO2Plotter()
	plot.plot_CO2()
	plt.savefig('co2.png')
	plot.plot_temperature()
	plt.savefig('temp.png')
	plot.plot_CO2_by_country()
	plt.savefig('emissions.png')
	plot.predict_future()
	plt.savefig('future.png')
	print('Saved plots as co2.png, temp.png, emissions.png, and future.png')
	#plt.show()