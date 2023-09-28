from flask import Flask, render_template, request, redirect, url_for
import json, random

app = Flask(__name__)



def getLinks():
    accessed_indices = set()
    with open('static/imageData.json') as f:
        data = json.load(f)

    choice = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    total_items = len(data)
    items = []
    
    while len(items) < 9:
        random_index = random.choice(choice)
        if random_index not in accessed_indices:
            accessed_indices.add(random_index)
            items.append(data[random_index])
    
    return items


@app.route('/')
def landing():
    return render_template('LandingPage.html')


@app.route('/login')
def login():
    return render_template('loginPage.html')

@app.route('/signupCustomer')
def signupCustomer():
    return render_template('signup-Customer.html')

@app.route('/signupMerchant')
def signupMerchant():
    return render_template('signup-merchant.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')

@app.route('/Home')
def Home():
    return render_template('LandingPage.html')

@app.route('/customer', methods=["GET", "POST"])
def customer():
    links = getLinks()
    return render_template('customerHome.html', links = links)


if __name__ == "__main__":
    app.run(debug=True)