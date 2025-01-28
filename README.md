# Amazon_Silver_Bar_Python_Scrapy
# Silver Bar 1 kg 999.9 Purity Search in Amazon Website using Python with Scrapy Framework

## Developer Information
- **Name:** MARUTHACHALAM S
- **Project Title:** Silver Bar 1 kg 999.9 Purity Search in Amazon Website using Python with Scrapy Framework
- **Date:** 28.01.2025
- **Version:** 1

## Description
This project involves web scraping the Amazon India website to search for 1 kg silver bars with 999.9 purity. The script extracts details such as company name, product title, ratings, MRP, and final price. The extracted data is then processed and logged.

## Requirements
- Python 3.x
- Scrapy

## Installation

### Step 1: Install Python
Ensure you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

### Step 2: Install Required Libraries
```bash
pip install scrapy

### Step 2: Run the Script:
```bash
scrapy crawl amazon_silver_scrap

Script Explanation:

Main Script:
Opens Amazon India website.
Searches for "silver bar 1kg 999.9 purity".
Iterates through the search results, extracting details for each product.
Extracts detailed information from each product listing.
Logs the scraped items and follows the next page link to continue scraping.

Author
MARUTHACHALAM S
