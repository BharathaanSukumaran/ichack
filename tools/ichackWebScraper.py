import requests
from bs4 import BeautifulSoup

def search_google(keyword):
    headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }   
    output = []
    # Make a GET request to Google to search for the keyword
    response = requests.get(f"https://www.google.com/search?q={keyword} recipe",headers=headers)
    
    # Use BeautifulSoup to parse the HTML of the response
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    
    # Find all the search result links
    result_links = soup.find_all("a")
    
    # Extract the URLs from the links and print them
    for link in result_links:
        url = link.get("href")
        url = str(url)
        if("google"not in url and "https"in url):
            output.append(url)
    
    return output[0]
        