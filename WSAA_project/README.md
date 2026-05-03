# Web Service And Applications - Project   

### Introduction

This project implements a hotel booking web application using Flask, SQLite and a structured Data Access Object (DAO) layer.

The application follows a modular architecture. The Flask server handles client requests and API routes while the DAO layer manages data operations separately. 

This separation keeps the code cleaner, easier to maintain, and closer to the structure used in real-world backend applications.


---

## Project Overview  

Blue Bay Hotel is a Flask web application that allows users to view and create hotel bookings through a browser interface.   

The project includes:

- A frontend interface for viewing and creating bookings
- CRUD operations for managing bookings, with create and read implemented and update/delete started in the DAO/API structure
- A SQLite `bookings` table for storing booking records
- Automatic room price logic
- Breakfast choice recording
- Current Galway weather display using a Weather API
- Deployment and testing on PythonAnywhere


## Technologies Used

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| API Requests | Fetch API |
| Deployment | PythonAnywhere |
| Version Control | Git, GitHub |


## Project Structure

```text
project-folder/
│
├── server.py              # Main Flask app with API routes for booking operations
├── bookingDAO.py          # Handles database actions
├── dbconfig.py            # Stores database name
├── create_db.py           # Helps create/test the database
├── hotel.db               # Hotel booking database
├── createschema.py        # Creates the database from schema.sql
├── schema.sql             # Defines the bookings table
├── requirements.txt       # Python packages needed
├── development_log.md     # Development progress notes
├── README.md              # Project information
│
├── templates/
│   └── index.html         # Main webpage
│
└── static/
    ├── style.css          # Page styling
    ├── app.js             # Page actions and API calls
    └── images/            # Images used in the website

```

### Development Log 

Full development steps and progress log can be found here : [Development Log](development_log.md)

---

## Environment Setup

### Prerequisites

Before running the project locally, make sure the following are installed:

- Python 3
- pip
- VS Code or another code editor

Git is optional. The project can also be downloaded from GitHub as a ZIP file.

### Local Setup

Download the project from GitHub:

```text
Code → Download ZIP → Extract the folder
```

Open the extracted project folder in VS Code.

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create the SQLite database:

```bash
python createschema.py
```

Run the Flask application:

```bash
python server.py
```

Open the application in the browser.

After running `server.py`, the terminal will display a local development URL. Open that URL in the browser.

Example:

```text
http://127.0.0.1:5000
```

---