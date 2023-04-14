from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/hairdresser")
def hairdresser():
    return render_template("hairdresser.html")

if __name__ == "__main__":
    app.run(use_reloader=True )
