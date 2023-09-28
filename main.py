from flask import Flask, render_template, request, redirect, url_for
import json, random

app = Flask(__name__)


def getLinks():
    links = []
    with open('static/imageData.json') as f:  
        data = json.load(f)
        links = data 
    return links



@app.route('/')
def landing():
	return render_template('LandingPage.html')


@app.route('/login')
def login():
	return render_template('loginPage.html')


@app.route('/contact')
def contact():
	return render_template('contactus.html')


@app.route('/customer', methods=["GET", "POST"])
def customer():
	links = getLinks()
	return render_template('customerHome.html', links = links)


if __name__ == "__main__":
	app.run(debug=True)