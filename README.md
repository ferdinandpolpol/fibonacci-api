# Fibonacci API
- The goal of this is to create an API that will generate the fibonacci value given it's index

### Setting Up
- Install Docker `https://docs.docker.com/get-docker/`
- Clone this repository and go to repo directory
- docker-compose up


### Usage
Send POST data to URL `http://localhost:8000` with body 
```
{ n: <number> }
```
The Response will be pending if the fibonacci index is unknown and is still being created
```
{
    'status': 'pending'
}
```
Otherwise, it will return the fibonacci value of the given index if it is known
```
{
    'status': 'success',
    'nth': <fib_value>
}
```




### Testing
- docker-compose up
- docker-compose exec web python manage.py test web.fib