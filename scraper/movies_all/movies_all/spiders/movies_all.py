import scrapy
from scrapy.loader import ItemLoader
from movies_all.items import MovieItem
import re
import random
import time
import requests
import logging


class MoviesAllScrape(scrapy.Spider):
    name = "movies_all"
    custom_settings = {
        'LOG_LEVEL': 'INFO',
    }
    

    def __init__(self):
        self.pages = [str(i) for i in range(1,11)]
        self.years_url = [str(i) for i in range(2000,2020)]
        self.uniq_data = set()

        #Preparing the monitoring of the loop
        self.start_time = time.time()
        self.num_requests = 0
        self.loaders = []

        self.headers = {"Accept-Language":"en-US, en;q=0.5"}

        self.elapsed_time = 0
    
    def start_requests(self):
        for year in self.years_url:

            for page in self.pages:
                
                request = scrapy.Request(url="https://www.imdb.com/search/title/?release_date=" + year +
                                        "&sort=num_votes,desc&page=" + page,
                                        headers=self.headers,callback=self.parse)

                
                self.num_requests = self.num_requests + 1
                self.elapsed_time = time.time() - self.start_time
                
                logging.basicConfig(format='%(asctime)s:%(levelname)s - %(message)s',level=logging.INFO)
                logging.info("Requests: {}; Frequency: {} requests/s; Year: {} - Page: {}".format(self.num_requests,self.num_requests/self.elapsed_time,year,page))
                
                yield request

    def parse(self,response):
        for movie in response.selector.xpath("//div[@class='lister-item mode-advanced']"):
            loader = ItemLoader(item=MovieItem(),selector=movie,response=response)
            movie_title = movie.xpath(".//h3[@class='lister-item-header']//a/text()").extract_first();                    

            if movie.xpath(".//div[contains(@class,'ratings-metascore')]//span") is not None:
                if movie.xpath(".//div[@class='ratings-bar']//strong") is not None:
                    if len(movie.xpath(".//p[@class='sort-num_votes-visible']/span[@name='nv']")) > 1:
                        # if movie_title not in self.uniq_data:                            loader.add_xpath('title',".//h3[@class='lister-item-header']//a")
                        loader.add_xpath('year',".//h3[@class='lister-item-header']//span[contains(@class,'lister-item-year')]")
                        loader.add_xpath('ratings',".//div[@class='ratings-bar']//strong")
                        loader.add_xpath('metascore',".//div[contains(@class,'ratings-metascore')]//span")
                        loader.add_xpath('votes',".//p[@class='sort-num_votes-visible']/span[@name='nv'][1]/@data-value")
                        loader.add_xpath('gross_income',".//p[@class='sort-num_votes-visible']/span[@name='nv'][2]/@data-value")

                        self.uniq_data.add(movie_title)
                        yield loader.load_item()
              
        
