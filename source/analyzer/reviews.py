from groq_service import analyze_sentiment
import re

def analyze_reviews():
    reviews = ["Had a blast! Would recommend to everyone"]
    for review in reviews:
        sentiment_response = analyze_sentiment(review).lower()
        print(sentiment_response)
        match = re.search(r"category:\s*(\w+),\s*score:\s*(\d+)", sentiment_response)
        if match:
            sentiment = match.group(1)
            score = match.group(2)
        else:
            print("Sentiment and score not found")
            continue
        print(sentiment, score)