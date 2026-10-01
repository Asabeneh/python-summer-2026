from flask import Flask 
from utils.utils import fetch_data, minifiy_data


url = 'https://studies.cs.helsinki.fi/restcountries/api/all'
data = fetch_data(url)
minified_data = minifiy_data(data)

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<div>

<h1> Welcome to Web Development</h1>
<p>I love web, do you ?</p>
</div>

'''

@app.route('/api/v1')
def api():
    return minified_data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)
