import re

# Match user query to a category
def match_query_advanced(query, categories):
    query = query.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(rf"\b{keyword.lower()}\b", query):
                return category
    return "Unmatched"

# Detect sentiment from the query
def detect_sentiment(query):
    positive_keywords = ["good", "great", "excellent", "happy", "love", "awesome", "amazing"]
    negative_keywords = ["bad", "poor", "terrible", "unhappy", "hate", "awful", "worse"]

    query = query.lower()
    if any(word in query for word in positive_keywords):
        return "Positive"
    elif any(word in query for word in negative_keywords):
        return "Negative"
    return "Neutral"
