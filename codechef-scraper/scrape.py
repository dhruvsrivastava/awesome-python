from bs4 import BeautifulSoup
from urllib2 import urlopen

id_dict = {}

#username
username = "ironmandhruv"

for year in range(2013 , 2017) :
	page = 0;
	while page < 300:

		print "current page %d" %(page)
		url = "https://www.codechef.com/submissions?page="+ str(page)+ "sort_by=All&sorting_order=asc&language=All&status=All&year="+str(year)+"&handle="+username+"&pcode=&ccode=&Submit=GO"
		try:
			url = urlopen(url)
		except urllib2.HTTPError:
			print "error "
		soup = BeautifulSoup(url)

		for link in soup.find_all('tr' , class_ = "kol"):
			child = link.find_all('td')
			for j in range(len(child)):
				print child[j].string
			if child[0].string in id_dict:
				page = 1000
				break
			else:
				id_dict[child[0].string] = 1
			
			timestamp = str(child[1].string)
			# print type(timestamp)
			data = timestamp.split(' ')
			# print data
			hours = ""
			minutes = ""
			bool_f = False
			for ch in timestamp:
				if ch == " ":
					break
				if ch == ":":
					bool_f = True
					continue
				if bool_f:
					minutes += ch
				else:
					hours += ch

			hours = int(hours)
			minutes = int(minutes)
		page += 1

	# print "%d %d" %(hours , minutes)

	# for items in child:
	# 	print items.string
	# print ""

# for link in soup.find_all('tr' , class_ = "kol"):
# 	child = link.find_all('td')
# 	print child[1].string
# 	print ""