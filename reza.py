import requests
from bs4 import BeautifulSoup


def textschreiber(endstring):
    if not endstring:
        return
    url = "https://www.ikiwiki.de/eintrag.aspx?Kategorie=fragen&Element={}".format(endstring)
    screen = requests.get(url)

    soup = BeautifulSoup(screen.content , 'html.parser')
    found = soup.find_all("span","LangDe")

    writer.write('----Frage:{}----\n'.format(endstring))
    for aussage in found:
            writer.write(aussage.text+'\n')


    found = soup.find_all("div", "ergFbRight")
    richtig = found[0].find_all('img')
    writer.write('----Antwort:-----\n')
    for aussage in richtig:
        if(aussage.get('title')):
            print(aussage.get('title'))
            writer.write(aussage.get('title')+'\n')
 
with open('fragen.txt', 'w') as writer:
    fragen = open('fragen-short.txt')
    for frage in fragen:
        print(frage.strip())
        textschreiber(frage.strip())

