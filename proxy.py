from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure headless Chrome
options = Options()
options.add_argument('--headless')

def search_bing(query):
  driver = webdriver.Chrome(options=options)
  
  # Open Bing search
  driver.get("https://www.bing.com/")
  
  # Enter search query
  search_bar = driver.find_element_by_class_name("b_searchbox")
  search_bar.send_keys(query)
  
  # Click search button
  search_button = driver.find_element_by_id("sb_form_go")
  search_button.click()
  
  # Get page content
  content = driver.page_source
  
  # Parse with BeautifulSoup
  soup = BeautifulSoup(content, 'html.parser')
  
  # Find first search result
  result = soup.find('li', class_='b_algo')
  
  # Extract website URL
  url = result.find('a', class_='b_title').get('href')
  
  # Close browser
  driver.quit()
  
  # Return extracted URL
  return url

def visit_website(url):
  driver = webdriver.Chrome(options=options)
  
  # Visit website
  driver.get(url)
  
  # Interact with the website
  # (modify this section based on your needs)
  # For example, click on a specific element by ID
  driver.find_element_by_id("element_id").click()
  
  # Get current page content
  content = driver.page_source
  
  # Close browser
  driver.quit()
  
  # Return page content
  return content

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    query = request.form['query']
    
    # Search Bing
    url = search_bing(query)
    
    # Visit website
    content = visit_website(url)
    
    return render_template('index.html', content=content)
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
