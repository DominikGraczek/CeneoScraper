import requests
from bs4 import BeautifulSoup
# opinia opinion, div.js_product-review
# identyfikator opinii opinion_id, ["data-entry-id"]
# autora author, user-post__author-name
# rekomendację recomendation, user-post__author-recomendation
# liczbę gwiazdek score, user-post__score-count
# czy opinia jest potwierdzona zakupem purchased, review-pz
# data wystawienia opinii published_at, user-post__published
# data zakupu produktu purchase_at, user-post__published
# ile osób uznało opinię za przydatną thumbs_up, votes-yes-16711712
# ile osób uznało opinię za nieprzydatną thumbs_down,  votes-no-16711712
# treść opinii content, user-post__text
# listę wad cons, review-feature__col
# listę zalet pros, review-feature__col

# product_code = input("Podaj Kod Produktu: ")
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")
for opinion in opinions:
    print(opinion["data-entry-id"])
