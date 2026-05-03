
    const roomPrices = {
    "Claddagh Suite": 180,
    "Blue Bay Rooftop": 220,
    "Royal Green": 200,
    "Red Zebra Twin": 160
};

document.getElementById("room_type").addEventListener("input", () => {
    const room = document.getElementById("room_type").value;

    if (roomPrices[room]) {
        document.getElementById("price_per_night").value = roomPrices[room];
    }
});

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

    await fetch("/bookings", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(booking)
    });

    

document.getElementById("bookingForm").reset();

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