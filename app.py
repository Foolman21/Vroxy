import requests
from bs4 import BeautifulSoup

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

# Parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the search results
results = soup.find_all('a', class_='result__a')

# Visit each search result
for result in results:
    # Extract the URL from the search result
    result_url = result['href']
    
    # Make the request with the proxy
    response = requests.get(result_url, proxies=proxy)
    
    # Print the response content
    print(f"\n**Visiting: {result_url}**\n")
    print(response.text)
