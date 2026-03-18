import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape 
url = "https://quotes.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract quotes
quotes = []
for quote in soup.find_all("span", class_="text"):
    quotes.append(quote.text)

# Create DataFrame
df = pd.DataFrame(quotes, columns=["text"])

# Save to CSV
df.to_csv("scraped_data.csv", index=False)

print("Data scraped and saved as scraped_data.csv")