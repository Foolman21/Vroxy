from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

DUCKDUCKGO_URL = "https://duckduckgo.com/html/?q="

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        search_term = request.form.get("search_term")
        url = DUCKDUCKGO_URL + search_term
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        results = []
        for result in soup.find_all("div", class_="result"):
            title = result.find("a").text
            link = result.find("a")["href"]
            results.append({"title": title, "link": link})
        return render_template("results.html", search_term=search_term, results=results)

if __name__ == "__main__":
    app.run(debug=True)
