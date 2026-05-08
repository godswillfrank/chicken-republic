from flask import Flask, request, session, render_template, redirect, url_for  # type: ignore[import]
from scraper import scrape_menu

app = Flask(__name__)
app.secret_key = "chickenrepublic"

# Route 1 - Home page with menu
@app.route("/")
def home():
    menu = scrape_menu()
    # Store menu with string keys for session compatibility
    session["menu"] = {str(k): v for k, v in menu.items()}
    return render_template("index.html", menu=menu)

# Route 2 - Place an order
@app.route("/order", methods=["POST"])
def order():
    menu = session.get("menu", {})
    selected = request.form.getlist("items")
    order = []
    for item_number in selected:
        if item_number in menu:  # now comparing string to string
            order.append(menu[item_number])
    session["order"] = order
    return redirect(url_for("receipt"))

# Route 3 - Receipt page
@app.route("/receipt")
def receipt():
    order = session.get("order", [])
    total = sum(
        float(item["price"].replace("₦", "").replace(",", ""))
        for item in order
    )
    return render_template("receipt.html", order=order, total=f"₦{total:,.2f}")

if __name__ == "__main__":
    app.run(debug=True)