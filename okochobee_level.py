#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urllib2

def get_lake_okochobee_level():
	url = "http://www.sfwmd.gov/sfwmd/common/images/weather/rt/rt_L.OKEE.html"
	data = urllib2.urlopen(url)
	soup = BeautifulSoup(data.read())
	level = soup.find('li').text.split('=')[1]
	as_of = soup.find('td',{'width':"25%"}).text
	
	return level,as_of

def main():
	level, as_of = get_lake_okochobee_level()
	print "Lake Okochobee level for %s is %s" % (as_of,level)
	
if __name__ == '__main__':
	main()
