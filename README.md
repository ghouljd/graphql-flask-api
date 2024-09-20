# Flask API Project

This project is a Proof of Concept (POC) for a GraphQL API using Flask.

## Prerequisites

- Python 3.6+
- pip (Python package installer)

## Installation

1. Clone the repository:

```sh
git clone
cd abcall-graphql-flask
```

2. Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

## Running the API

1. Set the Flask application environment variable:

```sh
export FLASK_APP=app.py  # On Windows use `set FLASK_APP=app.py`
```

2. Run the Flask application:

```sh
flask run
```

3. The API will be available at `http://127.0.0.1:5000/`.

## Testing

To run tests, use the following command:

```sh
pytest
```
