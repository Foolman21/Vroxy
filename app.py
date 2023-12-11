from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def search(query):
    """
    Sends a search query to DuckDuckGo through the proxy and extracts results.
    """
    try:
        # Set proxy details
        proxy = {
            "http": "http://127.0.0.1:8080",
            "https": "https://127.0.0.1:8080",
        }

        # Send search request
        response = requests.post(
            f"https://duckduckgo.com/search", data={"q": query}, proxies=proxy
        )
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract search results
        results = []
        for result in soup.find_all("a", class_="result__a"):
            title = result.find("h2", class_="result__title").text
            url = result["href"]
            results.append({"title": title, "url": url})

        return results
    except Exception as e:
        return []

def visit(url):
    """
    Visits the target URL and extracts website content.
    """
    try:
        # Set proxy details
        proxy = {
            "http": "http://127.0.0.1:8080",
            "https": "https://127.0.0.1:8080",
        }

        # Send visit request
        response = requests.get(url, proxies=proxy)
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract website content
        content = soup.find("div", id="content")

        return content
    except Exception as e:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles search and visit requests.
    """
    if request.method == "GET":
        query = request.args.get("q")
        results = []
        if query:
            results = search(query)
        return render_template("index.html", results=results)
    else:
        target_url = request.form.get("url")
        content = None
        if target_url:
            content = visit(target_url)
        return render_template("visit.html", content=content)

@app.errorhandler(Exception)
def handle_error(error):
    """
    Handles and displays error messages.
    """
    return render_template("error.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
