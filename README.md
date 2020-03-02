# Pico y Placa Predictor


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Vue 2.5.2
* Vuetify 2.2.15
* Flask 1.1.1
* Python 3.7.5
* Pytest 5.3.5

### Installing

Clone this project in your local machine executing the following instructions: 

```
git clone https://github.com/Boscoand/pico_y_placa.git
```

This project has two independent applications: the web app and the API. To run the API, execute the following statements inside the project root folder:

```
cd core
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
python api.py
```

To run the web app, execute the following steps inside the project root folder in another terminal:

```
cd webapp
npm install
npm run dev
```

Then you are able to open your browser and visit the page http://localhost:8080/ to see the project up. 

![Alt Text](https://media.giphy.com/media/Suy1xNS06nEdHmYtCf/giphy.gif)

## Running the tests

This project contains a set of unit tests that cover the core features that the API provides, and different scenarios are tested. To execute them, execute the following statements in the project root folder: 

```
cd core
source .venv/bin/activate
pytest
```

## Author

* **Bosco Andrade**
