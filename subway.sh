#!/bin/bash

# -------------------------------------------------------------
# Script for printing departures from Forskningsparken,
# Blindern and Sinsen.
# Options: --W (westbound), --E (eastbound), Blindern, Sinsen
# >> ./subways.sh <>
# 2016 - JVS
# -------------------------------------------------------------

# Finding departure times
find_dep () {
	eval var1="$1"
	eval var2="$2"
	dep_time=${var1#*${var2}}
	dep_time=${dep_time#*"departureTime"}
	dep_time=${dep_time%%"isRemainingTime"*}
	dep_time=${dep_time:3:5}
	echo $dep_time
}

if [ $# -lt 1 ]; then
	# Find right line in webpage
	forskningsparken=$(curl -sN "https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0" | grep -m 1 "angular.module")

	sentrum=${forskningsparken##*"1 ("}
	sentrum=${sentrum%%"2 ("*}
	ringen=${forskningsparken##*"2 ("}

	# Finding departure times westbound
	bergkrystallen=$(find_dep "\${sentrum}" Bergkrystallen)
	vestliviaM=$(find_dep "\${sentrum}" Vestli)
	ringenviaM=$(find_dep "\${sentrum}" Ringen)
	# Finding departure times eastbound
	vestliviaS=$(find_dep "\${ringen}" Vestli)
	sognsvann=$(find_dep "\${ringen}" Sognsvann)
	ringenviaS=$(find_dep "\${ringen}" Ringen)
	echo "Departures from Forskningsparken"
	echo "Departures city centre:"
	echo "Bergkrystallen:        " $bergkrystallen
	echo "Vestli via Majorstuen: " $vestliviaM
	echo "Ringen via Majorstuen: " $ringenviaM
	echo "Departures eastbound:"
	echo "Vestli via Storo:      " $vestliviaS
	echo "Sognsvann:             " $sognsvann
	echo "Ringen via Storo:      " $ringenviaS
elif [ "$1" == "--W" ]; then
	forskningsparken=$(curl -sN "https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0" | grep -m 1 "angular.module")

	sentrum=${forskningsparken##*"1 ("}
	sentrum=${sentrum%%"2 ("*}
	ringen=${forskningsparken##*"2 ("}
	# Finding departure times westbound
	bergkrystallen=$(find_dep "\${sentrum}" Bergkrystallen)
	vestliviaM=$(find_dep "\${sentrum}" Vestli)
	ringenviaM=$(find_dep "\${sentrum}" Ringen)
	echo "Departures from Forskningsparken"
	echo "Departures city centre/westbound:"
	echo "Bergkrystallen:        " $bergkrystallen
	echo "Vestli via Majorstuen: " $vestliviaM
	echo "Ringen via Majorstuen: " $ringenviaM
elif [ "$1" == "--E" ]; then
	forskningsparken=$(curl -sN "https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0" | grep -m 1 "angular.module")

	sentrum=${forskningsparken##*"1 ("}
	sentrum=${sentrum%%"2 ("*}
	ringen=${forskningsparken##*"2 ("}
	# Finding departure times eastbound
	vestliviaS=$(find_dep "\${ringen}" Vestli)
	sognsvann=$(find_dep "\${ringen}" Sognsvann)
	ringenviaS=$(find_dep "\${ringen}" Ringen)
	echo "Departures from Forskningsparken"
	echo "Departures eastbound:"
	echo "Vestli via Storo: " $vestliviaS
	echo "Sognsvann:        " $sognsvann
	echo "Ringen via Storo: " $ringenviaS
elif [ "$1" == "Blindern" ]; then
	# Find right line in webpage
	blindern=$(curl -sN "https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0" | grep -m 1 "angular.module")

	sentrum=${blindern##*"1 ("}
	sentrum=${sentrum%%"2 ("*}
	ringen=${blindern##*"2 ("}

	# Finding departure times westbound
	bergkrystallen=$(find_dep "\${sentrum}" Bergkrystallen)
	vestliviaM=$(find_dep "\${sentrum}" Vestli)
	ringenviaM=$(find_dep "\${sentrum}" Ringen)
	# Finding departure times eastbound
	vestliviaS=$(find_dep "\${ringen}" Vestli)
	sognsvann=$(find_dep "\${ringen}" Sognsvann)
	ringenviaS=$(find_dep "\${ringen}" Ringen)
	echo "Departures from Blindern"
	echo "Departures city centre:"
	echo "Bergkrystallen:        " $bergkrystallen
	echo "Vestli via Majorstuen: " $vestliviaM
	echo "Ringen via Majorstuen: " $ringenviaM
	echo "Departures eastbound:"
	echo "Vestli via Storo:      " $vestliviaS
	echo "Sognsvann:             " $sognsvann
	echo "Ringen via Storo:      " $ringenviaS
elif [ "$1" == "Sinsen" ]; then
		# Find right line in webpage
	sinsen=$(curl -sN "https://ruter.no/reiseplanlegger/Stoppested/(3012100)Sinsen%20%5bT-bane%5d%20(Oslo)/Avganger/#st:1,sp:0,bp:0" | grep -m 1 "angular.module")

	storo=${sinsen##*"1 ("}
	storo=${storo%%"2 ("*}
	vestlitoyen=${sinsen##*"2 ("}

	# Finding departure times westbound
	bergkrystallen=$(find_dep "\${storo}" Bergkrystallen)
	ringenviaS=$(find_dep "\${storo}" Ringen)
	# Finding departure times eastbound
	vestli=$(find_dep "\${vestlitoyen}" Vestli)
	sognsvann=$(find_dep "\${vestlitoyen}" Sognsvann)
	echo "Departures from Sinsen"
	echo "Departures Vestli/Tøyen:"
	echo "Bergkrystallen:       " $bergkrystallen
	echo "Ringen via Storo:     " $ringenviaS
	echo "Departures Storo/Majorstuen:"
	echo "Vestli:               " $vestli
	echo "Sognsvann:            " $sognsvann
else
	echo $0 ": Check your command line arguments, takes only --E, --W, Blindern, Sinsen or nothing"
fi

