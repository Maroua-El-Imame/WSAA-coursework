# Booking DAO (Data Access Object) - interacts with the database to perform CRUD operations for bookings.
# Author: Maroua EL imame

import sqlite3
import dbconfig as cfg
import os

class BookingDAO:
    connection = ""
    cursor = ""
    database = ""

    def __init__(self):
        ROOT = os.path.dirname(os.path.abspath(__file__))
        self.database = os.path.join(ROOT, "hotel.db")

    def getcursor(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.commit()
        self.connection.close()


    def getAll(self):
        cursor = self.getcursor()

        cursor.execute("SELECT * FROM bookings ORDER BY check_in")
        rows = cursor.fetchall()

        self.closeAll()



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
        conn = sqlite3.connect(self.database)
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
        cursor = self.getcursor()

        sql = f""""
        INSERT INTO bookings 
        (first_name, last_name, room_type, check_in, check_out, guests, guest_country, price_per_night, breakfast)
        VALUES (
            "{booking.get("first_name")}",
            "{booking.get("last_name")}",
            "{booking.get("room_type")}",
            "{booking.get("check_in")}",
            "{booking.get("check_out")}",
            {booking.get("guests")},
            "{booking.get("guest_country")}",
            {booking.get("price_per_night")},
            {booking.get("breakfast")}
        )"""

        print(sql)
        cursor.execute(sql)
    
        self.connection.commit()
        new_id = cursor.lastrowid
        booking["booking_id"] = new_id

        self.closeAll()
        return booking

    # UPDATE BOOKING
    def update(self, id, booking):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        sql = f"""
        UPDATE bookings SET
                first_name = "{booking.get("first_name")}",
                last_name = "{booking.get("last_name")}",
                room_type = "{booking.get("room_type")}",
                check_in = "{booking.get("check_in")}",
                check_out = "{booking.get("check_out")}",
                guests = {booking.get("guests")},
                guest_country = "{booking.get("guest_country")}"
                price_per_night = {booking.get("price_per_night")},
                breakfast = {booking.get("breakfast")}  
            WHERE booking_id = {id}
        """
        
        print(sql)
        cursor.execute(sql)

        conn.commit()
        conn.close()

        booking["booking_id"] = id
        return booking

    # DELETE BOOKING
    def delete(self, id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (id,))
        conn.commit()
        conn.close()

        return {"deleted": id}