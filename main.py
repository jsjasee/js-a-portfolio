from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About Me")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

if __name__ == '__main__':
    app.run(debug=True, port=5000)