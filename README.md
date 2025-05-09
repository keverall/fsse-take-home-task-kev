# FastAPI Asynchronous Pair Programming Task

## Overview
Your task will be to build a FastAPI-based web service that interacts asynchronously with a simulated neural network 
backend. The service will receive requests from many clients, batch different parts of the requests together and relay 
those batches onto the backend. The service should efficiently handle multiple client requests while ensuring proper 
deployment practices.

This is a skeleton repo for you to start with which has the Pydantic models used by the clients to send data in their 
requests as well as scripts for sending a client request with the requests library and with locust. You also have 
Pydantic models that we will assume the backend neural networks send back to your service.

## Requirements
1. Implement a FastAPI web app with a POST /predict endpoint that receives a JSON payload (Pydantic model for this 
payload is given), batches the data together and relays it to the backend.
2. The FastAPI web app will not need to perform or send actual requests to a neural network backend, instead it will be 
mocked. We’ll assume the request takes 3-7 seconds to process on the neural network backend. 
3. Each request may use multiple different neural networks so you’ll need a way to split the client requests between 
the different neural networks, batch them with other requests to the same network, and then to disseminate the 
results back to the corresponding client. 
4. The code should be structured, modular and follow best practices.

## Details
The client will send a JSONified Pydantic model which includes a dictionary mapping strings to “agent” requests. Each 
agent request will have at least a vector (list[float]), model name (str) and agent type (str) within it.

Your service should take each agent request, split them and then batch them with other agent requests that have the same
 agent type and that requested the same model as one another. You should end up with a JSON payload to send to the 
backend which houses a list of vectors (list[list[float]] - a matrix) and will receive a response with a vector 
(list[float]) from the backend.

The response from the backend will need to be split up and distributed back to the corresponding clients who made up 
that particular batch of agent requests.

## Installation
Ensure that python3.12, python3.12 venv, and make is installed:

### Ubuntu / Debian
```commandline
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv make
```

### MacOS with brew
```commandline
brew install python@3.12
brew install make
```

### Create Virtual Environment & Install Package
```commandline
make venv
make install
```
