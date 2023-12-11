import requests

# Set up the proxy
proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080',
}

# Set up the DuckDuckGo search URL
url = 'https://duckduckgo.com/html/'

# Set up the search query
query = 'python proxy'

# Make the request
response = requests.get(url, params={'q': query}, proxies=proxy)

# Print the response
print(response.text)
