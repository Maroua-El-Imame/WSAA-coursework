# Assignment 04 - GitHub API
# Author: Maroua EL imame

# This program reads a file from a GitHub repository, replaces all instances of the text "Andrew" with the user's name,
# It then commits the changes, and pushes the file back to the repository

# Resources: Lectures and Lab 4 materials were used as guidance for development and debugging.


# import required libraries 
from github import Github, Auth         # GitHub API
from config import config as cfg        # token config 
import requests                         # http request

# load GitHub API token from config.py
api_key = cfg["githubkey"]

# authenticate using the token
auth = Auth.Token(api_key)
g = Github(auth=auth)

# access repository
repo = g.get_repo("Maroua-El-Imame/WSAA-coursework")
print( "connection successful to repository:", repo.clone_url, "\n-----")

# get file from GitHub repository
fileInfo = repo.get_contents("assignments/rwAndrew.txt")
urlOfFile = fileInfo.download_url

# read file content
response = requests.get(urlOfFile)
contentOfFile = response.text

# replace text
newContents = contentOfFile.replace("Andrew", "Maroua").replace("his", "her")
print("Updated content:\n------\n")
print(newContents)

# update file, commit changes and push to repository
gitHubResponse = repo.update_file(
    fileInfo.path,
    "Replace Andrew with Maroua and adjust pronouns",
    newContents,
    fileInfo.sha
)
print("\n-----\nUpdate response:\n------\n")
print(gitHubResponse)


