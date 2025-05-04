import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import re  # Regular expression module for extracting numbers

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Define the base URL for the listings
base_url = "https://aqarmap.com.eg/ar/for-sale/property-type/cairo/new-cairo/?byOwnerOnly=1&page={}"

# Create CSV file and write headers
with open('aqarmap.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'عنوان الاعلان',
        'الفئه',
        'نوع الوحده ',
        'المساحه',
        'عدد الغرف',
        'عدد الحمامات',
        'مفروشه ام لا',
        'وصف الاعلان',
        'اللينك'
    ])

    # Loop through the first 10 pages
    for page in range(1, 11):  # Pages 1 to 10
        print(f"Processing page {page}...")

        # Open the page URL
        driver.get(base_url.format(page))
        time.sleep(5)

        # Get unique listing links on the current page
        listing_cards = driver.find_elements(By.CSS_SELECTOR, 'div.listing-card a[href*="/ar/listing/"]')
        listing_links = list(set(link.get_attribute('href') for link in listing_cards if link.get_attribute('href')))

        print(f"Found {len(listing_links)} listings on page {page}")

        # Define the threshold
        threshold = 5

        # Visit each listing
        for index, link in enumerate(listing_links, start=1):
            try:
                driver.get(link)
                time.sleep(3)

                # Extract price
                try:
                    price = driver.find_element(By.CSS_SELECTOR, 'span.text-title_3').text.strip()
                except NoSuchElementException:
                    price = "null"

                # Extract title
                try:
                    title = driver.find_element(By.CSS_SELECTOR, 'h1.text-gray__dark_2.text-body_1').text.strip()
                except NoSuchElementException:
                    title = "null"
                
                # Extract area (in square meters)
                try:
                    area = driver.find_element(By.CSS_SELECTOR, 'p.truncated-text.text-body_1').text.strip()
                except NoSuchElementException:
                    area = "null"
                
                # Extract number of rooms
                try:
                    rooms = driver.find_elements(By.CSS_SELECTOR, 'p.truncated-text.text-body_1')[1].text.strip()
                except NoSuchElementException:
                    rooms = "null"
                
                # Extract luxury level (e.g., Super Lux)
                try:
                    luxury = driver.find_elements(By.CSS_SELECTOR, 'p.truncated-text.text-body_1')[2].text.strip()
                except NoSuchElementException:
                    luxury = "null"
                
                # Extract number of bathrooms
                try:
                    bathrooms = driver.find_elements(By.CSS_SELECTOR, 'p.truncated-text.text-body_1')[3].text.strip()
                except NoSuchElementException:
                    bathrooms = "null"
                
                # Extract description (from <span> tag)
                try:
                    description = driver.find_element(By.CSS_SELECTOR, 'span').text.strip()
                except NoSuchElementException:
                    description = "null"

                # Extract the announcement count from the <p> element
                try:
                    announcement_text = driver.find_element(By.CSS_SELECTOR, 'p.pb-2x.text-gray__dark_1.text-body_2').text.strip()
                    announcement_number = int(re.search(r'\d+', announcement_text).group())  # Extract the number from the text
                except NoSuchElementException:
                    announcement_number = 0  # Default to 0 if not found
                
                # Check if the number is less than or equal to the threshold
                if announcement_number <= threshold:
                    # Extract the category (e.g., for sale, for rent)
                    category = "شقق للبيع"  # Modify this logic if necessary to extract the category
                    
                    # Extract unit type (e.g., apartment, villa)
                    unit_type = "شقه"  # Modify this logic if necessary to extract the unit type

                    # Extract furnished status (you can add logic to check for this)
                    furnished = "مفروشه" if "مفروشه" in description else "لا"

                    # Write data to CSV
                    writer.writerow([
                        title,
                        category,
                        unit_type,
                        area,
                        rooms,
                        bathrooms,
                        furnished,
                        description,
                        link
                    ])
                    print(f"Saved {index}. {title} - {announcement_number} announcements - {link}")
                else:
                    print(f"Skipping {index}. {title} - {announcement_number} announcements (exceeds threshold)")

            except Exception as e:
                print(f"Error processing {link}: {e}")

# Cleanup
driver.quit()

