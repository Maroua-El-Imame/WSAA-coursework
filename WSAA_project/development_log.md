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
- [ ] Started `update()` functionality
- [ ] Implemented `delete()`
- [x] Testing DAO independently  

---  

### 4. Flask Server

- [x] Created Flask server file: (`main.py`)
- [x] Created homepage route
- [x] Created `/bookings` API route
- [x] Connected Flask routes to DAO methods
- [x] Returned booking data as JSON
- [x] Tested API route in browser  
- [ ] Implement error handling  

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
- [ ] Add update functionality through the interface
- [ ] Add delete functionality through the interface
- [ ] Improve user Experience

---

### 6. Deployment

- [x] Deployed the Flask application on PythonAnywhere
- [x] Pulled project files from GitHub to PythonAnywhere
- [x] Tested live application

---

### 7. Additional Features

- [x] Added Weather API feature
- [x] Displayed current 'Galway' weather information in the user interface

*!! Potential Future Features*

- [ ] Add availability feature
- [ ] Add rooms section
- [ ] Add guest country/provenance feature
- [ ] Explore additional analysis features such as bookings by date or guest country summary

---

### 8. Final Improvements

- [ ] Improve layout and spacing
- [ ] Final testing
- [ ] Final README update
- [ ] Finalise project documentation  

---

### 9. Current Status

The application currently supports:  

- Viewing bookings
- Creating new bookings
- Displaying bookings grid
- Automatically assigning room prices
- Recording breakfast choice
- Checking 'Galway city' weather  
- Running locally and on PythonAnywhere

---

