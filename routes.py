from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/specials')
def specials():
    with open('./scrape/lunch_specials.csv', 'r') as f:
        specials = csv.DictReader(f)
        return render_template('specials.html', specials=specials)

if __name__ == '__main__':
    app.run(debug=True)