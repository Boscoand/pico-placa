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

## Running the tests

This project contains a set of unit tests that cover the core feature of the API in different scenarios. To execute them, execute the following sencentes in the project root folder: 

```
cd core
source .venv/bin/activate
pytest
```

## Author

* **Bosco Andrade**
