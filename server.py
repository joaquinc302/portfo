from flask import Flask, render_template, session, redirect, url_for, request
import pathlib
import csv



app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route("/<string:pagename>")
def my_page(pagename):
    return render_template(pagename)
        

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_db(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong try again.'
    
header = False

def write_to_db(data):
    with open('database.csv', 'a', newline='') as file:
        fieldnames = ['email', 'subject', 'message']
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writerow(data)
        print('Data written in database')
