# COM 624 Assignment

## Abstract

In this assignment I had to create an application that used machine learning to predict future stock prices.

## Technology Used

I plan to use python 3.9 for the backend, implementing a message broker. This gives flexibility for the 
front end. I plan to use a simple C# GUI for the technical demonstrator. The python backend will run in a docker
container.

## Prerequisite

- Python 3.9
- RabbitMQ docker service running.
- dotnet runtime 5 on a windows 10 or later machine.

## How to run the application



## How To Build the Python Backend as Docker

- Open a terminal in the `PythonBackend` folder
- There should be a `backend.Dockerfile`
- Run this command in the terminal: `docker build --file ./backend.Dockerfile --tag stock-predicting-backend .`
- To check the image was built, run: `docker images`, there should be an image with the name of `stock-predicting-backend`
- To tag the image, you can run this command: `docker tag stock-predicting-backend:latest [User defined tag]`,  you can enter what you want the tag to be in the `[user defined tag]`. Ensure you remove the square brackets too.



## How to run backend application in dev environment

I used PyCharm to create the python backend, wit a virtual environment. To get you up and running with the dependencies,
I also included a requirements.txt file.

- First, run ```sh python3 -m venv <filepath of virtual env you want>```
- Then, run ```sh <filepath of virtual env you want>\Scripts\activate```
- Finally, enter ```sh pip install -r <filepath of project>\requirements.txt```
