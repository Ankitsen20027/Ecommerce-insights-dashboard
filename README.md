# 📚 Books to Scrape - Web Scraper & Analytics

A Python web scraper that extracts book data (title, price, rating, availability) from [books.toscrape.com](https://books.toscrape.com), exports it to CSV, and visualizes it in Power BI.

## 🔧 Tech Stack
- **Python** - core scripting
- **Requests** - HTTP requests
- **BeautifulSoup4** - HTML parsing
- **Pandas** - data cleaning & CSV export
- **Power BI** - dashboard & visualization

## 📌 What it does
- Scrapes all book listing pages from the site
- Extracts: title, price (£), star rating, availability, page number
- Cleans and structures the data using Pandas
- Exports a ready-to-use `books_data.csv`
- CSV imported into Power BI to build a dashboard (price distribution, rating breakdown, availability trends)

## 🚀 How to run
```bash
pip install requests beautifulsoup4 pandas
python books_scraper.py
```
This generates `books_data.csv` in the project folder.

## 📊 Dashboard
The CSV output was imported into Power BI to analyze:
- Average price by rating
- Number of books by rating category
- In-stock vs out-of-stock distribution

*(Add your dashboard screenshot here: `dashboard_screenshot.png`)*

## 📁 Project Structure
```
books-scraper/
├── books_scraper.py
├── books_data.csv
├── dashboard_screenshot.png
└── README.md
```

## 🙋 Author
Built as a portfolio project to demonstrate web scraping + data analytics skills.
