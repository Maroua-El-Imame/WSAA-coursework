# Booking DAO (Data Access Object) - interacts with the database to perform CRUD operations for bookings.
# Author: Maroua EL imame


import sqlite3
import dbconfig as cfg
import os
from datetime import datetime

ROOM_TYPES = {
    "Claddagh Suite": 180,
    "Blue Bay Rooftop": 220,
    "Royal Green": 200,
    "Red Zebra Twin": 160
}

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
                "guest_country": row[7],
                "price_per_night": row[8],
                "breakfast": row[9]
            })

        return bookings

    # GET ONE BOOKING BY ID
    def findByID(self, id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM bookings
        WHERE booking_id = ?
        """, (id,))
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
            "guest_country": row[7],
            "price_per_night": row[8],
            "breakfast": row[9] 
        }
    
    # CREATE BOOKING
    def create(self, booking):
        cursor = self.getcursor()

        room_type = booking.get("room_type")
        guests = int(booking.get("guests"))
        breakfast = int(booking.get("breakfast"))

        check_in = booking.get("check_in")
        check_out = booking.get("check_out")

        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        today = datetime.today()

        if room_type not in ROOM_TYPES:
            raise ValueError("Invalid room type")

        if guests < 1 or guests > 2:
            raise ValueError("Guests must be between 1 and 2")

        if check_in_date.date() < today.date():
            raise ValueError("Check-in must be today or a future date")

        if check_out_date <= check_in_date:
            raise ValueError("Check-out must be at least 1 day after check-in")

        price_per_night = ROOM_TYPES[room_type]

        if breakfast == 1:
            price_per_night += 15 * guests

        


        sql = f"""
        INSERT INTO bookings 
        (first_name, last_name, room_type, check_in, check_out, guests, guest_country, price_per_night, breakfast)
        VALUES (
            "{booking.get("first_name")}",
            "{booking.get("last_name")}",
            "{room_type}",
            "{booking.get("check_in")}",
            "{booking.get("check_out")}",
             {guests},
            "{booking.get("guest_country")}",
            {price_per_night},
            {breakfast}
    )
    """

        print(sql) 
        cursor.execute(sql)
    
        self.connection.commit()
        new_id = cursor.lastrowid
        booking["booking_id"] = new_id
        booking["price_per_night"] = price_per_night


        self.closeAll()
        return booking

    # UPDATE BOOKING
    def update(self, id, booking):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        room_type = booking.get("room_type")
        guests = int(booking.get("guests"))
        breakfast = int(booking.get("breakfast"))

        check_in = booking.get("check_in")
        check_out = booking.get("check_out")

        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        today = datetime.today()

        if room_type not in ROOM_TYPES:
            raise ValueError("Invalid room type")

        if guests < 1 or guests > 2:
            raise ValueError("Guests must be between 1 and 2")

        if check_in_date.date() < today.date():
            raise ValueError("Check-in must be today or a future date")

        if check_out_date <= check_in_date:
            raise ValueError("Check-out must be at least 1 day after check-in")

        price_per_night = ROOM_TYPES[room_type]

        if breakfast == 1:
            price_per_night += 15 * guests

        
        sql = f"""
        UPDATE bookings SET
                first_name = "{booking.get("first_name")}",
                last_name = "{booking.get("last_name")}",
                room_type = "{booking.get("room_type")}",
                check_in = "{booking.get("check_in")}",
                check_out = "{booking.get("check_out")}",
                guests = {booking.get("guests")},
                guest_country = "{booking.get("guest_country")}",
                price_per_night = {price_per_night},
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
        deleted_rows = cursor.rowcount

        conn.commit()
        conn.close()

        if deleted_rows == 0:
            return {"message": "Booking not found"}

        return {
            "message": "Booking deleted successfully",
            "deleted": id
        }
    
    # GET BOOKINGS BY COUNTRY
    def getBookingsByCountry(self):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT guest_country, COUNT(*) 
            FROM bookings
            GROUP BY guest_country
            ORDER BY COUNT(*) DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        countries = []
        for row in rows:
            countries.append({
                "country": row[0],
                "count": row[1]
            })

        return countries