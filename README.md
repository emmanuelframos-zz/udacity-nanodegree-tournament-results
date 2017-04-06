# Swiss-system Tournament Database Model

## Description
An application to apply and validate Swiss-system tournament database model using unit tests.

## Installing Dependencies
- [Install](https://www.python.org/downloads/) Python 2.7
- [Install](http://initd.org/psycopg/docs/install.html) psycopg2 (PostgreSQL database adapter for Python)
- [Install](https://www.jetbrains.com/pycharm) PyCharm Community IDE for Python
- [Install](https://www.postgresql.org/download) PostgreSQL Database Server with pgAdmin Client

## Running the Tests
- Open pgAdmin and create the database, for example: **TOURNAMENT**
- Select the database and open query tool, run the SQL commands found in **tournament.sql** file
- Edit the **database.properties** file with you database configurations, such as: username, password and more
- Open PyCharm IDE and open a project in application root folder
- Open **tournament_test.py** file, click with right button in file content and select: "Run Unittests for test..."
- Check the console for logs

## Tools versions
- Python 2.7
- PyCharm Community Edition 2017.1
- PostgreSQL Database Server 9.6

## License
It is free software, and may be redistributed.