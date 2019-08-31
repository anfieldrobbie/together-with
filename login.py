from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('login.html')

@app.route('/together_with')
def success():
    return 'Together with A and B '

@app.route('/login')
def login():
    return redirect(url_for('success'))

if __name__ == '__main__':
    app.run(debug = True)
