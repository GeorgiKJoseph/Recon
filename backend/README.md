# [Recon](https://#) Live


**Flask** based webapp for traffic anomaly detection.

<br />

> Features

- DBMS: SQLite, PostgreSQL (production)
- DB Tools: SQLAlchemy ORM
- Modular design with **Blueprints**, simple codebase
- Session-Based authentication (via **flask_login**), Forms validation
- Deployment scripts: Docker, Gunicorn / Nginx, Heroku

<br />

> Links

- [Recon](https://#) - LIVE deployment

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/GeorgiKJoseph/Recon.git
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$
$ cd backend
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

[ReconLive](https://#) - Provided by [Cutie](https://#).
