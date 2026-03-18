from textblob import TextBlob
import pandas as pd

# Load dataset
data = pd.read_csv("scraped_data.csv")

# Function for sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
data["sentiment"] = data["text"].apply(get_sentiment)

# Show output
print(data)

# Save output
data.to_csv("output.csv", index=False)