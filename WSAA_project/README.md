# Blue Bay Hotel


<p align="left">
  <img src="static/images/" alt="" width="100%" height=50>
</p>

**Address:** (fictional)    
Blue Bay Hotel,  
 4 Lighthouse Lane,  
Galway Bay, Ireland

🌀 **Step inside Blue Bay Hotel:** [Visit the web page](https://.pythonanywhere.com/)


~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
<br>

Lecturer : Andrew Beatty  
Web Services and Applications S1-2026  
Higher Diploma in Science in Computing in Data Analytics  
Atlantic Technological University - ATU Galway Mayo 2025/2026.  

Author : Maroua EL imame

Submission deadline : /05/2026

<br>
<br>


### Introduction

This project implements a hotel booking web application using Flask, SQLite and a structured Data Access Object (DAO) layer.

The application follows a modular architecture. The Flask server handles client requests and API routes, while the DAO layer manages data operations separately. 

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

## Development Log 

Full development steps and progress log can be found here : [Development Log](development_log.md)

---

## Environment Setup  


### Prerequisites

Before running the project locally, make sure the following are installed:

- Python 3
- pip
- VS Code or another code editor

No database password or API key is required for this project.  
The application uses SQLite through a local `hotel.db` file, and the weather API endpoint used does not require an API key.

### Local Setup
Steps to run the project locally on your machine:  

Download the project from GitHub:  
><br>

> 1. Go to the GitHub repository in your browser.
> 2. Click the green **Code** button.
> 3. From the dropdown menu, click **Download ZIP**.
> 4. Extract the ZIP folder.
> 5. Open the extracted repository folder.
> 6. Open the `WSAA_project` folder in Comand line or VScode. 
> 
></br>  
<br>

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

Run the Blue Bay Hotel application:

```bash
python server.py
```

Open the local URL shown in the terminal:
Example:

```text
http://127.0.0.1:5000
```

### Deployment Setup  

The project was also deployed and tested on PythonAnywhere.


1. Create a free [PythonAnywhere](https://www.pythonanywhere.com/) account.
2. Open a Bash console in PythonAnywhere.
3. Clone the GitHub repository using: 

```bash
Example:
git clone https://github.com/Maroua-El-Imame/WSAA-coursework.git
```
4. Move into the repository folder:

```bash
Example:
cd ~/WSAA-coursework
```
5. Pull the latest project changes from GitHub:
``` bash 
git pull
```

6. On PythonAnywhere, after pulling the project, run:

```bash
python create_db.py
```


7. Go to the Web tab in PythonAnywhere.
8. Open the web app.
9. Reload the web app to apply the latest changes.  
<br>

**! Note** On PythonAnywhere, the application is served through the Web tab and WSGI configuration.  
For full setup instructions on creating a PythonAnywhere web app and configuring the WSGI file, see the Resources section below.  

## Resources

The core code structure was developed from concepts covered in the Web Services and Applications module lectures, especially Flask applications, API routes, URL handling, JSON data, and frontend-backend communication.

Additional resources were used to support syntax, examples, and further understanding during development.


- [Official PythonAnywhere guide](https://help.pythonanywhere.com/pages/Flask/)
- [Additional PythonAnywhere deployment tutorial](https://www.aicodesnippet.com/python/deployment-and-distribution/deploying-a-simple-web-app-to-pythonanywhere.html)
- [Flask documentation](https://flask.palletsprojects.com/en/stable/deploying/)
- [Open-Meteo Weather API documentation](https://open-meteo.com/en/docs)
- [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html)
- [GeeksforGeeks](https://www.geeksforgeeks.org/python/flask-tutorial/)
- [W3schools](https://www.w3schools.com/python/ref_module_sqlite3.asp)

<br>  

## Contact

Maroua El imame  
Author and sole contributor  
G00472980@atu.ie  