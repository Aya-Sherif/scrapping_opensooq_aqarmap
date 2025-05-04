
**Real Estate Scraper**

A Python-based web scraping tool that extracts real estate listings from multiple platforms, including Aqarmap and OpenSooq. This scraper collects valuable data such as property title, price, area, number of rooms, number of bathrooms, description, and listing URL. It is designed to:

* Scrape data from multiple pages (up to 10 pages) on both Aqarmap and OpenSooq.
* Filter listings based on a threshold value (e.g., number of available ads).
* Store the collected information in a CSV file with custom headers for easy data analysis.
* Handle various real estate property types such as apartments, villas, and more.
* Supports automated scraping with Selenium and ChromeDriver, and includes error handling to ensure smooth execution.

### Features:

* Scrapes multiple pages of listings (up to 10 pages) from both Aqarmap and OpenSooq.
* Extracts detailed property data (title, price, description, area, rooms, etc.).
* Filters listings based on a custom threshold value (e.g., number of ads).
* Saves data into a CSV file with clear column headers.
* Robust error handling for missing values.

### Platforms Supported:

* Aqarmap (Egypt)
* OpenSooq (Multiple countries)

### Installation:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/real-estate-scraper.git
   ```
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```
3. Run the script:

   ```
   python aqarmap.py  
   ```

### Requirements:

* Python 3.x
* Selenium
* WebDriver Manager

