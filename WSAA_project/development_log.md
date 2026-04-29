## Developpment Log 

This document records the step-by-step development of the hotel booking application, including database setup, backend implementation, and frontend integration.


### Environment Setup
- [x] Create virtual environment  
- [x] Activate virtual environment  
- [x] Install required packages (Flask)  

---  

### SQLite Database Setup
- [x] Create `dbconfig.py` to store SQLite database name
- [x] Create `schema.sql` for bookings table
- [x] Create `createschema.py` to generate database
- [x] Run schema script to create `hotel.db`
- [x] Verify database using SQLite viewer

---  

### Flask Server
- [x] Create Flask server file (`main.py`)  
- [x] Run Flask development server  
- [x] Configure basic application structure  
- [x] Create API route (`/bookings`)  
- [x] Test route in browser  


---  

### DAO Layer
- [x] Create DAO file (`bookingDAO.py`)  
- [x] Design booking data structure  
- [x] Implement `getAll()` method  
- [x] Implement `findByID()` method  
- [x] Implement sample `create()`, `update()`, and `delete()` methods  
- [x] Test DAO independently  

---

### Integration (Flask + DAO)
- [x] Import DAO into Flask server  
- [x] Instantiate DAO object  
- [x] Connect Flask route to DAO method  
- [x] Return JSON response from DAO through Flask  
- [x] Verify end-to-end functionality in browser  


---
### Frontend (HTML + JavaScript)
- [x] Create HTML template (`index.html`)
- [x] Add CSS styling
- [x] Display bookings using GET request
- [x] Add booking form (POST request)
- [x] Display booking reference in User Interface
- [x] Implement DELETE functionality via API

---

##  Next Steps
- [ ] Connect DAO to external database  
- [ ] Replace sample data with real database queries  
- [ ] Test database integration  
- [ ] Add additional API endpoints if required  
- [ ] Implement error handling  
- [ ] Finalise project documentation  

### Next Steps
- [ ] Implement show/hide toggle for bookings
- [ ] Add delete button directly in User Interface
- [ ] Add rooms table
- [ ] Add breakfast option
- [ ] Add pricing logic
- [ ] Improve User Experience
- [ ] Prepare deployment on PythonAnywhere


---