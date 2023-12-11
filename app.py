from flask import Flask, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/static/index.html')

@app.route('/proxy')
def proxy():
    # Get the URL of the website requested by the user
    url = request.args.get('url', '')
    
    # Make a request to the website
    response = requests.get(url)
    
    # Modify the response content to work as a proxy
    content = response.content
    
    return content

if __name__ == '__main__':
    app.run()
