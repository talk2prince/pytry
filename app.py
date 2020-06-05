from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('res1.html')


app.run(port = 5000)
