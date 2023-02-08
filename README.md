# Flask SQL Injection: GameStore Demo Site
## About
This is a Flask web application that is vulnerable to SQL injection. The goal of this web application is show how SQL injection can be performed. This application highlights the SQL executed on the server to show what is happening in the background. __This application is very vulnerable, DO NOT use this application in production.__

This Flask application is a mini website about a fictional game shop called 'GameStore'. The homepage allows users to search for a game, which will show the games that match the query that have been released. The application also includes an admin panel, which allows admins to view, add, delete and update the games in the database. Another option, that is also provided, is to reset the database incase all the data gets deleted from the database.

Possible attacks on the application include: Viewing games that haven't been released, stealing user's credentials and taking control of the admin panel. It is possible to gain full control of the database with this application and therefore it is recommended that you __DO NOT__ use this application on any public server.

## How to Run
### Requirements
To run this application you will need:
- Python 3.7+
- Docker
- Docker-compose

### Installation
To install the required Python libraries, run the command:
```
pip install -r requirements.txt
```

### Running the database
To start the MySQL database, using Docker, run the command:
```
docker-compose up -d
```

To close the MySQL database, run the command:
```
docker-compose stop
```

If you wish to delete the database, run the command:
```
docker-compose down -v
```

### Running the Flask application
To run the Flask application, run the command:
```
python app.py
```

In your web browser, navigate to `http://127.0.0.1:5000` to view the website.

To close the Flask application, press Ctrl+C in the command line to terminate the program.
