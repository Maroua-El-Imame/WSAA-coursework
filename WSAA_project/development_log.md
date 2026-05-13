## Development Log 

This log records the main development stages of the Blue Bay Hotel booking application.  

### 1. Environment Setup

- [x] Created project folder structure
- [x] Created `development_log.md` and README.md
- [x] Created and activated virtual environment  
- [x] Installed required packages  
- [x] Created requirements.txt

---  

### 2. Database Setup

- [x] Created `dbconfig.py` to store SQLite database filename
- [x] Created `schema.sql` for the `bookings` table
- [x] Created `createschema.py` to generate the database
- [x] Generated `hotel.db`
- [x] Verified the database using SQLite viewer  

---

### 3. DAO Layer

- [x] Created `bookingDAO.py`
- [x] Connected DAO to `hotel.db` 
- [x] Implemented `getAll()` method  
- [x] Implemented `findByID()` method  
- [x] Implemented  `create()`
- [x] Implemented `update()` functionality
- [x] Implemented `delete()`
- [x] Testing DAO independently  

---  

### 4. Flask Server

- [x] Created Flask server file: (`server.py`)
- [x] Created homepage route
- [x] Created `/bookings` API route
- [x] Created `/bookings/by-country` API route for analytics
- [x] Connected Flask routes to DAO methods
- [x] Returned booking data as JSON
- [x] Tested API route in browser  
- [x] Implemented error handling  

---

### 5. Frontend

- [x] Created `index.html`
- [x] Created CSS styling
- [x] Created JavaScript file
- [x] Used `fetch()` to display bookings
- [x] Added booking form
- [x] Added booking reference display after submission
- [x] Added room price logic
- [x] Added breakfast option
- [x] Add update functionality through the interface
- [x] Add delete functionality through the interface
- [x] Improve user Experience
- [x] Added collapsible interface sections for bookings, weather, and analytics
- [x] Added Chart.js pie chart for guest country distribution

---

### 6. Deployment

- [x] Deployed the Flask application on PythonAnywhere
- [x] Pulled project files from GitHub to PythonAnywhere
- [x] Tested live application

---

### 7. Additional Features

- [x] Added Weather API feature
- [x] Displayed 'Galway' weather forecast information based on selected check-in date.
- [x] Added guest country analytics chart
- [x] Displayed guest country distribution using a pie chart


---

### 8. Final Improvements

- [x] Improve layout and spacing
- [x] Final testing
- [x] Final README update
- [x] Finalise project documentation  

---

### 9. Current Status

The application currently supports:  

- Viewing all  hotel bookings
- Creating new bookings
- Displaying bookings in a responsive grid layout
- Automatically assigning room prices based on selected room type
- Recording breakfast choice as Bed & Breakfast (BB) or Room Only (RO)
- Updating the total price according to the selected breakfast option
- Updating existing bookings using the booking ID
- Deleting existing bookings using the booking ID
- Checking Galway city weather for a selected stay date
- Viewing guest country distribution using a Chart.js pie chart
- Switching between bookings, weather, and analytics sections
- Running locally and on PythonAnywhere

---

