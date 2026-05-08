try:
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup
except ImportError as e:
    raise ImportError("Required libraries not found. Install with: pip install beautifulsoup4") from e

def scrape_menu():
    url = "https://getfood.ng/restaurants/chicken-republic-challenge/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Chrome/120.0.0.0 Safari/537.36)"
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    item_names = soup.find_all("h6")
    item_prices = soup.find_all("span", class_="price")
    invalid_keywords = ["categories", "not available", "your order"]
    menu = {}
    counter = 1
    for name, price in zip(item_names, item_prices):
        clean_name = name.text.strip()
        clean_price = price.text.strip()
        if any(keyword in clean_name.lower() for keyword in invalid_keywords):
            continue
        menu[counter] = {"name": clean_name, "price": clean_price}
        counter += 1
    return menu