from bs4 import BeautifulSoup
from urllib2 import urlopen , HTTPError

id_dict = {}

#username
username = "ironmandhruv"
all_submissions = 0
filename = username + ".txt"

file = open(filename , "w")

for year in range(2013 , 2017) :
	page = 0;
	submission_count = {}
	while page < 300:

		print "current page %d" %(page)
		url = "https://www.codechef.com/submissions?page="+ str(page)+ "sort_by=All&sorting_order=asc&language=All&status=All&year="+str(year)+"&handle="+username+"&pcode=&ccode=&Submit=GO"
		connected = False
		while not connected:
			try:
				url = urlopen(url)
				connected = True
			except HTTPError:
				print "error "
		soup = BeautifulSoup(url)

		for link in soup.find_all('tr' , class_ = "kol"):

			child = link.find_all('td')

			if len(child) == 0:
				continue

			# for j in range(len(child)):
				# file.write(str(child[j].string) + " ")
				# print child[j].string
			# file.write("\n")
			# print child[0].string
			if child[0].string in id_dict:		#id already found ie last page has been scraped
				page = 1000
				break
			else:
				all_submissions += 1
				id_dict[child[0].string] = 1

			if len(child) == 1:
				continue

			timestamp = child[1].string
			timestamp = timestamp.split(' ')
			timestamp = timestamp[2]
			# print timestamp

			if str(timestamp) == "ago":
				continue

			#date is of the format 03/04/16
			submission_month = int(timestamp[3]) * 10 + int(timestamp[4])
			print submission_month
			if submission_month not in submission_count:
				submission_count[submission_month] = 0
			submission_count[submission_month] += 1
		page += 1
	file.write(str(year) + "\n")
	for month in range(1 , 13):
		if month in submission_count:
			file.write(str(submission_count[month]) + " ")
		else:
			file.write("0 ")
	file.write("\n")



print "All submissions %d" %(all_submissions)

			# hours = ""
			# minutes = ""
			# bool_f = False
			# for ch in timestamp:
			# 	if ch == " ":
			# 		break
			# 	if ch == ":":
			# 		bool_f = True
			# 		continue
			# 	if bool_f:
			# 		minutes += ch
			# 	else:
			# 		hours += ch

			# if str(minutes) == "hours":
			# 	continue
			# hours = int(hours)
			# minutes = int(minutes)
