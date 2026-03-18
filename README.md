# Sentiment Analysis Project

This project implements a Sentiment Analysis system using Python to classify text data into positive, negative, and neutral sentiments.

## 📌 Overview
Sentiment analysis is a Natural Language Processing (NLP) technique used to identify emotions in text. This project demonstrates a complete pipeline from data collection to visualization.

## ⚙️ Project Workflow
1. **Data Collection (Web Scraping)**  
   Text data is collected from an online source using Python (requests and BeautifulSoup).

2. **Data Storage**  
   The scraped data is stored in a CSV file (`scraped_data.csv`).

3. **Data Processing**  
   Sentiment analysis is performed using the TextBlob library. Each text is classified based on polarity:
   - Positive (> 0)
   - Negative (< 0)
   - Neutral (= 0)

4. **Output Generation**  
   The results are saved in `output.csv` with sentiment labels.

5. **Data Visualization**  
   Excel is used to create charts showing sentiment distribution.

## 🛠️ Technologies Used
- Python  
- Pandas  
- TextBlob  
- BeautifulSoup  
- Excel  

## 📊 Results
The dataset shows a mix of positive, negative, and neutral sentiments. Most of the texts are classified as positive, demonstrating the effectiveness of the model.

## ☁️ Future Scope
This solution can be extended using Azure services such as:
- Azure Blob Storage (data storage)
- Azure Data Factory (data ingestion)
- Power BI (visualization)

## 🔗 GitHub
The complete code and dataset are available in this repository.

## 📚 References
- https://monkeylearn.com/sentiment-analysis/  
- TextBlob Documentation
