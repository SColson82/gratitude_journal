import sqlite3
from datetime import datetime

conn = sqlite3.connect("journal.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS gratitude_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    item_1 TEXT NOT NULL,
    item_2 TEXT NOT NULL,
    item_3 TEXT NOT NULL
)
""")

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"What are 3 things you're grateful for? ({now})")
item_1 = input("1: ").strip()
item_2 = input("2: ").strip()
item_3 = input("3: ").strip()

# Save entry to database
cursor.execute(
    "INSERT INTO gratitude_entries (timestamp, item_1, item_2, item_3) VALUES (?, ?, ?, ?)", (now, item_1, item_2, item_3)
)
conn.commit()
conn.close()

print("Your gratitude entry has been saved!")

