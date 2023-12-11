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

# Parse the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the search results
results = soup.find_all('a', class_='result__a')

# Visit the first search result
first_result = results[0]
first_result_url = first_result['href']

# Make the request to the first search result
response = requests.get(first_result_url, proxies=proxy)

# Print the response
print(response.text)
