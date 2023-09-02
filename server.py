from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)

def write_data_file(data):
    with open('./database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', '+a') as database:  # You will need 'wb' mode in Python 2.x
        writer = csv.DictWriter(database, data.keys())
        writer.writerow(data)      

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Sorry, couldn't save to database."
    else:
        return 'Oops something went wrong!'