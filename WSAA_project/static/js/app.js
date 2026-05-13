// ===== ROOM PRICE LOGIC =====

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

// ===== ROOM PRICE EVENT LISTENERS =====

document.getElementById("room_type").addEventListener("input", updatePrice);
document.getElementById("guests").addEventListener("input", updatePrice);
document.getElementById("breakfast").addEventListener("change", updatePrice);


// ===== LOAD & DISPLAY BOOKINGS =====

async function loadBookings(showDelete = false) {
    const res = await fetch("/bookings");
    const data = await res.json();
    data.sort((a, b) => a.booking_id - b.booking_id);

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

            ${showDelete ? `
            <button class="delete-btn" onclick="deleteBooking(${b.booking_id})">
            Delete
            </button>
` : ""}
        `;
            container.appendChild(card);
});
}

// ===== SHOW BOOKINGS BUTTON =====

document.getElementById("loadBtn").addEventListener("click", async () => {
    clearEditMode();
    document.querySelector(".weather-section").style.display = "none";
    document.getElementById("weatherResult").innerHTML = "";
    document.getElementById("weatherBackBtn").style.display = "none";
    document.getElementById("countryChart").style.display = "none";

    await loadBookings(false);
    document.getElementById("backBtn").style.display = "block";
    scrollToBottom();
});

// ===== CREATE OR UPDATE BOOKING =====

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

    
    // FRONTEND VALIDATION 
    // Guests
    if (booking.guests < 1 || booking.guests > 2) {
        alert("Guests must be between 1 and 2");
        return;
    }

    // Dates
    const today = new Date();
    const checkIn = new Date(booking.check_in);
    const checkOut = new Date(booking.check_out);

    today.setHours(0,0,0,0);
    checkIn.setHours(0,0,0,0);
    checkOut.setHours(0,0,0,0);

    if (checkIn < today) {
        alert("Check-in must be today or a future date");
        return;
    }

    if (checkOut <= checkIn) {
        alert("Check-out must be at least 1 day after check-in");
        return;
    }

    const bookingId = document.getElementById("booking_id").value;
    let url = "/bookings";
    let method = "POST";

    if (bookingId) {
        url = "/bookings/" + bookingId;
        method = "PUT";
    }

    const response = await fetch(url, {

        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(booking)
    });

    const data = await response.json();

    if (!response.ok) {
        alert(data.error);
        return;
    }

    alert(bookingId ? "Booking updated successfully" : "Booking created successfully");
    document.getElementById("countryChart").style.display = "none";
    if (window.countryChart instanceof Chart) window.countryChart.destroy();
    
    document.getElementById("bookingForm").reset();
    document.getElementById("booking_id").value = "";
    document.getElementById("submitBtn").textContent = "Book Now";
    document.querySelectorAll("#bookingForm input, #bookingForm select")
        .forEach(field => {
            field.classList.remove("editing-input");
    });

    await loadBookings(false);
    document.getElementById("backBtn").style.display = "block";
    scrollToBottom();
});

// ===== BACK BUTTON FOR BOOKINGS =====

document.getElementById("backBtn").addEventListener("click", () => {
    document.getElementById("bookings").style.display = "none";
    document.getElementById("backBtn").style.display = "none";
    scrollToBottom();

});

// ===== DELETE MODE BUTTON =====

document.getElementById("deleteModeBtn").addEventListener("click", async () => {
    clearEditMode();
    document.querySelector(".weather-section").style.display = "none";
    document.getElementById("weatherResult").innerHTML = "";
    document.getElementById("weatherBackBtn").style.display = "none";
    document.getElementById("countryChart").style.display = "none";

    if (window.countryChart instanceof Chart) {
    window.countryChart.destroy();
}
    await loadBookings(true);
    document.getElementById("backBtn").style.display = "block";
    scrollToBottom();
});

// ===== CLEAR EDIT MODE =====

function clearEditMode() {

    document.getElementById("bookingForm").reset();

    document.querySelectorAll("#bookingForm input, #bookingForm select")
        .forEach(field => {
            field.classList.remove("editing-input");
        });

    document.getElementById("submitBtn").textContent = "Book Now";

    document.getElementById("booking_id").value = "";

    updatePrice();
}
// ===== SCROLL HELPER FUNCTION =====

function scrollToBottom() {
    setTimeout(() => {
        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: "smooth"
        });
    }, 100);
}

// ===== WEATHER FEATURE =====

document.getElementById("weatherBtn").addEventListener("click", async () => {
    document.getElementById("bookings").style.display = "none";
    document.getElementById("backBtn").style.display = "none";
    document.getElementById("countryChart").style.display = "none";

    if (window.countryChart instanceof Chart) {
        window.countryChart.destroy();
    }           
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
        scrollToBottom();
        return;
    }

    if (differenceInDays > 15) {
        weatherResult.innerHTML = "<p>Weather forecast is only available up to 15 days ahead.</p>";
        scrollToBottom();
        return;
    }

    const res = await fetch(`/weather?date=${checkInDate}`);
    const data = await res.json();

    if (data.error) {
        weatherResult.innerHTML = `<p>${data.error}</p>`;
        scrollToBottom();
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

// ===== WEATHER BACK BUTTON =====

document.getElementById("weatherBackBtn").addEventListener("click", () => {
    document.querySelector(".weather-section").style.display = "none";
    document.getElementById("weatherResult").innerHTML = "";
    document.getElementById("weatherBackBtn").style.display = "none";
});

// ===== EDIT BOOKING =====
// Loads selected booking into the form for editing / but the actual update is handled by the form submit (PUT request).

document.getElementById("editBtn").addEventListener("click", async () => {
    document.getElementById("countryChart").style.display = "none";

    if (window.countryChart instanceof Chart) {
        window.countryChart.destroy();
    }

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
    `   ;

        container.style.display = "grid";
        document.getElementById("submitBtn").textContent = "Update Booking";
        document.querySelectorAll("#bookingForm input, #bookingForm select")
            .forEach(field => {
                field.classList.add("editing-input");
            });
        alert("Booking loaded. You can now edit the form.");
        document.getElementById("bookingForm").scrollIntoView({
            behavior: "smooth",
            block: "center"
    });
    } else { 
        alert("Booking not found.");
    }
});

