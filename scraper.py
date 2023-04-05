import requests
from bs4 import BeautifulSoup
# opinia opinion, div.js_product-review
# identyfikator opinii opinion_id, ["data-entry-id"]
# autora author, user-post__author-name
# rekomendację recomendation, span.user-post__author-recomendation > em
# liczbę gwiazdek score, user-post__score-count
# czy opinia jest potwierdzona zakupem purchased, div.review-pz
# data wystawienia opinii published_at, span.user-post__published > time:nth-child(1)["datetime"]
# data zakupu produktu purchase_at, span.user-post__published > time:nth-child(2)["datetime"]
# ile osób uznało opinię za przydatną thumbs_up, span[id^=votes-yes]
# ile osób uznało opinię za nieprzydatną thumbs_down,  span[id^=votes-no]
# treść opinii content, div.user-post__text
# listę wad cons, div.review-feature__col:has(> div.review-feature__title review-feature__title--negatives)
# listę zalet pros, div.review-feature__col:has(> div.review-feature__title review-feature__title--positives) 
# https://www.ceneo.pl/96685108#tab=reviews

def get_cos(ancestor, selector = None, attribute = None, return_list = False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy(),
        if not selector:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[atribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
# product_code = input("Podaj Kod Produktu: ")
product_code = "96685108"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
opinions = page.select("div.js_product-review")
all_opinions = []
for opinion in opinions:
    single_opinion = {
        "opinion_id": opinion["data-entry-id"],
        "author": opinion.select_one("span.user-post__author-name").text.strip(),
        "recomendation": opinion.select_one("span.user-post__author-recomendation > em").text.strip(),
        "score": opinion.select_one("span.user-post__score-count").text.strip(),
        "purchased": opinion.select_one("div.review-pz").text.strip(),
        "published_at": opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"].strip(),
        "purchase_at": opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"].strip(),
        "thumbs_up": opinion.select_one("span[id^=votes-yes]").text.strip(),
        "thumbs_down": opinion.select_one("span[id^=votes-no]").text.strip(),
        "content": opinion.select_one("div.user-post__text").text.strip(),
        "cons": [pros.text.strip() for pros in opinion.select("div.review-feature__col:has(> div.review-feature__title--negatives) > div.review-feature__item")],
        "pros": [cons.text.strip() for cons in opinion.select("div.review-feature__col:has(> div.review-feature__title--positives) > div.review-feature__item")],


    }
    all_opinions.append(single_opinion)
print(all_opinions)