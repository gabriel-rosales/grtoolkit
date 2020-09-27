import requests
from bs4 import BeautifulSoup, NavigableString
# from grtoolkit.Storage import loadPickle, savePickle
from grtoolkit.Storage import Pickle

def goodreads_scraper(author, page_num=None):
    ### SOURCE: https://soniajoseph.github.io/goodreads-scraper/
    ### If pagenum=None, then it will return all results.

	# old_author = author
	author = author.replace(" ", "+")
	all_quotes = []

	# if page number not specified, get true page number
	if page_num is None:
		try:
			page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=1" + "&q=" + author + "&utf8=%E2%9C%93")
			soup = BeautifulSoup(page.text, 'html.parser')
			pages = soup.find(class_="smallText").text
			a = pages.find("of ")
			page_num = pages[a+3:]
			page_num = page_num.replace(",", "").replace("\n", "")
			page_num = int(page_num)
			print("looking through", page_num, "pages")
		except:
			page_num = 1

	# for each page
	for i in range(1, page_num+1, 1):
		try:
			page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" + str(i) + "&q=" + author + "&utf8=%E2%9C%93")
			soup = BeautifulSoup(page.text, 'html.parser')
			print("scraping page", i)
		except:
			print("could not connect to goodreads")
			break
			
		try:
			quote = soup.find(class_="leftContainer")
			quote_list = quote.find_all(class_="quoteDetails")
		except:
			pass

		# get data for each quote
		for quote in quote_list:
			meta_data = []
			# Get quote's text
			try:
				outer = quote.find(class_="quoteText")
				inner_text = [element for element in outer if isinstance(element, NavigableString)]
				inner_text = [x.replace("\n", "") for x in inner_text]
				final_quote = "\n".join(inner_text[:-4])
				meta_data.append(final_quote.strip())
			except:
				pass 

			# Get quote's author
			try:
				author = quote.find(class_="authorOrTitle").text
				author = author.replace(",", "")
				# author = author.replace("\n", "")
				meta_data.append(author.strip())
				# print(author)
			except:
				meta_data.append(None)

			# Get quote's book title
			try: 
				title = quote.find(class_="authorOrTitle")
				title = title.nextSibling.nextSibling.text
				# title = title.replace("\n", "")
				meta_data.append(title.strip())
				# print(title)
			except:
				meta_data.append(None)

			# Get quote's tags
			try:
				tags = quote.find(class_="greyText smallText left").text
				tags = [x.strip() for x in tags.split(',')]
				tags = tags[1:]
				meta_data.append(tags)
				# print(tags)
			except:
				meta_data.append(None)

			# Get number of likes
			try:
				likes = quote.find(class_="right").text
				likes = likes.replace("likes", "")
				likes = int(likes)
				meta_data.append(likes)
				# print(likes)
			except:
				meta_data.append(None)
			all_quotes.append(meta_data)

		# for text, author, title, tags, likes in all_quotes:
		# 	print(text)
		# 	print(author)
		# 	print(title)
		# 	print(tags)
		# 	print(likes)
		# 	print()
	return all_quotes

def generateDB(author, page_num=None, saveFile=None):
	db = goodreads_scraper(author, page_num)
	if saveFile != None:
		try:
			p = Pickle(saveFile)
			p.save(db)
			# savePickle(saveFile,db)
		except:
			print("Error saving pickle...")
	return db

def loadDB(pickleFile):
	p = Pickle(pickleFile)
	p.load()
	# return loadPickle(pickleFile)
	return p.contents

def bookTitles(db):
	titles = []
	for quote in db:
		if quote[2] not in titles:
			titles.append(quote[2])
	return titles

def filterQuotesByBook(db, book, min_likes=0):
    by_book = list()
    for quote in db:
        if quote[2] == book:
            if quote[4] >= min_likes:
                by_book.append(quote[0])
    return by_book

def export(quotes, saveFile, enc):
	from grtoolkit.Storage import File
	save = File(saveFile, enc=enc)

	for i in range(0,len(quotes)):
		if i == 1:
			save.write(quotes[i][1:-1])
			save.append("\n")
		else:
			save.append(quotes[i][1:-1],newline=False)
			save.append("\n")




if __name__ == "__main__":
    generateDB("jk rowling", 1)

