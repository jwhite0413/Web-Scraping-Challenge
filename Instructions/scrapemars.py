from splinter import Browser
from bs4 import BeautifulSoup
import pandas as  pd
import requests
import pymongo

def init_browser():
    executable_path = {"execeutable_path": "chromedriver.exe"}
    return Browser ("chrome", **executable_path, headless = False)

def scrape():
    Browser = init_browser()
    mars_dict = {}

    news_url = 'https//mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    news_soup = BeautifulSoup(html,'html.parser')
    news_title = news_soup.find_all('div', class_ = 'content_title')[0].text
    news_p = news_soup.find_all('div', class_ ='article_teaser_body')[0].text
       
    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "fact_table": str(mars_html_table),
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_dict