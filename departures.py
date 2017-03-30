#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script printing out depature times for chosen stop
in Oslo and Akershus.

Usage:
>>> departuretimes.py

@ JVS 2017
'''
from urllib.request import urlopen
import json
import sys

start = input('Stoppested: ')

def fetchdata(departure):
    linje = departure['MonitoredVehicleJourney']['LineRef']
    dest  = departure['MonitoredVehicleJourney']['DestinationName']
    tid   = departure['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime'][-14:-9]
    platf = departure['MonitoredVehicleJourney']['MonitoredCall']['DeparturePlatformName']
    dest2 = departure['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay']
    opr = departure['MonitoredVehicleJourney']['OperatorRef']
    drc   = departure['MonitoredVehicleJourney']['DirectionName']
    return linje,dest,tid,platf,dest2,drc,opr

stops = urlopen('http://reisapi.ruter.no/Place/GetStopsRuter')
stops_ = stops.read()
encoding = stops.info().get_content_charset('utf8')
stopdict = json.loads(stops_.decode(encoding))
startID = []
for element in stopdict:
    if start in element['Name']:
        startID.append([str(element['ID']),element['Name']])

if len(startID) == 0:
    print('Ooops, I didn´t manage to find {}! Remember that I´m cae sensitive.'.format(start))

for stop in startID:
    file = urlopen('http://reisapi.ruter.no/StopVisit/GetDepartures/'+stop[0]+'?')
    data = file.read()
    encoding = file.info().get_content_charset('utf8')
    data = json.loads(data.decode(encoding))
    drc_1 = []
    drc_2 = []
    for departure in data[0:6]:
        linje = departure['MonitoredVehicleJourney']['LineRef']
        dest  = departure['MonitoredVehicleJourney']['DestinationName']
        tid   = departure['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime'][-14:-9]
        platf = departure['MonitoredVehicleJourney']['MonitoredCall']['DeparturePlatformName']
        dest2 = departure['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay']
        opr   = departure['MonitoredVehicleJourney']['OperatorRef']
        drc   = departure['MonitoredVehicleJourney']['DirectionName']
        if drc == '1':
            drc_1.append('Linje {} til {}: {} kjører fra plattform {} ({})'.format(linje,dest,tid,platf,opr))
        elif drc == '2':
            drc_2.append('Linje {} til {}: {} kjører fra plattform {} ({})'.format(linje,dest,tid,platf,opr))
    print(stop[1])
    for departure in drc_1:
        print(departure)
    for departure in drc_2:
        print(departure)