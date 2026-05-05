
    const roomPrices = {
    "Claddagh Suite": 180,
    "Blue Bay Rooftop": 220,
    "Royal Green": 200,
    "Red Zebra Twin": 160
};

function updatePrice() {
    const room = document.getElementById("room_type").value;
    const guests = parseInt(document.getElementById("guests").value) || 0;
    const breakfast = parseInt(document.getElementById("breakfast").value);

    if (roomPrices[room]) {
        let price = roomPrices[room];

        if (breakfast === 1) {
            price = price + (15 * guests);
        }

        document.getElementById("price_per_night").value = price;
    }
}

document.getElementById("room_type").addEventListener("input", updatePrice);
document.getElementById("guests").addEventListener("input", updatePrice);
document.getElementById("breakfast").addEventListener("change", updatePrice);

async function loadBookings() {
    const res = await fetch("/bookings");
    const data = await res.json();

    const container = document.getElementById("bookings");
    container.innerHTML = "";
    container.style.display = "grid";

    
    data.forEach(b => {
        const card = document.createElement("div");
        card.className = "card";

        
        card.innerHTML = `
            <h4>Booking number ${b.booking_id}</h4>
            <h3>${b.first_name} ${b.last_name}</h3>
            <p>Room: ${b.room_type}</p>
            <p>Check-in: ${b.check_in}</p>
            <p>Check-out: ${b.check_out}</p>
            <p>Guests: ${b.guests}</p>
            <p>Country: ${b.guest_country}</p>
            <p>Price: €${b.price_per_night}</p>
            <p>Breakfast: ${b.breakfast == 1 ? "Yes" : "No"}</p>
        `;
            container.appendChild(card);
});
}

document.getElementById("loadBtn").addEventListener("click", async () => {
    await loadBookings();
    document.getElementById("backBtn").style.display = "block";
    scrollToBottom();
});



document.getElementById("bookingForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    console.log("Book Now clicked");

    const booking = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        room_type: document.getElementById("room_type").value,
        check_in: document.getElementById("check_in").value,
        check_out: document.getElementById("check_out").value,  
        guests: parseInt(document.getElementById("guests").value),
        guest_country: document.getElementById("guest_country").value,

        price_per_night: parseFloat(document.getElementById("price_per_night").value),
        breakfast: parseInt(document.getElementById("breakfast").value)
    };

const bookingId = document.getElementById("booking_id").value;

let url = "/bookings";
let method = "POST";

if (bookingId) {
    url = "/bookings/" + bookingId;
    method = "PUT";
}

await fetch(url, {
    method: method,
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(booking)
});

    
document.getElementById("bookingForm").reset();
document.getElementById("booking_id").value = "";
document.getElementById("submitBtn").textContent = "Book Now";

await loadBookings();
document.getElementById("backBtn").style.display = "inline-block";
});


document.getElementById("backBtn").addEventListener("click", () => {
    document.getElementById("bookings").style.display = "none";
    document.getElementById("backBtn").style.display = "none";
    

});

function scrollToBottom() {
    setTimeout(() => {
        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: "smooth"
        });
    }, 100);
}


document.getElementById("weatherBtn").addEventListener("click", async () => {
    const checkInDate = document.getElementById("check_in").value;
    const weatherResult = document.getElementById("weatherResult");
    const weatherSection = document.querySelector(".weather-section");
     const weatherBackBtn = document.getElementById("weatherBackBtn");

    weatherSection.style.display = "block";
    weatherBackBtn.style.display = "inline-block";


    if (!checkInDate) {
        weatherResult.innerHTML = "<p>Please select a check-in date first.</p>";
        scrollToBottom();

        return;
    }


    const selectedDate = new Date(checkInDate);
    const today = new Date();

    today.setHours(0, 0, 0, 0);
    selectedDate.setHours(0, 0, 0, 0);

    const differenceInDays = (selectedDate - today) / (1000 * 60 * 60 * 24);

    if (differenceInDays < 0) {
        weatherResult.innerHTML = "<p>Please select today or a future date.</p>";
        scrollToBottom()
        return;
    }

    if (differenceInDays > 15) {
        weatherResult.innerHTML = "<p>Weather forecast is only available up to 15 days ahead.</p>";
        scrollToBottom()
        return;
    }

    const res = await fetch(`/weather?date=${checkInDate}`);
    const data = await res.json();

    if (data.error) {
        weatherResult.innerHTML = `<p>${data.error}</p>`;
        scrollToBottom()
        return;
    }

    weatherResult.innerHTML = `
        <div class="weather-card">
            <h3>${data.city} Weather</h3>
            <p>Date: ${data.date}</p>
            <p>Max Temperature: ${data.max_temperature}°C</p>
            <p>Min Temperature: ${data.min_temperature}°C</p>
            <p>Rain: ${data.precipitation} mm</p>
            <p>Max Wind Speed: ${data.wind_speed} km/h</p>
        </div>
    `;


scrollToBottom();
});

document.getElementById("weatherBackBtn").addEventListener("click", () => {
    document.querySelector(".weather-section").style.display = "none";
    document.getElementById("weatherResult").innerHTML = "";
    document.getElementById("weatherBackBtn").style.display = "none";
});


document.getElementById("editBtn").addEventListener("click", async () => {
    await loadBookings();

    const res = await fetch("/bookings");
    const data = await res.json();

    const bookingId = prompt("Enter the booking number you want to edit:");

    const selectedBooking = data.find(b => b.booking_id == bookingId);
   
if (selectedBooking) {
    document.getElementById("booking_id").value = bookingId;

    document.getElementById("first_name").value = selectedBooking.first_name;
    document.getElementById("last_name").value = selectedBooking.last_name;
    document.getElementById("room_type").value = selectedBooking.room_type;
    document.getElementById("check_in").value = selectedBooking.check_in;
    document.getElementById("check_out").value = selectedBooking.check_out;
    document.getElementById("guests").value = selectedBooking.guests;
    document.getElementById("guest_country").value = selectedBooking.guest_country;
    document.getElementById("price_per_night").value = selectedBooking.price_per_night;
    document.getElementById("breakfast").value = selectedBooking.breakfast;

    const container = document.getElementById("bookings");

    container.innerHTML = `
        <div class="card">
            <h4>Editing booking number ${selectedBooking.booking_id}</h4>
            <h3>${selectedBooking.first_name} ${selectedBooking.last_name}</h3>
            <p>Room: ${selectedBooking.room_type}</p>
            <p>Check-in: ${selectedBooking.check_in}</p>
            <p>Check-out: ${selectedBooking.check_out}</p>
            <p>Guests: ${selectedBooking.guests}</p>
            <p>Country: ${selectedBooking.guest_country}</p>
            <p>Price: €${selectedBooking.price_per_night}</p>
            <p>Breakfast: ${selectedBooking.breakfast == 1 ? "Yes" : "No"}</p>
        </div>
    `;

    container.style.display = "grid";
    document.getElementById("submitBtn").textContent = "Update Booking";
    alert("Booking loaded. You can now edit the form.");

} else { 
    alert("Booking not found.");
}
});