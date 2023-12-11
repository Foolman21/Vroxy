from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q")
    
    # Use DuckDuckGo's API to perform the search
    url = f"https://api.duckduckgo.com/?q={query}"
    response = requests.get(url)
    data = response.json()

    # Extract and format search results
    results = []
    for result in data["results"]:
        title = result["FirstURL"]
        description = result["Text"]
        results.append(f"<h3><a href='/visit?url={title}'>{title}</a></h3><p>{description}</p>")

    # Return search results in HTML format
    return f"""
        <h1>DuckDuckGo Proxy</h1>
        <p>Search results for "{query}"</p>
        <hr>
        {"".join(results)}
    """

@app.route("/visit")
def visit():
    url = request.args.get("url")

    # Fetch the content of the requested URL
    response = requests.get(url)
    content = response.content

    # Parse the content as HTML
    soup = BeautifulSoup(content, "lxml")

    # Replace all external resources with proxied versions
    for img in soup.find_all("img"):
        # Replace image src with a proxy URL
        img["src"] = f"/proxy_image?url={img['src']}"

    # Return the proxied HTML content
    return soup.prettify()

@app.route("/proxy_image")
def proxy_image():
    image_url = request.args.get("url")

    # Fetch the image content
    image_response = requests.get(image_url)
    image_content = image_response.content

    # Return the image content directly
    return image_content

if __name__ == "__main__":
    app.run(debug=True)
