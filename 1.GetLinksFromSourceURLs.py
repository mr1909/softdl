import re
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Disable logging
logging.disable(logging.CRITICAL)

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set path to chromedriver executable
chromedriver_path = "/path/to/chromedriver"  # Replace with your actual path

# Set the directory path for SourceURLs files
source_urls_dir = "SourceURLs"

# Find all text files in the SourceURLs directory
source_urls_files = [file for file in os.listdir(source_urls_dir) if file.endswith(".txt")]

# Set up the Chrome driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Process each SourceURLs file
for source_urls_file in source_urls_files:
    # Read URLs from the current SourceURLs file
    with open(os.path.join(source_urls_dir, source_urls_file), "r", encoding="utf-8") as file:
        urls = file.readlines()

    # Create a separate folder for the current SourceURLs file
    folder_name = os.path.splitext(source_urls_file)[0]
    folder_path = os.path.join("Result", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Process each URL
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace and newline characters

        # Print the URL being processed
        print(f"Processing URL: {url}")

        # Open the URL
        driver.get(url)

        # Wait for the website to load completely (10 seconds in this example)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Use regular expressions to find the links matching the criteria
        pattern = r'"(https://dl.+?\.(?:rar|exe|7z|zip)\?\d+)"'
        matches = re.findall(pattern, driver.page_source)

        # Exclude links containing ".tar.gz" or ".dmg"
        excluded_extensions = [".tar.gz", ".dmg"]
        filtered_matches = [link for link in matches if not any(extension in link for extension in excluded_extensions)]

        # Extract the filename from the URL
        filename = os.path.basename(url)
        filename = os.path.splitext(filename)[0]  # Remove the extension

        # Save the matching links to a separate file in the current folder using the extracted filename
        output_file = os.path.join(folder_path, f"Result_{filename}.txt")
        with open(output_file, "w", encoding="utf-8") as outfile:
            for link in filtered_matches:
                outfile.write(link + "\n")

# Close the browser
driver.quit()
