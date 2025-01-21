import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def analyze_sentiment(review):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""Provide me a sentinent analysis of the following comment:
                (Start of review){review}(End of review)
                Provide the answer in the following format:
                category: positive, negative, neutral, mixed
                sentiment polarity score: 0-100
                Your example should be like this:
                category: (category_name), score: (score_value)"""
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content