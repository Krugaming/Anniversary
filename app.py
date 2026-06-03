from flask import Flask, render_template
from config import SITE_CONFIG

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', config=SITE_CONFIG)

if __name__ == '__main__':
    app.run(debug=True, port=5000)