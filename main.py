from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('LandingPage.html')


@app.route('/login')
def login():
	return render_template('loginPage.html')


@app.route('/contact')
def contact():
	return render_template('contactus.html')


if __name__ == "__main__":
	app.run(debug=True)