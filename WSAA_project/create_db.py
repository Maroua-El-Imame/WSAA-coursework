import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "hotel.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Remove old table if it exists
cursor.execute("DROP TABLE IF EXISTS bookings")

# Create fresh bookings table
cursor.execute("""
CREATE TABLE bookings (
    booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    room_type TEXT NOT NULL,
    check_in TEXT NOT NULL,
    check_out TEXT NOT NULL,
    guests INTEGER NOT NULL,
    guest_country TEXT NOT NULL
)
""")

# Sample data
bookings = [
    ("Layla", "Haddad", "Double", "2026-04-25", "2026-04-27", 2, "Morocco"),
    ("Amelia", "Clarke", "Single", "2026-05-01", "2026-05-03", 1, "Ireland"),
    ("Kenji", "Tanaka", "Double", "2026-05-04", "2026-05-08", 2, "Japan"),
    ("Sofia", "Martinez", "Suite", "2026-05-06", "2026-05-10", 3, "Spain"),
    ("Chloe", "Dubois", "Single", "2026-05-11", "2026-05-13", 1, "France"),
    ("Luca", "Bianchi", "Double", "2026-05-14", "2026-05-18", 2, "Italy"),
    ("Ava", "Murphy", "Suite", "2026-05-16", "2026-05-20", 4, "Ireland"),
    ("Noah", "Smith", "Single", "2026-05-18", "2026-05-21", 1, "USA"),
    ("Fatima", "Alami", "Double", "2026-05-20", "2026-05-24", 2, "Morocco"),
    ("Jonas", "Muller", "Single", "2026-05-22", "2026-05-25", 1, "Germany")
]

cursor.executemany("""
INSERT INTO bookings
(first_name, last_name, room_type, check_in, check_out, guests, guest_country)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", bookings)

conn.commit()
conn.close()

print("hotel.db created successfully")