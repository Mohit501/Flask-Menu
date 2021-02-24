from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def Menu():
    return render_template('Menu.html')

@app.route('/Information')
def Information():
    return render_template('Information.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)