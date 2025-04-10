from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import csv

"""
Eurogamer Blog Scraper

This script scrapes the latest blog posts from Eurogamer.net's blogs section,
extracts key metadata, and saves it in both JSON and CSV formats.

Author: Larry Isenhour II
GitHub: https://github.com/leisenhour2/Github-Portfolio/blob/main/Python/Intermediate%20Python/Eurogamer%20Web%20Scraper/

Usage:
    - Requires a valid user agent in 'user_agent_override.txt'
    - Outputs saved in the /data directory

Dependencies:
    - requests
    - beautifulsoup4
"""


# Utility function to clean text by replacing non-breaking spaces and trimming whitespace
def clean(text):
    return text.replace('\u00a0', ' ').strip()

# Set file path to the directory where the script is located
filepath = Path(__file__).parent.resolve()
print("File path:", filepath)

# Read user-agent string from an external text file to mimic a real browser and avoid blocks
user_agent = ""
with open(filepath / "user_agent_override.txt", 'r') as user_override:
    user_agent = user_override.read()

# Target URL for Eurogamer blog page
url = "https://www.eurogamer.net/blogs"

# Send GET request with custom user-agent
response = requests.get(url, headers={"user-agent": user_agent})

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the container that holds all blog archive items
main_archive = soup.find("div", class_="archive__items")
archives = main_archive.find_all("article", class_="archive__item")

# List to hold blog post data
blog_list = []

# Iterate through each blog post and extract relevant details
for archive in archives:
    try:
        my_archive = archive.find("div", class_="archive__details")
        title = clean(my_archive.find("h2").get_text(strip=True))
        headline = clean(my_archive.find("div", class_="archive__strapline").get_text(strip=True))
        metadata = my_archive.find("div", class_="archive__metadata")
        date = clean(metadata.find("time").get_text(strip=True))
        author = clean(metadata.find("span").get_text(strip=True))

        # Append cleaned blog data as a dictionary to the list
        blog_list.append({
            "Title": title,
            "Headline": headline,
            "Author": author,
            "Date Published": date
        })
    except Exception as e:
        # Print error if any blog element is missing or parsing fails
        print(f"Error: {e}")

# Print blog list as formatted JSON in terminal (for dev/debugging)
print(json.dumps(blog_list, indent=4))

# Save blog data as JSON file in a 'data' directory
json_output_path = filepath / "data" / "blogs.json"
json_output_path.parent.mkdir(exist_ok=True)  # Ensure the directory exists
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(blog_list, f, indent=4, ensure_ascii=False)

# Save blog data as CSV for spreadsheet users
csv_output_path = filepath / "data" / "blogs.csv"
with open(csv_output_path, "w", encoding="utf-8", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Title", "Headline", "Author", "Date Published"])
    writer.writeheader()
    writer.writerows(blog_list)

# Confirm export success in terminal
print(f"\n Blog data saved to:")
print(f"   - JSON: {json_output_path}")
print(f"   - CSV:  {csv_output_path}")
