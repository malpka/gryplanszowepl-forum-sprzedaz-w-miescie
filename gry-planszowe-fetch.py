import urllib.request
import sys
from bs4 import BeautifulSoup  

quote_page = "http://www.gry-planszowe.pl/forum/viewforum.php?f=53" #
post_max_range = 2501
post_download_limit = 5
debug = 0 


post_number = 0
for i in range(0, post_max_range, 50):
    quote_page_start = quote_page + '&start=' + str(i)
    if debug == 1:
        print (quote_page_start)

    with urllib.request.urlopen(quote_page_start) as url:
        s = url.read()
    soup = BeautifulSoup(s, "html.parser")

    print("title;url;nick;location")

    for pagecontent in soup.find_all(id="pagecontent"):
        correcttable = pagecontent.find_all("table")[1]

        for link in correcttable.find_all("a", "topictitle"):
            post_title = link.text.replace(";",",")
            quote_page2 = "http://www.gry-planszowe.pl/forum/" + link['href'][2:]
            with urllib.request.urlopen(quote_page2) as url:
                s2 = url.read()
            if debug == 1:
                print(quote_page2)
            soup = BeautifulSoup(s2, "html.parser")
            author = soup.find("b", "postauthor")
            details = soup.find("span", "postdetails")
            pos_localisation = details.text.find("Lokalizacja: ")
            if pos_localisation != -1:
                localisation = details.text[13 + pos_localisation:].rstrip()
                print(post_title + ';' + quote_page2 + ';' + author.text + ';' + localisation)
                if post_number >= post_download_limit or debug == 1:
                    sys.exit()
                post_number += 1
