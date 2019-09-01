import random
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/together_with')
def success():
    str1 = "Together with "
    word=[['high number of vehicles for the roadway','increasing number of vehicles','substantial increase in the number of vehicles'],['separation of work and residential areas'],['highly connected street network'],['unsynchronized traffic signals'],['growing population'],['inadequate road infrastructure','inadequate network of roads','inadequate roads construction and maintenance','inadequate constructions, maintenance and rehabilitation of roads','inadequate street capacity','inadequate transportation system']]

    Effect = ['more delays','additional stress','the inability to estimate travel times','fuel consumption','senseless reactions such as road rage','a large volume of harmful carbon emissions']

    connection = ['which contributes to','which leads to','which results in','which gives rise to','thus contributing to','thus leading to','thus resulting in','thus giving rise to']

    group1=random.choice(word)
    c1 = random.choice(group1)

    word.remove(group1)

    group2 = random.choice(word)
    c2 = random.choice(group2)

    E1 = random.choice(Effect)
    Effect.remove(E1)
    E2 = random.choice(Effect)

    Connect = random.choice(connection)

    Snt = str1 + 'the ' + c1 + ' and ' + c2 + ' has come growing traffic congestion, ' + Connect + ' ' + E1 + ' and ' + E2 + '.'


    print (Snt)
    return Snt

@app.route('/login')
def login():
    return redirect(url_for('success'))


if __name__ == '__main__':
    app.run(debug = True)
