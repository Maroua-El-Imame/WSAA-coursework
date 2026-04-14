# Web Service And Applications - Assignments sheet  

This repository demonstrates the use of APIs, data handling, and automation using Python.  
It outlines the assignments proposed in the module of Web Service And Applications. 

This repository showcases my progressive learning based on the module’s lectures, demonstrates my ability to conduct independent research, interpret and apply relevant documentation and external resources.  

This repository contains 3 assignments, each covering different stages of course material.

Lecturer : Andrew Beatty  
Web Service And Applications S1-2026   
Higher Diploma in Science in Computing in Data Analytics  
Atlantic Technological University - ATU Galway Mayo 2025/2026.  

Author : Maroua EL imame  




## Assignments Overview :  
The assignments follow the order presented in the module’s lectures  

Assignment 1 : Card draw  
Assignment 2 : Quizz  
Assignment 3 : CSO - Exchequer Account (Historical Series)      
Assignment 4 : GitHub  
Assignment 5 : Quizz  



## Assignments in Detail  

[Deck of Cards API](https://deckofcardsapi.com) :   
an API that simulates dealing a deck of cards

In this program, 5 cards are drawn and printed
-  1: a new deck is shuffled, the API response includes a 'deck_id' which uniquely identifies the deck and is used to draw cards in the next steps. 
-  2: using the 'deck_id', cards are drawn from the deck then a value (rank) and a suit (category) of each card are displayed. 
-  3: the program checks whether Pair, Three of a Kind, Straight, or Flush have been drawn then congratulates the user accordingly.   


**Main technologies used:**   
Python (requests, JSON)  
Requests library for API communication  
JSON for structured data handling  
External REST API (Deck of Cards) for data simulation  


[Exchequer Account (Historical Series)](https://www.cso.ie/en/index.html)  
This program retrieves the dataset for the "exchequer account (historical series)" from the CSO.  
It then stores the data into a file called "cso.json" in the WSAA assignments repository.  

Python (requests,json) was used to send HTTP requests to the CSO API, retrieve the dataset, convert the response into JSON format, and store it locally in a structured and readable way.  

**Main technologies used:**  
requests – handles communication with the CSO RESTT API  
json – used to serialize and save the API response into a readable .json file  

[GitHub API](https://docs.github.com/en/rest)  
This program reads a file from a GitHub repository, replaces all instances of the text "Andrew" with the user's name.  
It then commits the changes, and pushes the file back to the repository. 

Steps followed to complete the assignment:  
- Create a config.py file to store the GitHub token securely (not shared publicly)  
- Add config.py to .gitignore to prevent it from being pushed to GitHub  
- Use the token from config.py to authenticate with the GitHub API  

**Main technologies used:**  
Python – used for scripting, file handling, and text processing.  
PyGithub Library used to interact with the GitHub API (access repository, read and update files).  
Requests library used to retrieve file content via HTTP.  
GitHub REST API – used to access and update files in a remote repository.  

## Resources  

The following websites were primarily used to explore resources in order to complete the weekly tasks.  

[Python documentation](https://docs.python.org/3/)  
[GeeksforGeeks](https://www.geeksforgeeks.org/)  
[Stackoverflow](https://stackoverflow.com/questions)  
[w3schools](https://www.w3schools.com/)  
[Deck of cards API](https://deckofcardsapi.com/)  
[CSO API](https://www.cso.ie/en/index.html)   
[GitHub API](https://docs.github.com/en/rest)  
Lectures and Lab material were used as guidance for development and debugging.  


## Environment Setup :

| Python in Git     |
|----------|

-Navigate to github  
-Click Sign up  
-Follow the prompts to create a personal account.  
***  
-Go to github.  
-Log in to your account.  
-Click the new repository button in the top-right **'+'** symbol   
-Follow [steps](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)  
-Click create repository.  
***  
-On GitHub, navigate to the main page of the repository.  
-Under the repository name, select the code dropdown menu.  
-Click Create codespace on main.  
-From menu top left click on View > Explorer -  
-Under repository title (in bold) click on New file  
-Lower case file name, then add .ipynb extension ( for notebook format) or .py extension ( for python file).  
-Follow steps from developing a code to committing then lastly syncing changes.

| Python on Windows     |
|----------|

[Download cmder](https://cmder.app/)  
[Download notepad++](https://notepad-plus-plus.org/)  
[Download anaconda (python)](https://www.anaconda.com/download)   
[Download vs code](https://code.visualstudio.com/Download)  

*** 
-Open VS Code and select "File > New File",  
    Save the file as .py format (e.g., my_script.py).  
    Write a Python script in the file.  

-With Python file open in VS Code, launch the terminal (see vscode menu)  
    Navigate through the terminal until reaching the same directory where Python file is located.  
    Possible to use Cmder for running Python code (CAT). Same as in Vs code, navigate to the directory where the Python file is 
saved using the cd command.  

-Cmder is mainly for command-line usage, while VS Code is where would most of coding and debugging run.   

-Lastly, steps to [clone repository using command line](https://docs.github.com/en/repositoriescreating-and-managing-repositories/cloning-a-repository)  
    Clone allows to copy the repository from GitHub to the local machine  
    Changes can be pushed to the remote repository on GitHub and/or pulled from Github into the local machine.  

| Python in repository - File browsing & viewing     |
|----------|

-Access the repository: You're already viewing the main [repository](https://github.com/Maroua-El-Imame/programming-for-data-analytics/blob/main/assignments/README.md) page.  
-View python file types: .py or .ipynb .  
-Navigate folder using the file explorer on the left. 
-Click on ipynb files to see their content, code and code output.  
-Notebook ouputs display automatically if no installation is planned.     

### Contact  
Maroua El imame   
Author and sole contributor   
G00472980@atu.ie   