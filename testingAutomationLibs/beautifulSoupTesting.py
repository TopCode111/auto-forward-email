import bs4 as bs

import urllib

sauce = urllib.urlopen('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# Display the entire HTML source code of the page
print(soup) 

# Parse for the sourse/sauce title
print(soup.title)

# Parse for the sourse/sauce title - remove the <title></title> tags from the result
print(soup.title.string)

#Parse for the first paragraph element in the page
print(soup.p.text)

#Parse for all paragraph elements in the page
print(soup.find_all('p'))

#Parse for all URL's in the page
for url in soup.find_all('a'):
	print(url)

#Parse for all URL's (only links without tags) in the page
for url in soup.find_all('a'):
	print(url.get('href'))

#Parse for all tables
table = soup.table
table_rows = table.find_all('tr')
for tr in table_rows:
	td=tr.find_all('td')
	row = [i.text for i in td]
	print(row)

form = soup.input;
print(form)
