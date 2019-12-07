from flask import Flask, render_template
import csv
from jsonify_menu import generate_menu

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/specials')
def specials():
    with open('./scrape/lunch_specials.csv', 'r') as f:
        specials = csv.DictReader(f)
        return render_template('specials.html', specials=specials)


@app.route('/menu')
def menu():
    full_menu = generate_menu()
    print(full_menu)
    return render_template('menu.html', menu=full_menu)


if __name__ == '__main__':
    app.run(debug=True)
