# Web Service And Applications - Project   

### Introduction

This project implements a web application using Flask that interacts with an external database through a structured Data Access Object (DAO) layer.

The application follows a modular architecture where the Flask server handles client requests, while the DAO layer manages all data access operations.  
This approach lets the application interact with the database through a separate layer, instead of mixing database code directly into the server, it keeps the code cleaner and easier to manage.  
By keeping these parts separate, the system becomes more flexible, easier to update, and less likely to break. It also follows the way real-world backend applications are built.  




The application follows a modular architecture where the Flask server handles client requests, while the DAO layer manages all data access operations. This approach lets the application interact with the database through a separate layer, instead of mixing database logic directly into the server. This keeps the code cleaner and easier to manage.

By keeping these parts separate, the system becomes more flexible, easier to update, and less likely to break. It also follows the way real-world backend applications are usually built.

---

##  Implementation Progress

### Environment Setup
- [x] Create virtual environment  
- [x] Activate virtual environment  
- [x] Install required packages (Flask)  

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

##  Next Steps
- [ ] Connect DAO to external database  
- [ ] Replace sample data with real database queries  
- [ ] Test database integration  
- [ ] Add additional API endpoints if required  
- [ ] Implement error handling  
- [ ] Finalise project documentation  

---

## 🧪 Development Notes

Temporary scratch files were used during development to test functionality (such as DAO methods and Flask routes) independently before integration.  
These files are used only for testing purposes and will be removed in the final version to keep the project clean and well organised.  
The final application logic is contained in the main project files.  