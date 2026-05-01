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
    guest_country TEXT NOT NULL,
    price_per_night REAL NOT NULL,
    breakfast INTEGER DEFAULT 0
)
""")

# Sample data
bookings = [
    ("Layla", "Haddad", "Double", "2026-04-25", "2026-04-27", 2, "Morocco", 120.0, 1),
    ("Amelia", "Clarke", "Single", "2026-05-01", "2026-05-03", 1, "Ireland", 80.0, 0),
    ("Kenji", "Tanaka", "Double", "2026-05-04", "2026-05-08", 2, "Japan", 150.0, 1),
    ("Sofia", "Martinez", "Suite", "2026-05-06", "2026-05-10", 3, "Spain", 200.0, 1),
    ("Chloe", "Dubois", "Single", "2026-05-11", "2026-05-13", 1, "France", 90.0, 0),
    ("Luca", "Bianchi", "Double", "2026-05-14", "2026-05-18", 2, "Italy", 140.0, 1),
    ("Ava", "Murphy", "Suite", "2026-05-16", "2026-05-20", 4, "Ireland", 250.0, 1),
    ("Noah", "Smith", "Single", "2026-05-18", "2026-05-21", 1, "USA", 100.0, 0),
    ("Fatima", "Alami", "Double", "2026-05-20", "2026-05-24", 2, "Morocco", 120.0, 1),
    ("Jonas", "Muller", "Single", "2026-05-22", "2026-05-25", 1, "Germany", 85.0, 0)
]

cursor.executemany("""
INSERT INTO bookings
(first_name, last_name, room_type, check_in, check_out, guests, guest_country, price_per_night, breakfast)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", bookings)

conn.commit()
conn.close()

print("hotel.db created successfully")