import requests
from bs4 import BeautifulSoup

# Define function to handle form submission with proxy
def submit_form(url, data, proxy):
    response = requests.post(url, data=data, proxies=proxy)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if url.endswith('/search'):
        # Extract search results
        results = soup.find_all('a', class_='result__a')
        for result in results:
            # Extract title and URL
            title = result.find('h2', class_='result__title').text
            result_url = result['href']
            print(f"**Title:** {title}")
            print(f"**URL:** {result_url}")
            print('-' * 50)
    elif url.endswith('/visit'):
        # Extract website content
        content = soup.find('div', id='content')
        print(f"**Website Content:**")
        print(content)
    else:
        raise Exception(f"Unknown URL endpoint: {url}")

    return soup

# Set up the proxy
proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080',
}

# Get request method and handle accordingly
if request.method == 'GET':
    query = request.args.get('q')
    
    # Submit the form with the search query
    if query:
        data = {'q': query}
        soup = submit_form('/search', data, proxy)
    else:
        # Display the search form
        print(f"Welcome to the DuckDuckGo Proxy! Use the form below to search the web.")
elif request.method == 'POST':
    target_url = request.form.get('url')
    
    # Submit the form with the target URL
    if target_url:
        data = {'url': target_url}
        soup = submit_form('/visit', data, proxy)
    else:
        # Display the visit form
        print(f"Enter a URL to visit:")

# Handle any other requests
else:
    print(f"Unsupported request method: {request.method}")

