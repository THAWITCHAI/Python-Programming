from flask import Flask, render_template,url_for

app = Flask(__name__)

my_contacts = [
    {'id':1,'name':'thawitchai'},
    {'id':2,'name':'thawitchai'},
    {'id':3,'name':'thawitchai'},
    {'id':4,'name':'thawitchai'},
    {'id':5,'name':'Pam Pam'},
]

@app.route('/')
def index():
    return render_template('index.html',tltle='Thawitchai')

@app.route('/contacts')
def contact():
    return render_template('contact.html', contacts=my_contacts, tltle='Contacts')

if __name__ == '__main__':
  app.run(debug=True)