# Library Management System
A simple flask app to manage users along with mysql service

![Libray Management App - Flask](https://github.com/hamzaavvan/library-management-system/blob/master/ss/ss2.JPG?raw=true)


## Installation

To run the app flawlessly, satisfy the requirements
```bash
pip install -r requirements.txt
```

## Set Environment Variables
```bash
export FLASK_APP=app.py
export FLASk_ENV=development
```

## Setup Datbase
Export `lms.sql` database from within [db](https://github.com/hamza-avvan/library-management-system/tree/master/db) directory using Phpmyadmin or terminal

```bash
mysql -u <username> -p <password> lms < lms.sql
```

## Start Server
```bash
flask run
```

Or run this command 
```bash
python -m flask run
```

Start flask with auto reload on code change
```bash
flask run --reload
```
