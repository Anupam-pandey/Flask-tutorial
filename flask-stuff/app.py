from flask import Flask

app = Flask(__name__)

@app.route('/') #accessing like http://www.google.com
def home():
    return "hello,world"
app.run()