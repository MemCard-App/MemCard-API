import urllib.request
from bs4 import BeautifulSoup


def find_meaning(word):

    url = "https://www.vocabulary.com/dictionary/" + word + ""
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')

    notworking = False

    soup1 = soup.find(class_="short")

    try:
        soup1 = soup1.get_text()
    except AttributeError:
        notworking = True

    # Print short meaning

    if notworking is False:
        return soup1
    else:
        return "The meaning of this word was not found :(. Maybe try editing the spelling? :)"
