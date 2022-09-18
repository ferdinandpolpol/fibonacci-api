# Fibonacci API
- The goal of this is to create an API that will generate the fibonacci value given it's index

### Setting Up
- docker-compose up


### Usage
Send POST data with body to `http://localhost:8000`
```
{ n: <number> }
```


### Testing
- docker-compose up
- docker-compose exec web python manage.py test web.fib