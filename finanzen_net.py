#!/usr/bin/env python
import re
import urllib.request
import urllib.error
import urllib.parse

# Fetch HTML code for specified bond
def fetch(bond):
	try:
		response = urllib.request.urlopen('http://www.finanzen.net/aktien/' + urllib.parse.quote(bond.replace(" ", "_")) + "-Aktie@stBoerse_XETRA")
	except urllib.error.URLError as e:
		if hasattr(e, 'reason'):
			return "ERROR: failed to reach a server! RESPONSE: " + e.reason
		elif hasattr(e, 'code'):
			return "ERROR: server failure! ERROR CODE: " + e.code
	else:
		html = response.read()
		return html

def price(html):
	if len(html) <= 100:
		return "ER:404"

	# Find the first occurance of a specified pattern
	pattern = re.compile(b'Kurs<[^>]+><[^>]+>[0-9.,]+')
	hits = pattern.findall(html)

	if len(hits) >= 1:
		# Retrieve the actual value from the hits: first number after '>', strip '>' afterwards
		pattern = re.compile('>[0-9.,+-]+')
		result = pattern.findall(hits[0].decode("utf-8"))[0][1:]
		return result
	else:
		return "ER:NONE"

def day_performance(html):
	if len(html) <= 100:
		return "ER:404"

	# Find the first occurance of a specified pattern
	pattern = re.compile(b'Kurs<[^>]+><[^>]+>[0-9.,]+[^%]+%')
	hits = pattern.findall(html)

	if len(hits) >= 1:
		# Retrieve the actual value from the hits: first number after '>', strip '>' afterwards
		pattern = re.compile('[0-9.,+-]+')
		result = pattern.findall(hits[0].decode("utf-8"))[-1]
		return result
	else:
		return "ER:NONE"

def predicted_target(html):
	if len(html) <= 100:
		return "ER:404"

	# Find the first occurance of a specified pattern
	pattern = re.compile(b'Kursziel: <strong>[0-9.,]+?</strong>')
	hits = pattern.findall(html)

	if len(hits) >= 1:
		# Retrieve the actual value from the hits
		pattern = re.compile('[0-9.,+-]+')
		result = pattern.findall(hits[0].decode("utf-8"))[0]
		return result
	else:
		return "NONE"


def predicted_performance(html):
	if len(html) <= 100:
		return "ER:404"

	# Find the first occurance of a specified pattern
	pattern = re.compile(b'Kursziel: <strong>[^%<]+?%<')
	hits = pattern.findall(html)

	if len(hits) >= 1:
		# Retrieve the actual value from the hits
		pattern = re.compile('[0-9.,+-]+')
		result = pattern.findall(hits[0].decode("utf-8"))[0]
		return result
	else:
		return "NONE"
