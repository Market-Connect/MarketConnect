from flask import Flask, render_template, request, redirect, url_for
import json, random
import smtplib


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


#email SMTP
def sendMail(email):
    sender_email = "senders_address"
    reciever_email = email
    password = "password"
    message = "Hi, Thanks for reaching out!"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, password)
    print("sucess")

    server.sendmail(sender_email, reciever_email, message)
    print("enail sent")





@app.route('/')
def landing():
    return render_template('LandingPage.html')


@app.route('/login')
def login():
    return render_template('loginPage.html')

@app.route('/signupCustomer')
def signupCustomer():
    return render_template('signup-Customer.html')

@app.route('/contact', methods=["GET", "POST"] )
def contact():
    if request.method == 'POST':
        x = request.form['email_input']
        sendMail(x)
    return render_template('contactus.html')


@app.route('/customer')
def customer():
    links = getLinks()
    return render_template('customerHome.html', links = links)


if __name__ == "__main__":
    app.run(debug=True)