// ===== DELETE BOOKING =====

async function deleteBooking(id) {
    if (!confirm("Are you sure you want to delete this booking?")) {
        return;
    }

    const response = await fetch(`/bookings/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {
        alert("Booking deleted successfully");
        await loadBookings(true);
    } else {
        alert("Error deleting booking");
    }
}

// ===== AUTO WEATHER REFRESH =====

document.getElementById("check_in").addEventListener("change", () => {
    const weatherSection = document.querySelector(".weather-section");

    if (weatherSection.style.display === "block") {
        document.getElementById("weatherBtn").click();
    }
});


// ===== BOOKINGS BY COUNTRY CHART =====

document.getElementById("chartBtn").addEventListener("click", async () => {
    document.querySelectorAll("#bookingForm input, #bookingForm select")
    .forEach(field => {
        field.classList.remove("editing-input");
    });

    document.getElementById("submitBtn").textContent = "Book Now";
    document.getElementById("booking_id").value = "";
    document.getElementById("submitBtn").textContent = "Book Now";
    document.getElementById("booking_id").value = "";

    document.getElementById("bookings").style.display = "none";
    document.getElementById("backBtn").style.display = "none";

    document.querySelector(".weather-section").style.display = "none";

    document.getElementById("weatherResult").innerHTML = "";

    document.getElementById("weatherBackBtn").style.display = "none";
    document.getElementById("countryChart").style.display = "block";

    const res = await fetch("/bookings/by-country");
    const data = await res.json();

    const labels = data.map(item => item.country);
    const counts = data.map(item => item.count);
    const total = counts.reduce((a, b) => a + b, 0);
    const ctx = document.getElementById("countryChart").getContext("2d");
    
    if (window.countryChart instanceof Chart) {
        window.countryChart.destroy();
    }

    window.countryChart = new Chart(ctx, {
        type: "pie",

        data: {
            labels: labels,

            datasets: [{
    data: counts,
    backgroundColor: [
        "#4DA8DA",
        "#FF6B8A",
        "#FFA94D",
        "#cc66ff",
        "#5DD39E",
        "#9B5DE5",
        "#B8B8C0",
        "#3FA7F0",
        "#bf5bf1",
        "#00C2A8",
        "#FF9F1C",
        "#6C63FF",
        "#EF476F",
        "#06D6A0",
        "#118AB2",
        "#8338EC",
        "#2c07fb50",
        "#3A86FF",
        "#FFBE0B",
        "#70E000"
    ],
    borderWidth: 10,
    borderColor: "transparent",
    spacing: 8
}]
        },
        options: {
    plugins: {
        legend: {
            position: "bottom",
            labels: {
                color: "#ffffff",
                font: {
                    size: 12,
                    weight: "500"
                }
            }
        }
    }
}
    });
scrollToBottom();
});

