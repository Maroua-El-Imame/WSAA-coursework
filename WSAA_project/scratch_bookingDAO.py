# Sample code

import sqlite3
import os

class BookingDAO:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(BASE_DIR, "hotel.db")

    # get all bookings

    def getAll(self):
        conn = sqlite3.connect(self.db)         # SQLite is just a file (hotel.db) in your project.  Sqlite3 library import to interact with it.
        cursor = conn.cursor()                  # DAO opens a connection to that file using sqlite3.connect().

        cursor.execute("SELECT * FROM bookings")
        rows = cursor.fetchall()

        conn.close()

        bookings = []
        for row in rows:
            bookings.append({
                "booking_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "room_type": row[3],
                "check_in": row[4],
                "check_out": row[5],
                "guests": row[6],
                "guest_country": row[7]
            })

        return bookings

    # GET ONE BOOKING BY ID
    def findByID(self, id):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM bookings
        ORDER BY last_name, first_name, check_in
        """)
        row = cursor.fetchone()

        conn.close()

        if row is None:
            return None

        return {
            "booking_id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "room_type": row[3],
            "check_in": row[4],
            "check_out": row[5],
            "guests": row[6],
            "guest_country": row[7]
        }

    # CREATE BOOKING
    def create(self, booking):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO bookings 
            (first_name, last_name, room_type, check_in, check_out, guests, guest_country)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            booking["first_name"],
            booking["last_name"],
            booking["room_type"],
            booking["check_in"],
            booking["check_out"],
            booking["guests"],
            booking["guest_country"]
        ))

        conn.commit()
        booking_id = cursor.lastrowid
        conn.close()

        booking["booking_id"] = booking_id
        return booking

    # UPDATE BOOKING
    def update(self, id, booking):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE bookings SET
                first_name = ?,
                last_name = ?,
                room_type = ?,
                check_in = ?,
                check_out = ?,
                guests = ?,
                guest_country = ?
            WHERE booking_id = ?
        """, (
            booking["first_name"],
            booking["last_name"],
            booking["room_type"],
            booking["check_in"],
            booking["check_out"],
            booking["guests"],
            booking["guest_country"],
            id
        ))

        conn.commit()
        conn.close()

        booking["booking_id"] = id
        return booking

    # DELETE BOOKING
    def delete(self, id):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (id,))
        conn.commit()
        conn.close()

        return {"deleted": id}