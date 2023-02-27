
import scraper
import requests
import re
import contractions

def format_file(seasons):
    '''
    functions:
        seasons : gets episodes in each season as dictionary
    
    Creates txt file for analysis
    '''
    for season in seasons.keys():
        for ep in seasons[season].keys():           
            response = requests.get(seasons[season][ep]).text
            txt = re.sub('\d{2}:.+','',response)
            txt = re.sub('(\\r\\n){2}\d*\\r\\n', '', txt) 
            txt = re.sub('Sync & corrections by XhmikosR www.addic7ed.com', '', txt)
            txt = re.sub('Corrections by XhmikosR www.addic7ed.com', '', txt)
            expanded_words = []   
            for word in txt.split():
                expanded_words.append(contractions.fix(word))
            expanded_text = ' '.join(expanded_words)
            directory = r"C:\Users\AMD\Documents\GitHub\Rick and Morty\data" # delete this later
            with open(f'{directory}\season-{season}-ep-{ep}-txt.csv', 'w', encoding="utf-8") as f:
                f.write(expanded_text)
                f.close()

no_of_season = 4
seasons = scraper.getLinks(no_of_season)
format_file(seasons) 