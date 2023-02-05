import requests
from bs4 import BeautifulSoup


def amazon_alert():
    link = input("Enter amazon link:  ")
    whished_prize = int(input("Whats your whised prize?:  "))
    web_scraping_class = "a-offscreen"

    # Make a request to the website
    response = requests.get(link).text

    # Parse the HTML of the page
    soup = BeautifulSoup(response, 'html.parser')

    # Find all elements with the class "s-prose js-post-body"
    try:
        element = soup.find('span', {"class": web_scraping_class})
        element = element.get_text()
    except:
        print("Oops! Something went wrong. Please try again!")
    print(element)


amazon_alert()
