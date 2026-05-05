from flask import Flask, render_template, jsonify, request
from bookingDAO import BookingDAO
import requests

app = Flask(__name__)

bookingDAO = BookingDAO()


@app.route("/")
def home():
    return render_template("index.html")


# Weather API route
@app.route("/weather")
def get_weather():
    date = request.args.get("date")

    if not date:
        return jsonify({"error": "Please select a check-in date first."}), 400

    # Galway coordinates
    latitude = 53.2707
    longitude = -9.0568

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
        "timezone": "Europe/Dublin",
        "start_date": date,
        "end_date": date
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return jsonify({
            "error": "Could not fetch weather data",
            "status_code": response.status_code
        }), response.status_code

    data = response.json()
    daily = data["daily"]

    if not daily["time"]:
        return jsonify({"error": "No weather data available for this date."}), 404

    return jsonify({
        "city": "Galway",
        "date": daily["time"][0],
        "max_temperature": daily["temperature_2m_max"][0],
        "min_temperature": daily["temperature_2m_min"][0],
        "precipitation": daily["precipitation_sum"][0],
        "wind_speed": daily["wind_speed_10m_max"][0]
    })

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