from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapemars
import os

app = Flask (__name__)

client = pymongo.MongoClient()
db= client.mars_db
collection = db.mars_collection


@app.route("/")
def index():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict= mars_dict)


@app.route ("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape_mars_news()
    mars_dict.update({},mars_data,upset = True)
    return redirect ("/", code = 302)

if __name__=="__main__":
    app.run(debug = True)