from flask import Flask, render_template, url_for

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index2.html')

@application.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@application.route('/login')
def login():
    return render_template('login.html')

@application.route('/register')
def register():
    return render_template('registration.html')

if __name__ == '__main__':
    application.run(debug=True)
