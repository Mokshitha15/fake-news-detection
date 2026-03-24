import mysql.connector

# ✅ Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",   # 🔴 change this
    database="fake_news"
)

cursor = conn.cursor()

# ✅ Step 2: Take user input
news = input("Enter news: ")

# ✅ Step 3: Fake News Prediction (Simple Logic)
def predict_news(text):
    fake_keywords = ["fake", "rumor", "not true", "hoax"]
    for word in fake_keywords:
        if word in text.lower():
            return "Fake"
    return "Real"

prediction = predict_news(news)

# ✅ Step 4: Verification Logic (Simple)
def verify_news(text):
    if "official" in text.lower() or "government" in text.lower():
        return True
    return False

verified = verify_news(news)

# ✅ Step 5: Insert into Database
query = """
INSERT INTO news_data (title, content, prediction, verified)
VALUES (%s, %s, %s, %s)
"""

values = ("User News", news, prediction, verified)

cursor.execute(query, values)
conn.commit()

# ✅ Step 6: Display Output
print("\n--- RESULT ---")
print("News:", news)
print("Prediction:", prediction)
print("Verified:", verified)

# ✅ Step 7: Show all stored data
print("\n--- DATABASE RECORDS ---")
cursor.execute("SELECT * FROM news_data")

for row in cursor.fetchall():
    print(row)

# ✅ Close connection
cursor.close()
conn.close()