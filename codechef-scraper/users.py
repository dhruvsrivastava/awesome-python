from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "https://www.codechef.com/ratings/long-challenge?filterBy=Institution%3DJaypee%20Institute%20of%20Information%20Technology&itemsPerPage=40&order=asc&sortBy=global_rank"
url = urlopen(url)
soup = BeautifulSoup(url)
print soup.prettify()
for link in soup.find_all('tr' , class_ = 'ember-view'):
	print link