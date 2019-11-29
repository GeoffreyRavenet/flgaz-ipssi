import csv
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'max-age=300'
    response.headers['Access-Control-Allow-Origin'] = 'http://kuro.eu.pythonanywhere.com'
    return response


@app.route('/')
def home():
    '''
    function home
    '''
    return 'Bienvenue !'


@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():

    '''
    function save data
    '''

    if request.method == 'POST':
        print(request.form)
        if len(request.form['user_text']) < 281:
            dump_to_csv(request.form)
        return redirect(url_for('timeline'))

    if request.method == 'GET':
        return render_template('formulaire.html')


@app.route('/timeline', defaults={'user': None}, methods=['GET'])
@app.route('/timeline/<user>/', methods=['GET'])
def timeline(user):

    '''
    function affiche message
    '''
    gaz = parse_from_csv(user)
    return render_template('timeline.html', gaz=gaz)


def parse_from_csv(user):

    '''
    function parse csv
    '''
    gaz = []
    with open('./gazouilles.csv', 'r') as file_parce_csv:
        reader = csv.reader(file_parce_csv)
        for row in reader:
            if user is not None and user == row[0]:
                gaz.append({'user': row[0], 'text': row[1]})
            elif user is None:
                gaz.append({'user': row[0], 'text': row[1]})

    return gaz


def dump_to_csv(donnees_request):
    '''
    function ecrit csv
    '''
    donnees = [donnees_request['user-name'], donnees_request['user_text']]
    with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(donnees)
