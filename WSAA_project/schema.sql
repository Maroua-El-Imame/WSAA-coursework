DROP TABLE IF EXISTS booking;

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
);