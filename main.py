import requests
import time
from bs4 import BeautifulSoup

url = 'https://www.capitalethiopia.com/'
response = requests.get(url)
content = response.content
def scrape_data(content):

  soup = BeautifulSoup(content, 'html.parser')
  titles = soup.find_all("div", class_="col-md-4 col-sm-6 col-xs-6 simple")
  articles = soup.find_all("article")
  
  
  for article in articles:
   image_tag = article.find("img")
   image_url = image_tag["src"] if image_tag else "Image URL not found"
    
   text_tag = article.find("h3", itemprop="name").find("a")
   text = text_tag.text.strip() if text_tag else "Text not found"

   


   base_url = 'https://api.telegram.org/bot6342347387:AAEWK6_qJ21dTaYCY-Zbgie_fiY2D1DUCjo/sendMessage?chat_id=878856703&text='
   message = f"{text}\nImage URL: {image_url}"
   requests.get(base_url + message)
# time.sleep(10)
   print(text)
   print(image_url)
scrape_data(content)
 