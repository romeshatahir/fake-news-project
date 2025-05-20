
fake_keywords = [ "miracle", "secret", "shocking", "cure","fahad", "alien", "unbelievable", "hoax", "exposed", "conspiracy", "bizarre" ]

print("Fake News Detector (Word Match Prototype)") 
print("Type a news headline (or 'exit' to quit):")

while True: 
    news = input("News: ").lower() 
    if news == "exit":
        break
    
    news_words = news.strip().split(" ")

    for word in news_words:
        if word in fake_keywords:
            print("Prediction: FAKE")
            break
    else:
        print("Prediction: REAL")