# Sample code 

# bookingDAO.py

class BookingDAO:

    # get all bookings
    def getAll(self):
        return [
            {
                "booking_id": 1,
                "first_name": "Layla",
                "last_name": "Haddad",
                "room_type": "Double",
                "check_in": "2026-04-25",
                "check_out": "2026-04-27",
                "guests": 2
            },
            {
                "booking_id": 2,
                "first_name": "Amelia",
                "last_name": "Clarke",
                "room_type": "Single",
                "check_in": "2026-05-01",
                "check_out": "2026-05-03",
                "guests": 1
            },
            {
                "booking_id": 3,
                "first_name": "Anne-Marie",
                "last_name": "Dubois",
                "room_type": "Suite",
                "check_in": "2026-05-10",
                "check_out": "2026-05-14",
                "guests": 3
            },
            {
                "booking_id": 4,
                "first_name": "Evelyne",
                "last_name": "Moreau",
                "room_type": "Double",
                "check_in": "2026-06-02",
                "check_out": "2026-06-05",
                "guests": 2
            }
        ]

    # find booking by id
    def findByID(self, id):
        for booking in self.getAll():
            if booking["booking_id"] == id:
                return booking
        return None

    # create booking
    def create(self, booking):
        booking["booking_id"] = 999  # fake id for now
        return booking

    # update booking
    def update(self, id, booking):
        booking["booking_id"] = id
        return booking

    # delete booking
    def delete(self, id):
        return {"deleted": id}