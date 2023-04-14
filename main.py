from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home_page.html')

@app.route("/registracija", methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route("/prijava")
def login():
    return render_template('login.html')

@app.route("/statenis")
def statenis():
    return render_template('statenis.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/o statenis")
def about():
    return render_template('about.html')

@app.route("/kontakt", methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(use_reloader=True )
