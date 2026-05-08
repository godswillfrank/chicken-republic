# 🍗 Chicken Republic Ordering System

A Python web scraping and Flask API project that retrieves the live menu
from Chicken Republic on getfood.ng and allows users to place orders
and get a receipt with the total cost.

---

## 📌 Features

- Scrapes live menu data from getfood.ng in real time
- Displays menu items with real Naira prices
- Allows users to place multiple orders
- Calculates and returns total cost on receipt
- REST API built with Flask

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Requests
- BeautifulSoup4

---

## 📁 Project Structure

chicken-republic/
├── app.py            # Flask routes and API logic
├── scraper.py        # Web scraping logic
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation

---

## 🚀 How to Run

1. Clone the repository
git clone https://github.com/godswillfrank/chicken-republic.git

2. Navigate into the project folder
cd chicken-republic

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask app
python app.py

5. Open your browser and visit
http://127.0.0.1:5000

---

## 📡 API Endpoints

| Method | Endpoint   | Description              |
|--------|------------|--------------------------|
| GET    | /          | Returns full menu as JSON|
| POST   | /order     | Place an order           |
| GET    | /receipt   | Get receipt with total   |

---

## 📝 Example API Response

GET /

{
    "1": {"name": "New Big Crew Meal", "price": "₦25700.00"},
    "2": {"name": "Refuel Dodo",       "price": "₦3000.00"},
    "3": {"name": "Chips",             "price": "₦900.00"}
}

---

## 📦 POST /order Example

Send a POST request with JSON body:

{
    "items": [1, 3, 5]
}

Response:

{
    "message": "Order received!",
    "order": [
        {"name": "New Big Crew Meal", "price": "₦25700.00"},
        {"name": "Chips",             "price": "₦900.00"}
    ]
}

---

## 👨‍💻 Author

Godswill
Final Python Project