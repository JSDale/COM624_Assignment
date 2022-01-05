# COM 624 Assignment

## Abstract

In this assignment I had to create an application that used machine learning to predict future stock prices.

## Technology Used

I plan to use python 3.9 for the backend, implementing a message broker. This gives flexibility for the 
front end. I plan to use a simple C# GUI for the technical demonstrator. The python backend will run in a docker
container.

## Prerequisite

- Python 3.9.2 or later.
- RabbitMQ docker service running. (tutorial)[https://www.architect.io/blog/rabbitmq-docker-tutorial]
- dotnet runtime 5 on a windows 10 or later machine.

## How to run the application(s) - Windows

- First run the `StockPredictor.msi` file. This will install all the necessary files into the file location selected during the installation process. 
- Navigate to the filepath you selected at install time. Open the folder named `StockValuesPredictor\\python_backend`.
- This tutorial will use a virtual environment to run the python backend, if you do not wish to use a venv skip the next two steps.
- Open a terminal in the folder `StockValuesPredictor\\python_backend` and enter `python -m venv ./venv`.
- Then enter `.\venv\Scripts\activate`. Your terminal should now have `(venv)` infront of the filepath.
- Enter `pip install -r requirements.txt`.
- To run the python backend, you must enter `python .\main.py --hostname {hostname of RabbitMQ server} --username {RMQ username} --password {RMQ password} --filepath {where you want the graphs saved}`.
- Then you can navigate back to `StockValuesPredictor` folder in file exploer and run the `StockValuesPredictor.exe`.
- Go to the configure page and enter the hostname of the device running the RMQ server with acceptable username and passwords and click `apply`.
- You can then navigate back to the `Enter stock to predict` page and select model, enter a ticker and select which service to get the information from.
- If all is set up correctly, the python terminal should print a message saying it received a message.



## How to run backend application in dev environment

I used PyCharm to create the python backend, wit a virtual environment. To get you up and running with the dependencies,
I also included a requirements.txt file.

- First, run `python -m venv <filepath of virtual env you want>`
- Then, run `<filepath of virtual env>\Scripts\activate`
- Finally, enter `pip install -r <filepath of project>\requirements.txt`
- Then you can open the folder as a pycharm project and configure the interpretor to be the venv.
