# book-review
A project developed with Python (version 3.4) and Django web framework (1.11) to book review using Goodreads API.


# Goodreads Api Documentation
https://www.goodreads.com/api/documentation



## Environment

You must have Python3, Virtualenv, PIP and NPM installed in your machine.  

Create a virtualenv:
```
cd <repo-path>
virtualenv -p python3 venv
```

Activating the environment (**always** do this before performing any other actions):  
```
cd <repo-path>
source venv/bin/activate
```

Installing dependencies:  
```
cd <repo-path>
source venv/bin/activate
pip install -r requirements/dev.txt
```

You need the GoodReads keys in your environment variables:
```
export GOOD_READS_API_SECRET=<your goodreads API secret>
export GOOD_READS_API_KEY=<your goodreads API key>
```

## Run

```
python manage.py runserver
```

## API

To show api endpoint access:
```
http://127.0.0.1:8000/api/books/
```

## Template list books consume API

To access an information table with data API data, go to:
```
http://127.0.0.1:8000/books/table-list/
```
