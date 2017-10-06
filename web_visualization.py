#!/usr/bin/env python3

'''

.. 	module:: temperature_CO2_plotter
	:platform: OS X
	:synopsis: Solution to 6.2, 6.3

.. moduleauthor:: Jon Vegard Sparre

Script rendering a web page showing results from temperature_CO2_plotter.py
with interactive features to plot user defined plots of CO2 levels,
temperatures and more.

Intervals to be plotted are taken from forms on the web page.

An error page is loaded if you give wrong inputs in the forms.

Usage:

>>> python3 web_visualization.py

.. note::

	If you want to run the app open on your network, change the __main__() to
	app.run(host="0.0.0.0").

'''

from flask import Flask
from flask import render_template, request, send_from_directory, url_for, send_file, redirect
import matplotlib.pyplot as plt
from temperature_CO2_plotter import TemperatureCO2Plotter
import os

app = Flask("TemperatureCO2Plotter")

# Initializing class
plot = TemperatureCO2Plotter()

@app.route("/", methods= ["GET"])
def index_site():
	'''
	
	Rendering index site with plots generated
	on dataset.

	'''

	plot.plot_CO2()
	plt.savefig('static/co2.png')
	plot.plot_temperature()
	plt.savefig('static/temp.png')

	return render_template('index.html')

@app.route("/handle_co2", methods=['POST'])
def handle_co2():
	'''

	Make a user defined plot of CO2 levels over a chosen
	period of time.

	'''
	assert request.method == 'POST'

	filename 	= 'co2_user.png'
	headline	= 'CO2 levels over time'
	# Fetching time interval from web form
	start_year 	= int(request.form["startyear"])
	end_year   	= int(request.form["endyear"])

	try:
		# Optional to choose y-limits
		ymin = float(request.form["ymin"])
		ymax = float(request.form["ymax"])
		ylim = [ymin,ymax]
	# If something's wrong with the input an error site is rendered
	except ValueError:
		# ylim = None
		return render_template('error.html')
	
	plot.plot_CO2(years=[start_year, end_year], ylim=ylim)
	plt.savefig('fig/' + filename)
	# Clearing figure
	plt.clf()

	return render_template('plot_user.html', filename=filename, headline=headline)

@app.route("/handle_temp", methods=['POST', 'GET'])
def handle_temp():
	'''
	
	Make a user defined plot of temperatures from
	a chosen month over a chosen period of years.

	'''
	assert request.method == 'POST'

	filename 	= 'temp_user.png'
	headline	= 'Temperature over time'
	start_year 	= int(request.form["startyear"])
	end_year   	= int(request.form["endyear"])
	month	   	= str(request.form["month"])

	try:
		# Optional to choose y-limits
		ymin = float(request.form["ymin"])
		ymax = float(request.form["ymax"])
		ylim = [ymin,ymax]
	except ValueError:
		return render_template('error.html', redirection=redirection)

	plot.plot_temperature(years=[start_year, end_year], month=month, ylim=ylim)
	plt.savefig('fig/'+filename)
	plt.clf()

	return render_template('plot_user.html', filename=filename, headline=headline)

@app.route("/handle_emissions", methods=['POST'])
def handle_emissions():
	'''

	Generate a user defined plot of emission by
	countries between possibly chosen treshold values.
	
	'''
	assert request.method == 'POST'

	filename 		= 'emissions_user.png'
	headline 		= 'Emissions by country'

	try:
		year 			= str(request.form["year"])
		upper_threshold = float(request.form["upperthreshold"])
		lower_threshold = float(request.form["lowerthreshold"])
	except ValueError:
		return render_template('error.html', redirection=redirection)

	plot.plot_CO2_by_country(threshold_u=upper_threshold, threshold_l=lower_threshold, year=year)
	plt.savefig('fig/' + filename)
	plt.clf()

	return render_template('plot_user.html', filename=filename, headline=headline)

@app.route("/handle_future", methods=['POST'])
def handle_future():
	'''

	Generate a user defined plot over temperature in the future
	
	'''
	
	assert request.method == 'POST'

	filename 	= 'future_user.png'
	headline 	= 'Future temperature'
	try:
		end_year  	= int(request.form["endyear"])
		month_	 	= str(request.form["month"])
	except ValueError:
		return render_template('error.html', redirection=redirection)
	
	plot.predict_future(endyear=end_year, month=month_)
	plt.savefig('fig/' + filename)
	plt.clf()

	return render_template('plot_user.html', filename=filename, headline=headline)

# Functions sending plots and help pages when they're asked for.
@app.route("/fig/<path:filename>")
def _fig(filename):
	return send_from_directory('fig',filename)

@app.route("/<path:filename>")
def _help(filename):
	return send_from_directory('doc/_build/html',filename)

# Using a tip from Piazza so that images are not cached by the browser
@app.after_request
def _add_header(response):
    """

    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
	app.run(debug=True)