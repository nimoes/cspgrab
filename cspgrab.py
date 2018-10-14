#!/usr/bin/python3

# help users on implementing content-security-policy header or identifying
# list of external sources the website calls out to using pure python.
import requests
import argparse
from bs4 import BeautifulSoup



def scraper(input_url):		
	browser = requests.session()
	response = browser.get(input_url[0])

	if not (response.status_code == 200):
		print('Status code other than 200. Processing..')
	else:
		print('Web page processing..')

	# decode byte to string object
	decoded = response.content.decode('utf-8')
	soup = BeautifulSoup(decoded, 'html.parser')

	# href
	href_list = soup.find_all(name=['a', 'link'], href=True)
	href = [item['href'] for item in href_list]
	# src
	src_list = soup.find_all(['font', 'iframe', 'img', 'input', 'script'], src=True)
	src = [item['src'] for item in src_list]
	
	return{'href':href, 'src':src}


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
	data = scraper(url)
	print(data)
	# return "scraper fcn completed"

if __name__ == "__main__":
	main()