from flask import Flask, jsonify, request
from flask import render_template
from scratch_bookingDAO import BookingDAO

app = Flask(__name__)

bookingDAO = BookingDAO()


@app.route("/")
def home():
    return render_template("index.html")

# get all bookings
@app.route('/bookings')
def getAll():
    return jsonify(bookingDAO.getAll())


# find booking by id
@app.route('/bookings/<int:id>')
def findById(id):
    booking = bookingDAO.findByID(id)
    if booking is None:
        return jsonify({"message": "Booking not found"}), 404
    return jsonify(booking)


# create booking
@app.route('/bookings', methods=['POST'])
def create():
    booking = request.json
    new_booking = bookingDAO.create(booking)
    return jsonify(new_booking)


# update booking
@app.route('/bookings/<int:id>', methods=['PUT'])
def update(id):
    booking = request.json
    updated_booking = bookingDAO.update(id, booking)
    return jsonify(updated_booking)


# delete booking
@app.route('/bookings/<int:id>', methods=['DELETE'])
def delete(id):
    result = bookingDAO.delete(id)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)