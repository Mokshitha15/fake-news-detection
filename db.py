import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mokshitha@15v",   # put your MySQL password
        database="fake_news"
    )

    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully!")

except Exception as e:
    print("❌ Error:", e)