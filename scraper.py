import requests
from bs4 import BeautifulSoup

def soup(link, parser = 'html.parser'):
    '''
    functions:
        link : 'website link', 
        parser : 'html.parser' as the default argument
    Soup function will returns the "href" tags found in the web page
    '''
    class_name = 'su-list'
    request = requests.get(link).text
    soup = BeautifulSoup(request, parser)
    div_class = soup.find('div', class_name)
    anchor = div_class.find_all('a')
    return [i['href'] for i in anchor]

def getLinks(no_of_season):
    '''
    functions:
        no_of_season : takes the number of season as the input variable
    getLinks fucntion return the dictionary of seasons and their links
    '''
    seasons = dict()
    for i in range(1, no_of_season + 1):
        link = f"https://subdl.live/rick-and-morty-season-{i}-subtitles/"
        seasons[i] = dict(enumerate(soup(link), 1)) 
    return seasons