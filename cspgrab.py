#!/usr/bin/python3

# help users on implementing content-security-policy header or identifying
# list of external sources the website calls out to using pure python.
import requests
import argparse
import re
from bs4 import BeautifulSoup


def scraper(input_url):		
	browser = requests.session()
	response = browser.get(input_url[0])

	print('\nReturning all external sources by type..\n')

	# decode byte to string object
	decoded = response.content.decode('utf-8')
	soup = BeautifulSoup(decoded, 'html.parser')

	ext_sources = {
		'href':[],
		'script': [],
		'stylesheets': [],
		'img': [],
		'connect': [],
		'font': [],
		'object': [],
		'media': [],
		'frame': [],
		'form': [],
		}

	# href
	for eachhref in soup.find_all('a', attrs={'href': re.compile('^http.*$')}):
		href = eachhref.get('href')
		ext_sources['href'].append(href)
	# script
	for eachscript in soup.find_all('script', attrs={'src': re.compile('^http.*$')}):
		script = eachscript.get('src')
		ext_sources['script'].append(script)
	# stylesheet
	for eachsheet in soup.find_all('stylesheet', attrs={'src': re.compile('^http.*$')}):
		stylesheet = eachsheet.get('src')
		ext_sources['stylesheet'].append(stylesheet)
	# img
	for eachimg in soup.find_all('img', attrs={'src': re.compile('^http.*$')}):
		img = eachimg.get('src')
		ext_sources['img'].append(img)
	# font
	for eachfont in soup.find_all('font', attrs={'src': re.compile('^http.*$')}):
		font = eachfont.get('src')
		ext_sources['font'].append(font)
	# frame/iframe
	for eachframe in soup.find_all(re.compile('^.frame$'), attrs={'src': re.compile('^http.*$')}):
		frame = eachframe.get('src')
		ext_sources['frame'].append(frame)
	# media -- video
	# form
	for eachform in soup.find_all('form', attrs={'action': re.compile('^http.*$')}):
		form = eachform.get('action')
		ext_sources['form'].append(form)
	

	for key,val in ext_sources.iteritems():
		if not val:
			val.append('No external source(s) for this type exists on this webpage')
	return(ext_sources)

def urlarg():
	parser = argparse.ArgumentParser(description='Content-Security-Policy header implementation guide',
		epilog='Example:$ python3 cspgrab.py https://docs.python.org')
	parser.add_argument('-u', nargs=1, required=True, type=str, 
		help='please type in url (http or https) for data scraping')
	arg = parser.parse_args()
	return arg.u


def main():
	url = urlarg()
	print('\nurl parsing complete')
	print(scraper(url))


if __name__ == "__main__":
	main()