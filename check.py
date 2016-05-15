#!/usr/bin/env python
import finanzen_net
import signal
import sys

DAX = ['adidas', 'Allianz', 'BASF', 'BAYER', 'Beiersdorf', 'BMW', 'Commerzbank',
	'Continental', 'Daimler', 'Deutsche Bank', 'Deutsche Boerse', 'Deutsche Post',
	'Deutsche Telekom', 'E.ON', 'Fresenius', 'Fresenius Medical Care', 'HeidelBergCement',
	'Henkel vz', 'Infineon', 'Linde', 'Lufthansa', 'Merck', 'Muenchener Rueck',
	'ProSiebenSat1 Media', 'RWE', 'SAP', 'Siemens', 'thyssenkrupp', 'Volkswagen VZ', 'Vonovia']

MDAX = ['Aareal Bank', 'Airbus', 'alstria office REIT-AG', 'Aurubis', 'Axel Springer',
	'Bilfinger', 'Brenntag', 'Covestro', 'CTS Eventim', 'Deutsche Euroshop',
	'Deutsche Wohnen', 'Deutsche-Pfandbriefbank', 'DMG MORI', 'Duerr', 'Evonik',
	'Fielmann', 'Fraport', 'FUCHS PETROLUB vz', 'GEA Group', 'Gerresheimer',
	'Hannover Rueck', 'Hella', 'HOCHTIEF', 'HUGO BOSS', 'Jungheinrich', 'K+S',
	'Kion', 'KRONES', 'KUKA', 'LANXESS', 'LEG Immobilien', 'LEONI', 'METRO',
	'MTU Aero Engines', 'NORMA Group', 'OSRAM', 'Rheinmetall', 'RHOEN-KLINIKUM', 'RTL Group',
	'Salzgitter', 'Stada', 'Steinhoff International', 'Stroeer SE', 'Suedzucker',
	'Symrise', 'TAG Immobilien', 'Talanx', 'WACKER CHEMIE', 'Wincor Nixdorf', 'Zalando']

TECDAX = ['ADVA Optical Networking SE', 'Aixtron', 'Bechtle', 'Cancom',
	'Carl Zeiss Meditec', 'CompuGroup Medical', 'Dialog Semiconductor',
	'Draegerwerk', 'Drillisch', 'Evotec', 'Freenet', 'GFT Technologies',
	'Jenoptik', 'MorphoSys', 'Nemetschek', 'Nordex',
	'Pfeiffer Vacuum', 'Qiagen', 'RIB Software', 'Sartorius',
	'Siltronic', 'SLM Solutions Group', 'SMA Solar Technology', 'Software',
	'Stratec Biomedical', 'SUeSS MicroTec', 'Telefónica Deutschland',
	'United Internet', 'Wirecard', 'XING']

class bcolors:
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	BGGREEN = '\033[42m'
	RED = '\033[91m'
	BGRED = '\033[41m'

def signal_handler(signal, frame):
	print(bcolors.RED + ' exiting...' + bcolors.ENDC)
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def color_sign(string_with_sign):
	if string_with_sign[:1] == "+":
		return bcolors.GREEN + string_with_sign + bcolors.ENDC
	else:
		return bcolors.RED + string_with_sign + bcolors.ENDC

def print_stock_table_row(stock):
	html = finanzen_net.fetch(stock)
	print("{:25}\t{:6}\t{:20}\t{:6} ({})".format(stock, \
		finanzen_net.price(html),                       \
		color_sign(finanzen_net.day_performance(html)), \
		finanzen_net.predicted_target(html),            \
		color_sign(finanzen_net.predicted_performance(html))))

print(bcolors.BOLD + "TECDAX:\n{:25}\t{:6}\t{:8}\t{:6} ({}) in EUR".format("Aktie", "Kurs", "Day Perf. (%)", "Kursziel", "Target (%)") + bcolors.ENDC)
for stock in TECDAX:
	print_stock_table_row(stock)

print(bcolors.BOLD + "\nMDAX\n{:25}\t{:6}\t{:8}\t{:6} ({}) in EUR".format("Aktie", "Kurs", "Day Perf.", "Kursziel", "in %") + bcolors.ENDC)
for stock in MDAX:
	print_stock_table_row(stock)

print(bcolors.BOLD + "\nDAX\n{:25}\t{:6}\t{:8}\t{:6} ({}) in EUR".format("Aktie", "Kurs", "Day Perf.", "Kursziel", "in %") + bcolors.ENDC)
for stock in DAX:
	print_stock_table_row(stock)
