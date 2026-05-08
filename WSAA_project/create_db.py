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
    ("Maroua", "Meli", "Claddagh Suite", "2026-04-20", "2026-04-24", 2, "Morocco", 220.0, 1),
    ("Andrew", "Beatty", "Blue Bay Rooftop", "2026-04-22", "2026-04-26", 1, "Japan", 180.0, 1),
    ("Amel", "Eden", "Royal Green", "2026-04-25", "2026-04-28", 2, "Morocco", 230.0, 1),
    ("Amelia", "OSullivan", "Blue Bay Rooftop", "2026-05-01", "2026-05-04", 1, "Ireland", 220.0, 1),
    ("Kenji", "Nakamura", "Claddagh Suite", "2026-05-04", "2026-05-08", 2, "Japan", 180.0, 1),
    ("Sofia", "Martinez", "Red Zebra Twin", "2026-05-06", "2026-05-10", 3, "Spain", 160.0, 1),
    ("Chloe", "Dubois", "Royal Green", "2026-05-11", "2026-05-13", 1, "France", 200.0, 0),
    ("Luca", "Bianchi", "Blue Bay Rooftop", "2026-05-14", "2026-05-18", 2, "Italy", 220.0, 1),
    ("Ava", "Murphy", "Claddagh Suite", "2026-05-16", "2026-05-20", 4, "Ireland", 180.0, 1),
    ("Noah", "Anderson", "Red Zebra Twin", "2026-05-18", "2026-05-21", 1, "United States", 160.0, 0),
    ("Fatima", "Alami", "Royal Green", "2026-05-20", "2026-05-24", 2, "Morocco", 200.0, 1),
    ("Jonas", "Muller", "Red Zebra Twin", "2026-05-22", "2026-05-25", 1, "Germany", 160.0, 0),
    ("Isabella", "Costa", "Blue Bay Rooftop", "2026-05-24", "2026-05-27", 2, "Portugal", 220.0, 1),
    ("Yasmine", "Benali", "Royal Green", "2026-05-25", "2026-05-29", 2, "Morocco", 200.0, 1),
    ("Oliver", "Wilson", "Claddagh Suite", "2026-05-27", "2026-05-30", 1, "Canada", 180.0, 0),
    ("Elena", "Petrova", "Blue Bay Rooftop", "2026-05-28", "2026-06-01", 2, "Greece", 220.0, 1),
    ("Michael", "Scott", "Claddagh Suite", "2026-06-01", "2026-06-04", 1, "United States", 180.0, 0),
    ("James", "Bond", "Royal Green", "2026-06-03", "2026-06-06", 1, "United Kingdom", 200.0, 1),
    ("Aisha", "Khan", "Blue Bay Rooftop", "2026-06-05", "2026-06-08", 2, "United Arab Emirates", 220.0, 1),
    ("Mateo", "Silva", "Red Zebra Twin", "2026-06-06", "2026-06-10", 2, "Brazil", 160.0, 1),
    ("Hana", "Kim", "Royal Green", "2026-06-08", "2026-06-12", 1, "South Korea", 200.0, 1),
    ("Leo", "Johansson", "Claddagh Suite", "2026-06-10", "2026-06-13", 2, "Sweden", 180.0, 0),
    ("Nina", "Ivanova", "Blue Bay Rooftop", "2026-06-12", "2026-06-15", 2, "Russia", 220.0, 1),
    ("Daniel", "Okafor", "Royal Green", "2026-06-14", "2026-06-18", 3, "Nigeria", 200.0, 1)

]

cursor.executemany("""
INSERT INTO bookings
(first_name, last_name, room_type, check_in, check_out, guests, guest_country, price_per_night, breakfast)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", bookings)

conn.commit()
conn.close()

print("hotel.db created successfully")