import cfscrape
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self):
        self.__scraper = cfscrape.create_scraper()
    
    def get_megasena_result(self):
        content = self.__scraper.get('https://www.google.com/search?q=caixa+mega+sena').content
        content = content
        soup = BeautifulSoup(content, "lxml")
        nums = []
        spans = soup.find_all("span", class_="zSMazd UHlKbe")
        for i in range(len(spans)):
            nums.append(spans[i].text)
        return nums