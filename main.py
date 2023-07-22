import requests
from bs4 import BeautifulSoup

url = 'https://www.booksiteethiopia.com'
response = requests.get(url)
content = response.content

def scrape_data(html_code):
    soup = BeautifulSoup(html_code, "html.parser")
    articles = soup.find_all("li", attrs={"class":"product"})

    for article in articles:
        image_tag = article.find("img")
        image_url = image_tag["src"] if image_tag else "Image URL not found"

        text_tag = article.find("h2",attrs={"class":"woocommerce-loop-product__title"})
        text = text_tag.text.strip() if text_tag else "Text not found"

        base_url = 'https://api.telegram.org/bot6342347387:AAEWK6_qJ21dTaYCY-Zbgie_fiY2D1DUCjo/sendMessage?chat_id=-1001940209421&text='+text+image_url
        requests.get(base_url)
      #   print("Image URL:", image_url)
        print("Text:", text)
        

scrape_data(content)
