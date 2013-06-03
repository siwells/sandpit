import urllib2
from BeautifulSoup import BeautifulSoup

base_url = "http://scholar.google.co.uk/citations?"
link = "&"
lang = "en"
lang_str = "&hl=" + lang
user = "NJ4EZFwAAAAJ"
user_str = "user="+user

url = base_url + lang_str + link + user_str

page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

table = soup.find(id="stats")

citations = 0
hindex = 0
i10 = 0

for idx, row in enumerate(table.findAll('tr')[1:]):
    cols = row.findAll('td')
    if idx == 0:
        citations = "".join(cols[1].contents)
    elif idx == 1:
        hindex = "".join(cols[1].contents)
    elif idx == 2:
         i10 = "".join(cols[1].contents)

print citations, hindex, i10
